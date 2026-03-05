def generate_feedback(word_count, filler_count, relevance_score, user_text, ideal_answer):
    feedback = []

    # Length Check
    if word_count < 50:
        feedback.append("Your answer is too short. Expand with more detail and examples.")
    elif word_count > 250:
        feedback.append("Your answer is too long. Make it concise and structured.")

    # Filler Check
    if filler_count > 3:
        feedback.append("Too many filler words. Improve clarity and confidence.")
    elif filler_count > 0:
        feedback.append("Reduce filler words for a more professional tone.")

    # Relevance Check
    if relevance_score < 0.3:
        feedback.append("Your answer is not strongly aligned with the question.")

        # 🔥 Provide Sample Answer
        feedback.append("Here is a sample strong answer you can learn from:")
        feedback.append(ideal_answer)

    elif relevance_score < 0.6:
        feedback.append("Your answer is partially aligned. Strengthen focus on key points.")

        feedback.append("Refer to this sample answer to improve structure:")
        feedback.append(ideal_answer)

    else:
        feedback.append("Your answer is well aligned with the question.")

    # Example Detection
    keywords = ["for example", "during", "in my project", "while working"]
    if not any(word in user_text.lower() for word in keywords):
        feedback.append("Add a real example from your experience to improve impact.")

    return feedback