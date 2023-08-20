from flask import Flask, request, render_template, jsonify
from pycaret.anomaly import *
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = load_model('iforest_pipeline')
cols = ['FISCAL_YR', 'FISCAL_MTH', 'DEPT_NAME', 'DIV_NAME', 'MERCHANT', 'CAT_DESC', 'TRANS_DT', 'AMT']

@app.route('/')
def home():
    return render_template("index.html")



@app.route('/detect_anomaly', methods=['POST'])
def detect_anomaly():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns=cols)
    anomaly_result = predict_model(model, data=data_unseen)
    print(anomaly_result)
    anomaly = anomaly_result['Anomaly'][0]
    anomaly_score = anomaly_result['Anomaly_Score'][0]
    return render_template('index.html', pred="Anomaly: {}. Anomaly Score: {}".format(anomaly, anomaly_score))


@app.route('/detect_anomaly_api', methods=['POST'])
def detect_anomaly_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    anomaly_result = predict_model(model, data=data_unseen)
    anomaly = anomaly_result['Anomaly'][0]
    anomaly_score = anomaly_result['Anomaly_Score'][0]

    if anomaly >= 0.5:
        anomaly_status = "anomaly"
    else:
        anomaly_status = "normal"

    output = {
        "anomaly_status": anomaly_status,
        "anomaly": anomaly,
        "anomaly_score": anomaly_score
    }

    return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)