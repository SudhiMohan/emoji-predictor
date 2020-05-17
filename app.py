from flask import Flask, render_template
import preprocessor
from preprocessor import preprocess_text
import model
from model import get_model
import tokenizer
from tokenizer import get_tokenizer
import pandas as pd
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from mappings import map_emoji

tokenizer = get_tokenizer()
model = get_model()

app = Flask(__name__)


@app.route('/<string:text>')
def index(text):
    text_processed = preprocess_text(text)
    df_test = pd.DataFrame({'Text': [text_processed]})
    X_predict = tokenizer.texts_to_sequences(df_test['Text'].values)
    print("Here")
    X_predict = pad_sequences(X_predict)
    pred = model.predict(X_predict)
    pred_labels = np.argmax(pred, axis=1)
    pred_emojis = map_emoji(pred_labels)
    return pred_emojis[0]


if __name__ == '__main__':
    app.run(debug=True)
