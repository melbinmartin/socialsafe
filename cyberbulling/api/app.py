from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler


model_file = 'model.pkl'
model = joblib.load(model_file)

vectorizer_file = 'vector.pkl'
vectorizer = joblib.load(vectorizer_file)

scaler_file = 'scaler.pkl'
scaler = joblib.load(scaler_file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():
    text = request.json['text']
    input_vec = vectorizer.transform([text])
    input_scaled = scaler.transform(input_vec)
    prediction_proba = model.predict_proba(input_scaled)
    prediction = model.predict(input_scaled)
    if prediction == 1:
        result = "Cyberbullying detected." 
    else:
        result = "No cyberbullying detected."

    return jsonify(result=result, probability=float(prediction_proba[0, 1]))


if __name__ == '__main__':
    app.run()
