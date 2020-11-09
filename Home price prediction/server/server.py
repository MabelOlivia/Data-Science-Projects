from flask import Flask, request, jsonify
import utils

app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        "locations" : utils.get_location_names()
    })
    response.headers.add('Access_Control-Allow-Origin', "*")

    return response


@app.route("/predict_home_price", methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bedroom = int(request.form['bedroom'])
    bath = int(request.form['bath'])

    response = jsonify({
        "estimated_price" : utils.get_estimated_price(location,total_sqft,bedroom,bath)

    })
    response.headers.add('Access_Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    utils.load_saved_artifacts()
    app.run()