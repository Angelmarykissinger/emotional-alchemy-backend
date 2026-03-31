import os
import json
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Load Gemini Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

# Gemini Client
client = genai.Client(api_key=api_key)


# ============================
# ✅ Chat Function
# ============================
def get_gemini_reply(user_message: str) -> str:
    try:
        prompt = f"""
        You are an empathetic, emotionally positive support companion. 
        The user says: "{user_message}"
        
        Please respond with an uplifting, encouraging, and emotionally positive message. 
        You MUST also provide a gentle, positive, and actionable suggestion to help improve the user's mood right now.
        Keep your entire response conversational, perfectly balanced, and strictly under 7 sentences maximum.
        Do not use bullet points, lists, or markdown formatting.
        """
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("🔥 Gemini Error:", e)
        return "Sorry, I couldn’t reply right now 💜"

# ============================
# ✅ Mood Analysis Function
# ============================
def analyze_mood(user_message: str) -> dict:
    try:
        prompt = f"""
        Analyze the emotion of the following journal entry: "{user_message}"
        Respond strictly in valid JSON format with three keys:
        - "label": One of these exact strings: [Happy, Sad, Stressed, Neutral, Joyful, Low, Angry]
        - "score": A float from 1.0 to 10.0 representing positivity (1.0 is extremely negative, 10.0 is extremely positive)
        - "recommendation": A short comforting or encouraging tip.
        Do not include any markdown formatting or extra text.
        """
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
            
        return json.loads(text.strip())

    except Exception as e:
        print("🔥 Gemini Error in analyze_mood:", e)
        return {"label": "Neutral", "score": 5.0, "recommendation": "Take a deep breath 💜"}
