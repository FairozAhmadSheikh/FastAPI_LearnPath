from fastapi import FastAPI,HTTPException,Depends
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from datetime import datetime,timedelta,timezone
from passlib.context import CryptContext


app=FastAPI()


SECRET_KEY="Mysecretkey"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRY_MINUTES=30


pwd_context=CryptContext(schemes=['bcrypt'])
oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")


fake_database_user={
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("1234")
    }
}



# Create and verify hash  functions
def create_hash(passowrd:str):
    return pwd_context.hash(passowrd)


def verify_password(password:str,hashed_password:str):
    return pwd_context.verify(password,hashed_password)



# Create Token 
def create_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    to_encode.update({
        "exp":expire
    })
    token=jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    return token


# Login API (Oauth2 Token Generator)
@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user=fake_database_user.get(form_data.username)
    if not user or not verify_password(form_data.password,user["hashed_password"]):
        raise HTTPException(status_code=401,detail="Invalid Token")
    access_token=create_token({"sub":form_data.username})
    return{
        "access_token":access_token,
        "bearer":"bearer"
    }
