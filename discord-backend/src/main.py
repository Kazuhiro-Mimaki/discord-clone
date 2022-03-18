from fastapi import FastAPI, WebSocket
from .usecases.user_usecase import user_usecase
from .requests import UserSignupRequest
from fastapi.middleware.cors import CORSMiddleware
import socketio


app = FastAPI()


# ============================
# WebSocket
# ============================
sio = socketio.AsyncServer(async_mode='asgi')
app_socketio = socketio.ASGIApp(sio, other_asgi_app=app)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


# ============================
# Socket
# ============================
@sio.event
def connect(sid, environ):
    print("connect ", sid)


# @sio.on('message')
# async def chat_message(sid, data):
#     print("message ", data)
#     await sio.emit('response', 'hi ' + data)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)
