import os
import json
from flask import Flask, request, redirect, flash, url_for, render_template
from werkzeug.utils import secure_filename
import colorgram

app = Flask(__name__)

mode = os.environ.get('MODE')

# UPLOAD_FOLDER = './static/uploads/'
UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# need to check if dev env or production
if mode == 'PRODUCTION':
    with open('/etc/config.json') as config_file:
        config = json.load(config_file)
        app.config['SECRET_KEY'] = config.get('SECRET_KEY')
        app.secret_key = app.config['SECRET_KEY']
else:
    app.config['SECRET_KEY'] = 'the652Eete'

app.config['MAX_CONTENT_LENGTH'] = 3 * 1000 * 1000
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# for basic color extraction, use colorgram
# for advance usage, graphs, set number of colors, matplotlib and pandas

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files["file"]
        if file:
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('show_colors', filename=filename))
            else:
                flash('File type is not approved.')
                return redirect(url_for('index'))
        else:
            flash('No file uploaded')
            return redirect(url_for('index'))
    else:
        return render_template('index.html')


@app.route('/show-colors/<filename>')
def show_colors(filename):
    file_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    colors = colorgram.extract(file_location, 6)
    return render_template('basic_show.html', colors=colors, hex=rgb_to_hex)


if __name__ == '__main__':
    app.run(debug=True)
