from fastapi import FastAPI, WebSocket
from src.requests.user import UserSigninRequest, UserSignupRequest
from .usecases import user_usecase, msg_usecase
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import json

app = FastAPI()
load_dotenv()


# ============================
# WebSocket
# ============================

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
async def signup(req: UserSignupRequest):
    return user_usecase.signup(req=req)


@app.post("/api/auth/signin", tags=["signin"])
async def signin(req: UserSigninRequest):
    return user_usecase.signin(req=req)


# ============================
# Socket
# ============================
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("Accepting Connection")
    await websocket.accept()
    print("Accepted")
    key = websocket.headers.get('sec-websocket-key')
    clients = {}
    clients[key] = websocket
    while True:
        try:
            data = await websocket.receive_text()
            json_data = json.loads(data)
            msg_list = msg_usecase.create(req=json_data)
            output = []
            for msg in msg_list:
                output.append({"id": msg.id, "content": msg.content})
            print(clients)
            for client in clients.values():
                await client.send_json(output)
            # await websocket.send_json(output)
        except:
            pass
            break
