"""Nexora harness: an API that returns a mock reply.

Run it with:  uv run main.py   → http://localhost:8000 (docs at /docs)
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Nexora Harness")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.post("/api/chat")
def chat(request: ChatRequest) -> ChatResponse:
    # Mock data for now. Replace this with a real model call later.
    return ChatResponse(reply=f"This is just a mock response. You said: {request.message}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
