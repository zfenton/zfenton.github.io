from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import users, voting, messages, admin
from .seed_data import sync_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    sync_database()
    yield


app = FastAPI(
    title="Anniversary Voting App",
    description="A voting app for anniversary celebration activities",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://zfenton.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(voting.router)
app.include_router(messages.router)
app.include_router(admin.router)


@app.get("/")
def root():
    return {"message": "Anniversary Voting App API", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
