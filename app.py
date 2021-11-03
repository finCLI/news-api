from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route("/bitcoin/")
# def bitcoin():
#     return render_template("./data/bitcoin.json")

if __name__ == '__main__':
    app.run(debug=True)