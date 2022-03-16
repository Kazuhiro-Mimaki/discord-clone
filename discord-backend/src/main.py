from fastapi import FastAPI
from .controller import auth_controller

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/auth", tags=["auth"])
async def auth():
    return {"auth": "call auth"}


@app.post("/api/auth/signup", tags=["signup"])
async def signup():
    return auth_controller.signup()


@app.post("/api/auth/signin", tags=["signin"])
async def signin():
    return auth_controller.signin()
