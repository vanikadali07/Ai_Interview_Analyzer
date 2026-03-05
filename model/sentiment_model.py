from transformers import pipeline

analyzer = pipeline("sentiment-analysis")

def analyze_text(text):
    return analyzer(text)[0]