from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from api_service import get_gemini_reply, analyze_mood
import os

app = FastAPI()

# ✅ Allow Flutter App Requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request Model
# -----------------------------
class ChatRequest(BaseModel):
    message: str

# -----------------------------
# Root Test
# -----------------------------
@app.get("/")
def home():
    return {"status": "Backend is running 🚀"}

# -----------------------------
# Chat Endpoint
# -----------------------------
@app.post("/chat")
def chat(req: ChatRequest):
    reply = get_gemini_reply(req.message)
    return {"response": reply}

# -----------------------------
# Analyze Mood Endpoint
# -----------------------------
@app.post("/analyze_mood")
def analyze_mood_endpoint(req: ChatRequest):
    result = analyze_mood(req.message)
    return result
