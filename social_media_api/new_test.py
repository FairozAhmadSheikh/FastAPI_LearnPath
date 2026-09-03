from fastapi import FastAPI,Depends,HTTPException
from datetime import datetime,timezone,timedelta
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import jwt,JWTError
from passlib.context import CryptContext


app=FastAPI()

pwd_context=CryptContext(schemes=['bcrypt'])
oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY="mysecretkey"
ALGORITHM='HS256'
TOKEN_EXPIRY_MINUTES=30

fake_database={
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("123")
    }
}

def create_hash(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

# Create a token 
def create_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=TOKEN_EXPIRY_MINUTES)
    to_encode.update({
        "exp":expire   
    })
    token=jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    return token 

@app.route("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user=fake_database.get(form_data.username)
    if not user or not verify_password(form_data.password,user["hashed_password"]):
        raise HTTPException(status_code=401,detail="Invalid Username or Password")
    access_token=create_token({"sub":form_data.username})
    return {
        "access_token":access_token,
        "bearer":"bearer"
    }

def verify_token(token:str=Depends(oauth2_schema)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get("sub")
        if username is None :
            raise HTTPException(
                status_code=401,
                detail="Invalid token "
            )
        return username
    except JWTError:
        raise HTTPException(status_code=401,
                            detail="Invalid Token ")

@app.get("/secured")
def secured(user:str=Depends(verify_token)):
    return{
        "message":"Access Provided",
        "username":user
    }