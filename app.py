from flask import Flask, flash, request, render_template

app = Flask(__name__)

# for basic color extraction, use colorgram
# for advance usage, graphs, set number of colors, matplotlib and pandas

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<p>About</p>'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        flash('No file part')
    return '<p>About</p>'
