from fastapi import FastAPI
from .usecases.user_usecase import user_usecase
from .requests import UserSignupRequest

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/auth", tags=["auth"])
async def auth():
    return {"auth": "call auth"}


@app.post("/api/auth/signup", tags=["signup"])
async def signup(request: UserSignupRequest):
    return user_usecase.signup(request=request)


@app.post("/api/auth/signin", tags=["signin"])
async def signin():
    return user_usecase.signin()
