from flask import Flask, render_template, request, session
from utils.question_bank import get_random_question
from utils.filler_detector import detect_fillers
from utils.scoring import calculate_score
from utils.feedback_engine import generate_feedback
from utils.researched_ideal_answers import ideal_answers
from utils.similarity import calculate_similarity

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session management

@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize session history
    if "history" not in session:
        session["history"] = []

    score = None
    feedback = None
    word_count = None
    filler_info = None
    similarity_score = None
    text = ""

    # POST request with user input
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        question_key = request.form.get("question_key")
        display_question = request.form.get("display_question")

        if text:  # Only process non-empty input
            word_count = len(text.split())

            # Filler detection
            filler_count, found_fillers = detect_fillers(text)
            filler_info = f"{filler_count} filler words: {found_fillers}"

            # Ideal answer & similarity
            ideal_answer = ideal_answers.get(question_key, "")
            similarity_score = calculate_similarity(text, ideal_answer) if ideal_answer else 0
            relevance_score = similarity_score / 100

            # Scoring & feedback
            score = calculate_score(similarity_score, word_count, filler_count)
            feedback = generate_feedback(word_count, filler_count, relevance_score, text, ideal_answer)

            # Save only user response to history
            history = session.get("history", [])
            # Avoid duplicate entries for the same question + answer
            if not history or history[-1]["answer"] != text:
                history.append({
                    "question": display_question,
                    "answer": text,       # Only user input
                    "score": round(score, 2),
                    "similarity": round(similarity_score, 2)
                })
                session["history"] = history

        # Get next question
        question_key, display_question = get_random_question()
        text = ""  # Reset textarea

    else:
        # GET request — first visit
        question_key, display_question = get_random_question()

    return render_template(
        "index.html",
        question_key=question_key,
        display_question=display_question,
        score=score,
        feedback=feedback,
        word_count=word_count,
        filler_info=filler_info,
        similarity_score=similarity_score,
        history=session.get("history", [])
    )

if __name__ == "__main__":
    app.run(debug=True)