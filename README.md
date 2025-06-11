# Simple Sentiment Text Analyzer 📰📊
A simple Python script that fetches a news article from the web, summarizes it, and performs basic sentiment analysis using newspaper3k and TextBlob. Great for quick insights into how an article feels — positive, negative, or neutral.

# Simple Sentiment Text Analyzer 📰📊

This is a small Python script I built to analyze the sentiment of online news articles. It uses the `newspaper3k` library to fetch and summarize the article, and then uses `TextBlob` to run a basic sentiment analysis.

It's meant to be a simple, minimal tool for learning and experimenting with sentiment analysis on real-world content.

---

## What it does

- Takes a single news article URL
- Extracts the article title and summary
- Runs sentiment analysis on the summary
- Prints out the polarity and subjectivity
- Labels the article as Positive, Negative, or Neutral
- Optionally saves everything to a local `.txt` file



## How to use it

1. Clone this repo or copy the script.
2. Install the required libraries (see below).
3. Change the `url` variable in the script to any valid news article.
4. Run the script.

```bash
python analyze_article.py



# Simple Sentiment Text Analyzer 📰📊

This is a small Python script I built to analyze the sentiment of online news articles. It uses the `newspaper3k` library to fetch and summarize the article, and then uses `TextBlob` to run a basic sentiment analysis.

It's meant to be a simple, minimal tool for learning and experimenting with sentiment analysis on real-world content.

---

## What it does

- Takes a single news article URL
- Extracts the article title and summary
- Runs sentiment analysis on the summary
- Prints out the polarity and subjectivity
- Labels the article as Positive, Negative, or Neutral
- Optionally saves everything to a local `.txt` file

---

## How to use it

1. Clone this repo or copy the script.
2. Install the required libraries (see below).
3. Change the `url` variable in the script to any valid news article.
4. Run the script.

```bash
python analyze_article.py
````

---

## Requirements

Install the libraries with:

```bash
pip install newspaper3k textblob requests
python -m textblob.download_corpora
```

You’ll also need to download the NLTK tokenizer (used internally):

```python
import nltk
nltk.download('punkt')
```

---

## Example output

```
📰 Title: Nvidia CEO: There's a new programming language...

📄 Summary:
Nvidia CEO Jensen Huang recently said...

📊 Sentiment Analysis:
  - Polarity: 0.22
  - Subjectivity: 0.38
  😊 Overall Sentiment: Positive
```

---

## Things I might add later

* Support for multiple URLs
* Option to read URLs from a file
* Better sentiment model using `transformers`
* Maybe a simple Streamlit front-end

---

## Why I made this

I just wanted a lightweight script that could give me a quick read on how an article “feels.” It's nothing fancy, but it's a good starting point if you're learning about NLP or working with media content.

---
