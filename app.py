from flask import Flask, render_template, request, jsonify, redirect
from src.main import (url_bitcoin, 
url_ethereum,
url_cryptocurrency,
url_global_finance,
url_indian_finance,
getJSONData
)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/bitcoin/")
def bitcoin():
    return jsonify(getJSONData(url_bitcoin))

@app.route("/ethereum/")
def ethereum():
    return jsonify(getJSONData(url_ethereum))

@app.route("/cryptocurrency/")
def cryptocurrency():
    return jsonify(getJSONData(url_cryptocurrency))

@app.route("/globe/")
def globe():
    return jsonify(getJSONData(url_global_finance))

@app.route("/india/")
def india():
    return jsonify(getJSONData(url_indian_finance))

if __name__ == '__main__':
    app.run(debug=True)