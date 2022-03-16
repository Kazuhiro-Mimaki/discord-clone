from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/auth", tags=["auth"])
async def auth():
    return {"auth": "call auth"}


@app.post("/api/auth/register", tags=["register"])
async def auth():
    return {"register": "register"}


@app.post("/api/auth/login", tags=["login"])
async def auth():
    return {"login": "login"}
