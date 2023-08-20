from flask import Flask,request, url_for, redirect, render_template, jsonify
from pycaret.regression import *
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = load_model(r'C:/Users/JJ Yit/Desktop/NYP STuff/Year 3 things/Machine Learning Operations/Machine Learning Ops Assignment/MLOPS Assignment/models/resale_pipeline')
cols = ['town', 'month', 'flat_type', 'storey_range', 'floor_area_sqm', 'flat_model', 'lease_commence_date', 'cbd_dist', 'min_dist_mrt']
@app.route('/')
def home():
    return render_template("jj_home.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen, round = 0)
    print(prediction)
    prediction = int(prediction.prediction_label)
    return render_template('jj_home.html',pred='Predicted resale price is ${}'.format(prediction))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = predict_model(model, data=data_unseen)
    output = prediction.prediction_label
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# from flask import Flask,request, url_for, redirect, render_template, jsonify
# from pycaret.regression import *
# import pandas as pd
# import pickle
# import numpy as np
#
# app = Flask(__name__)
#
# model = load_model('resale_pipeline')
# cols = ['town', 'month', 'flat_type', 'storey_range', 'floor_area_sqm', 'flat_model', 'lease_commence_date', 'cbd_dist', 'min_dist_mrt']
#
# @app.route('/')
# def home():
#     return render_template("home.html")
#
# @app.route('/predict',methods=['POST'])
# def predict():
# 	int_features = [x for x in request.form.values()]
# 	final = np.array(int_features)
# 	data_unseen = pd.DataFrame([final], columns = cols)
# 	prediction = predict_model(model, data=data_unseen, round = 0)
# 	prediction = int(prediction.resale_price[0])
# 	return render_template('home.html', pred = 'Expected Resale Price will be ${}'.format(prediction))
#
# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     data = request.get_json(force=True)
#     data_unseen = pd.DataFrame([data])
#     prediction = predict_model(model, data=data_unseen)
#     output = prediction.resale_price[0]
#     return jsonify(output)
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
