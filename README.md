# AI_INTERVIEW_ANALYZER

AI Interview Analyzer is a web app for practicing technical interviews. It evaluates your answers with scoring, filler word detection, relevance, and similarity to ideal answers.

Technology Stack

1.Backend: Python, Flask
2.Frontend: HTML, CSS, JavaScript
3.Deployment: Render (Gunicorn + Flask)
4.NLP: sentence-transformers, Transformers, Torch

Live Demo:https://ai-interview-analyzer-kghb.onrender.com

Usage

-Open the app in a browser.

-Read the randomly displayed question.

-Submit your answer.

-View the score, feedback, word count, filler words, and session history.

Installation (Local)

Clone the repo:
git clone https://github.com/vanikadali07/Ai_Interview_Analyzer.git

Go to the project folder:
cd Ai_Interview_Analyzer

Create and activate a virtual environment:
python -m venv venv
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run the app:
python app.py

Deployment

Render is used to deploy this app with:
web: gunicorn app:app

Live link: https://ai-interview-analyzer-kghb.onrender.com
