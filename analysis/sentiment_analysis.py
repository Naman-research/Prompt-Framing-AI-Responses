from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result['label']
    score = round(result['score'], 4)
    return label, score

if __name__ == "__main__":
    sample_text = "I believe AI can be both helpful and harmful depending on its use."
    label, score = analyze_sentiment(sample_text)
    print(f"Sentiment: {label} | Confidence: {score}")
