from fastapi import FastAPI,Request
import time 

app=FastAPI()

@app.middleware("http")
def log_middleware(request:Request,call_next):
    start_time=time.time()
    print(f"request recieved at {start_time}")
    response=call_next(request)
    process_time=time.time()-start_time
    print(f'Path:{request.url.path}| Time {process_time}')
    return response
