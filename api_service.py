import os
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
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=user_message
        )

        return response.text

    except Exception as e:
        print("🔥 Gemini Error:", e)
        return "Sorry, I couldn’t reply right now 💜"
