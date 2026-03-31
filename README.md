The Emotional Alchemy Backend provides the server-side logic for the Emotional Alchemy emotional wellness application.  
It processes user journal entries and chat messages, performs sentiment analysis, and returns mood scores that help the mobile application generate emotional insights.

Features
- Sentiment analysis for journal entries and chat messages
- Mood score generation based on detected emotions
- API endpoints to interact with the Flutter frontend
- Secure environment configuration using `.env` files

Technologies Used
- Python
- FastAPI / Flask (depending on your framework)
- Natural Language Processing (NLP)
- REST API architecture

Project Structure

emotional-alchemy-backend
 - main.py # Main API server
 - api_service.py # Core sentiment analysis logic
 - requirements.txt # Python dependencies
 - Procfile # Deployment configuration

Installation
1. Clone the repository
git clone https://github.com/Angelmarykissinger/emotional-alchemy-backend.git
2. Navigate to the project folder
cd emotional-alchemy-backend
3. Install dependencies
pip install -r requirements.txt
4. Run the backend server
python main.py

API Function

The backend receives text input from the mobile app and returns a calculated mood score based on sentiment analysis.

Example workflow:
1. User writes a journal entry in the mobile app
2. Text is sent to the backend API
3. Sentiment analysis is performed
4. A mood score is returned to the app

Security

Sensitive configuration values such as API keys are stored in a `.env` file and excluded from the repository using `.gitignore`.

Related Project

Frontend mobile application built using **Flutter and Firebase**.
Frontend repository:
https://github.com/Angelmarykissinger/emotional-alchemy

Future Improvements
- Advanced NLP models for deeper emotional understanding
- AI based recommendations
- Scalable cloud deployment
