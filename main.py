from flask import Flask, make_response, jsonify
from data_base import cars

app = Flask(__name__)

@app.route('/cars', methods=['GET'])
def get_cars():
    return make_response(
        jsonify(cars)
    )

app.run()