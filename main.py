from textblob import TextBlob

# LLM used: ChatGPT


def analyze_sentiment(text):
    """Analyzes the sentiment of a given text and classifies it as Positive, Negative, or Neutral."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Polarity ranges from -1 to 1

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


if __name__ == "__main__":
    # Example Inputs
    test_sentences = [
        "I love this product! It's amazing.",
        "This is the worst experience I've ever had.",
        "It's an average day, nothing special."
    ]

    # Running Sentiment Analysis on test cases
    for sentence in test_sentences:
        sentiment = analyze_sentiment(sentence)
        print(f"Text: \"{sentence}\" -> Sentiment: {sentiment}")

    message = input("Enter a message: ")

    print(f"\nUser message: {message} -> Sentiment: {analyze_sentiment(message)}")
