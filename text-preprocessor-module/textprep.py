import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.metrics import edit_distance

text = """
Okay, testing for cases so to clear the module
"""
def text_preprocessor(text, case=0):
      no_punctuation = re.sub(r"\W+", " ", text).lower()
      tokens = word_tokenize(no_punctuation)
      stop_words = set(stopwords.words("english"))
      removed_stopwords = [token for token in tokens if token not in stop_words]
      if case == 0:
            return removed_stopwords
      elif case == 1:
            stemmer = PorterStemmer()
            lemmatizer = WordNetLemmatizer()
            stemmed_tokens = [lemmatizer.lemmatize(stemmer.stem(word)) for word in removed_stopwords]
            return stemmed_tokens

      return removed_stopwords

def levenshtein_distance(str1, str2):
      return "The levenshtein distance between the two terms {} AND {} is {}".format(str1, str2, edit_distance)

print(text_preprocessor(text,0))