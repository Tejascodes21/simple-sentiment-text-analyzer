from newspaper import Article
from textblob import TextBlob
import nltk
import requests

# Download tokenizer
nltk.download('punkt')

# ✅ Use a single reliable article URL
url = "https://timesofindia.indiatimes.com/technology/tech-news/nvidia-ceo-jensen-huang-theres-a-new-programming-language-it-is-called/articleshow/121746887.cms"
def analyze_article(url):
    try:
        # Check if the article is reachable
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            raise Exception(f"URL not reachable (status code: {response.status_code})")

        # Download and process the article
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        print(f"\n📰 Title: {article.title}")
        print(f"\n📄 Summary:\n{article.summary}")

        # Sentiment Analysis
        blob = TextBlob(article.summary)
        sentiment = blob.sentiment

        print("\n📊 Sentiment Analysis:")
        print(f"  - Polarity: {sentiment.polarity}")
        print(f"  - Subjectivity: {sentiment.subjectivity}")

        # Interpretation
        if sentiment.polarity > 0:
            print("  😊 Overall Sentiment: Positive")
        elif sentiment.polarity < 0:
            print("  😞 Overall Sentiment: Negative")
        else:
            print("  😐 Overall Sentiment: Neutral")

    except Exception as e:
        print("\n❌ Error:", e)

# Run analysis
analyze_article(url)
