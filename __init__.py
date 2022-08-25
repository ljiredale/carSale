from flask import *
import os


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/2016whitefordfusion")
def whitefordfusion():
    return render_template('2016whitefordfusion.html')

app.run(debug=True)