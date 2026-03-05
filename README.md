# AI_INTERVIEW_ANALYZER
AI Interview Analyzer

Live Demo: https://ai-interview-analyzer-kghb.onrender.com

AI Interview Analyzer is a web application designed to simulate technical interviews and provide users with detailed evaluation of their responses, including scoring, filler word detection, relevance, and similarity to ideal answers.

Features

Random interview questions for practice

Automated evaluation of user responses:

Similarity score against ideal answers

Word count

Filler word detection

Relevance scoring

Actionable feedback on answers

Session-based answer history for tracking progress

Clean, user-friendly interface

Technology Stack
Layer	Technology
Backend	Python, Flask
Frontend	HTML, CSS, JavaScript
Deployment	Render (Gunicorn + Flask)
NLP	sentence-transformers, Transformers, Torch
Session	Flask session storage
Requirements

All required Python packages are listed in requirements.txt, including:

Flask
gunicorn
torch
transformers
sentence-transformers
scikit-learn
numpy
scipy
Installation (Local)

Clone the repository:

git clone https://github.com/vanikadali07/Ai_Interview_Analyzer.git
cd Ai_Interview_Analyzer

Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open your browser at:

http://127.0.0.1:5000
Usage

Open the app in a browser.

A random interview question is displayed.

Enter your answer in the text box.

Submit to receive:

Score

Feedback

Word count

List of filler words

Session history of answers

Deployment on Render

The application is deployed on Render using a Procfile:

web: gunicorn app:app

Live link: https://ai-interview-analyzer-kghb.onrender.com

Project Structure
Ai_Interview_Analyzer/
│── app.py
│── Procfile
│── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── utils/
    ├── question_bank.py
    ├── filler_detector.py
    ├── similarity.py
    ├── scoring.py
    ├── feedback_engine.py
    └── researched_ideal_answers.py
How It Works

The homepage loads a random question.

User submits an answer.

The app:

Counts the number of words

Detects filler words

Computes similarity with the ideal answer

Calculates a final score

Generates feedback

User answers are stored in session history for review.

Future Improvements

Persistent user accounts and database storage

Audio input with speech-to-text evaluation

Graphical analytics for scores and progress

Leaderboards or progress tracking

Scheduled mock interview sessions
