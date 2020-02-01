from flask import Flask, flash, redirect, render_template, request
from random import randint
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def process():
    rgbval = request.form.get("rgbval")
    hexval = request.form.get("hexval")
    return render_template("home.html", rgb=rgbval, hex=hexval)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)