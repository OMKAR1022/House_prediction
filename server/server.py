from http.client import responses

from joblib.parallel import method

import util
from flask import Flask ,request,jsonify

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    return "Hii"


@app.route('/predict_home_price',methods =['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'prediction_price': util.get_prediction_price(location,total_sqft,bhk,bath)
    })
    return response

if __name__ == "__main__":
    print("Starting Flask Server.... predicting home prices >>>")
    util.load_saved_artifacts()
    app.run()