import os
from flask import Flask, flash, request, redirect, render_template, Blueprint, session
from werkzeug.utils import secure_filename


# Variables

app = Flask(__name__)
main_page = Blueprint('main_page',__name__, template_folder='/templates')
UPLOAD_FOLDER = 'C:/Users/tondi/OneDrive/Documents/GitHub/CSEE5590-IOT-Robotics/ICP 9/downloads'
ALLOWED_EXTENSIONS = set(['txt', 'wav'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'secret key'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Flask


@main_page.route('/')
def upload_form():
    return render_template('upload.html')


@main_page.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            session['filename'] = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect('/machinelearning')
        else:
            flash('Allowed file types are txt, wav')
            return redirect(request.url)



