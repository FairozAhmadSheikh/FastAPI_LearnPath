from fastapi import FastAPI,Depends,HTTPException,Request,Header
from fastapi.responses import JSONResponse

app= FastAPI()

# COMMON USEABLE METHOD
def verify_token(token:str=Header(None)):
    if token !="mysupersecret":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return JSONResponse(
        status_code=200,
        content={
            "user":"Authorized user "
        }
    )

@app.get("/secure")
def user(data=Depends(verify_token)):
    return{
        "message":"Secure data access ",
        "data":data
    }

# Another Example
users_online=['ali','fairoz']
def get_current_user():
    return {
        "user":[u for u in users_online]
    }

@app.get('/profile')
def profile(user=Depends(get_current_user)):
    return user

@app.get('/dashboard')
def dashboard(user=Depends(get_current_user)):
    return user