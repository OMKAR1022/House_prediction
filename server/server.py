from http.client import responses
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

if __name__ == "__main__":
    print("Starting Flask Server....")
    app.run()