import dill as pickle
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

import re, string, os

class PredictModel:
    def __init__(_self):
        with open(os.getcwd() + '/social/analysis.pk', 'rb') as fin:
            _self.classifier = pickle.load(fin)

    def predict(_self, input): 
        custom_tokens = _self._remove_noise(word_tokenize(input))
        result = _self.classifier.classify(dict([token, True] for token in custom_tokens))
        print(input, result)

        return result

    def _remove_noise(_self, tweet_tokens, stop_words = ()):
        cleaned_tokens = []

        for token, tag in pos_tag(tweet_tokens):
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                        '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
            token = re.sub("(@[A-Za-z0-9_]+)","", token)

            if tag.startswith("NN"):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)

            if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
                cleaned_tokens.append(token.lower())
        return cleaned_tokens

# def remove_noise(tweet_tokens, stop_words = ()):
