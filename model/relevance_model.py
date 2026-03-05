from transformers import pipeline

similarity_model = pipeline("feature-extraction", model="sentence-transformers/all-MiniLM-L6-v2")

def get_embedding(text):
    return similarity_model(text)[0][0]