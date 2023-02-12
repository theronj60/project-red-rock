import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import colorgram

app = Flask(__name__)

UPLOAD_FOLDER = './static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('show_colors', filename=filename))
        else:
            message = 'No file uploaded'
        return render_template('index.html', error=message)
    else:
        return render_template('index.html')


@app.route('/show-colors/<filename>')
def show_colors(filename):
    file_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    colors = colorgram.extract(file_location, 6)
    return render_template('basic_show.html', colors=colors)


if __name__ == '__main__':
    app.run(debug=True)
