from flask import Flask
from flask import render_template

app = Flask(__name__)

# for basic color extraction, use colorgram
# for advance usage, graphs, set number of colors, matplotlib and pandas

@app.route("/")
def index():
    return render_template('index.html') 

@app.route("/about")
def about():
    return "<p>About</p>"
