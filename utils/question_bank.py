import random

questions = {
    "tell_me_about_yourself": "Tell me about yourself.",
    "greatest_strength": "What is your greatest strength?",
    "greatest_weakness": "What is your greatest weakness?",
    "challenge_faced": "Describe a time you faced a challenge at work.",
    "team_conflict": "Explain a time you handled conflict in a team.",
    "five_years": "Where do you see yourself in 5 years?",
    "why_should_we_hire_you": "Why should we hire you?",
    "leadership_example": "Give an example of leadership.",
    "handle_stress": "How do you handle stress and pressure?",
    "failure_example": "Tell me about a time you failed and learned from it."
}

def get_random_question():
    key = random.choice(list(questions.keys()))
    return key, questions[key]