# Import necessary libraries
from flask import Flask, request, jsonify
import pandas as pd
import textdistance
import re
from collections import Counter
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)
CORS(app)

# Load autocorrect data and model
words = []

with open('book.txt', 'r', encoding='utf-8') as f:
    file_name_data = f.read()
    file_name_data = file_name_data.lower()
    words = re.findall(r'\w+', file_name_data)

V = set(words)
word_freq_dict = Counter(words)
probs = {k: v / sum(word_freq_dict.values()) for k, v in word_freq_dict.items()}

def my_autocorrect(input_word, V, word_freq_dict, probs, threshold=0.5, top_n=5):
    input_word = input_word.lower()
    if input_word in V:
        return ['Your word seems to be correct']
    else:
        similarities = [1 - textdistance.Jaccard(qval=2).distance(v, input_word) for v in word_freq_dict.keys()]
        df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
        df = df.rename(columns={'index': 'Word', 0: 'Prob'})
        df['Similarity'] = similarities
        df_filtered = df[df['Similarity'] >= threshold]
        output = df_filtered.sort_values(['Similarity', 'Prob'], ascending=False).head(top_n)
        return output['Word'].tolist()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_word = data.get('text', '')
    result = my_autocorrect(input_word, V, word_freq_dict, probs)
    return jsonify({'suggestions': result})

# Load next word prediction model and tokenizer
model = tf.keras.models.load_model('C:/Users/MOKSHITH/Desktop/project/Combo/next_word_model.keras')
with open('C:/Users/MOKSHITH/Desktop/project/Combo/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

@app.route('/predict-next', methods=['POST'])
def predict_next():
    data = request.json
    seed_text = data.get('seed_text', '')
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=model.input_shape[1], padding='pre')
    predicted = np.argsort(model.predict(token_list), axis=-1)[0, -3:]
    output_words = [word for word, index in tokenizer.word_index.items() if index in predicted]
    return jsonify({'next_words': output_words})

@app.route('/evaluate-fluency', methods=['POST'])
def evaluate_fluency():
    data = request.json
    sentence = data.get('sentence', '')
    # Placeholder for fluency evaluation logic
    fluency_score = len(sentence.split()) / 10.0  # Simple placeholder logic
    return jsonify({'fluency_score': fluency_score})

if __name__ == '__main__':
    app.run(debug=True, port=5000)