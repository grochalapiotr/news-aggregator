import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')


class SentimentAnalyzer:
      
    def __init__(self) -> None:
        pass
      
    def analyze_sentiment(self, text):
        sid = SentimentIntensityAnalyzer()
        sentiment_scores = sid.polarity_scores(text)
        
        # Determine sentiment based on the compound score
        compound_score = sentiment_scores['compound']
        
        if compound_score >= 0.05:
            return "Positive"
        elif -0.05 < compound_score < 0.05:
            return "Neutral"
        else:
            return "Negative"