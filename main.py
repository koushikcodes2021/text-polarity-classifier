from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt')

url = 'https://www.bbc.com/news/entertainment-arts-58456170'

article = Article(url)
article.download()
article.parse()
article.nlp()

text = article.text


blob = TextBlob(text)

sentiment = blob.sentiment.polarity

print(sentiment)
