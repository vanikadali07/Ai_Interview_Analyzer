from sentence_transformers import SentenceTransformer, util
from utils.researched_ideal_answers import researched_ideal_answers

model = SentenceTransformer("all-MiniLM-L6-v2")

ideal_embeddings = {}

for key, answer in researched_ideal_answers.items():
    ideal_embeddings[key] = model.encode(answer, convert_to_tensor=True)


def evaluate_answer(question_key, user_answer):
    if question_key not in ideal_embeddings:
        return {"error": "Invalid question key"}

    user_embedding = model.encode(user_answer, convert_to_tensor=True)

    cosine_score = util.cos_sim(
        user_embedding,
        ideal_embeddings[question_key]
    )

    similarity = float(cosine_score[0][0])
    score = max(0, min(similarity * 100, 100))

    return {
        "score": round(score, 2),
        "similarity": similarity
    }