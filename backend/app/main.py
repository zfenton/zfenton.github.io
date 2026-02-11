from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routes import users, voting, messages, admin

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Anniversary Voting App",
    description="A voting app for anniversary celebration activities",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
