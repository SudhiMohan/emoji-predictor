import pickle
from sklearn.externals import joblib

def get_tokenizer():
    tokenizer_pkl = open('data/tokenizer.pkl','rb')
    tokenizer = joblib.load(tokenizer_pkl)
    return tokenizer