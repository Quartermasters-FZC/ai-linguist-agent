from transformers import pipeline

# Use a zero-shot classifier as placeholder for AI detection
classifier = pipeline("text-classification", model="roberta-base")

def detect_ai_content(text):
    result = classifier(text, truncation=True)
    return result[0]['score']
