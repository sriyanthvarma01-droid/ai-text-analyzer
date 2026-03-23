from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="finiteautomata/bertweet-base-sentiment-analysis"
)

text = input("Enter text: ")
print(sentiment_pipeline(text))