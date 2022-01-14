from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS, cross_origin
from src.main import (url_bitcoin, 
url_ethereum,
url_cryptocurrency,
url_global_finance,
url_indian_finance,
getJSONData
)
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route("/bitcoin/")
@cross_origin()
def bitcoin():
    return jsonify(getJSONData(url_bitcoin))

@app.route("/ethereum/")
@cross_origin()
def ethereum():
    return jsonify(getJSONData(url_ethereum))

@app.route("/cryptocurrency/")
@cross_origin()
def cryptocurrency():
    return jsonify(getJSONData(url_cryptocurrency))

@app.route("/globe/")
@cross_origin()
def globe():
    return jsonify(getJSONData(url_global_finance))

@app.route("/india/")
@cross_origin()
def india():
    return jsonify(getJSONData(url_indian_finance))

if __name__ == '__main__':
    app.run(debug=True)