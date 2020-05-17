import re
import string
import unicodedata
import nltk
import inflect
import numpy as np

from nltk import word_tokenize
from nltk.corpus import stopwords


def select_words(text):
    words = np.asarray(re.split(r'\W+', text))
    return words


def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


def remove_numbers(text):
    """Remove numbers from list of tokenized words"""
    new_words = []
    for word in text:
        if not word.isdigit():
            new_words.append(word)
    return new_words


def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in set(('', ' ')):
            new_words.append(word)
    return new_words


def normalize_words(words):
    words = remove_non_ascii(words)
    words = remove_numbers(words)
    words = remove_stopwords(words)
    return words


def preprocess_text(text):
    text_processed = select_words(text.lower())
    text_processed = normalize_words(text_processed)
    return ' '.join(text_processed)
