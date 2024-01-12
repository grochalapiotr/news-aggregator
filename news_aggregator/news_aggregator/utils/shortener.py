import nltk
import json
import numpy as np
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance

nltk.download('stopwords')


class Shortener:
    def __init__(self) -> None:
        pass


    def sentence_similarity(self, sent1, sent2, stopwords=None):
        if stopwords is None:
            stopwords = []
        
        words1 = [word.lower() for word in sent1.split() if word.isalnum() and word.lower() not in stopwords]
        words2 = [word.lower() for word in sent2.split() if word.isalnum() and word.lower() not in stopwords]

        all_words = list(set(words1 + words2))

        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)

        for word in words1:
            vector1[all_words.index(word)] += 1

        for word in words2:
            vector2[all_words.index(word)] += 1

        return 1 - cosine_distance(vector1, vector2)

    def build_similarity_matrix(self, sentences, stopwords):
        similarity_matrix = np.zeros((len(sentences), len(sentences)))

        for i in range(len(sentences)):
            for j in range(len(sentences)):
                if i != j:
                    similarity_matrix[i][j] = self.sentence_similarity(sentences[i], sentences[j], stopwords)

        return similarity_matrix

    def generate_summary(self, text, top_n=5):        #top_n - how many sentences should be in summary
        article = text
        sentences = nltk.sent_tokenize(article)
        stopwords = nltk.corpus.stopwords.words("english")

        sentence_similarity_matrix = self.build_similarity_matrix(sentences, stopwords)

        sentence_similarity_scores = np.zeros(len(sentences))
        for i in range(len(sentences)):
            sentence_similarity_scores[i] = sum(sentence_similarity_matrix[i])

        ranked_sentences = [sentences[i] for i in np.argsort(sentence_similarity_scores)[::-1][:top_n]]

        return " ".join(ranked_sentences)

# Example usage

# with open('articles/bbc.json') as f:
#     articles = json.load(f)

# for i in range(len(articles)):
#     article_text = ' '.join(articles[i]["text"]).replace("  ", " ")
#     summary = Shortener().generate_summary(article_text)
#     print("Title: "+articles[i]["title"])
#     print("Summary:")
#     print(summary)
#     print("-------------------")






