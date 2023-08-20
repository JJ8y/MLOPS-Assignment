from flask import Flask,request, url_for, redirect, render_template, jsonify
from pycaret.classification import *
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = load_model('ensemble_model')
cols = ['age', 'gender', 'chest_pain', 'resting_BP', 'cholesterol', 'fasting_BS', 'resting_ECG', 'max_HR',
        'exercise_angina', 'old_peak', 'ST_slope']


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict_resale')
def predict_resale():
    return render_template('home-jj.html')

@app.route('/detect_anomaly')
def detect_anomaly():
    return render_template('index-keith.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns=cols)
    prediction = predict_model(model, data=data_unseen)
    print(prediction,flush=True)#check output in python console
    predicted_class = int(prediction['prediction_label'][0])

    return render_template('home.html', pred='Presence of cardiovascular issue: {}'.format(predicted_class))


@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])

    # Perform classification prediction
    prediction = predict_model(model, data=data_unseen)
    predicted_class = int(prediction['prediction_label'][0])

    return jsonify(predicted_class)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)






