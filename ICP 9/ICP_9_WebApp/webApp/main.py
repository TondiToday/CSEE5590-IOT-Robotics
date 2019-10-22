from pydub import AudioSegment
import os
# import magic
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template, Blueprint
from werkzeug.utils import secure_filename

main_page = Blueprint('main_page',__name__, template_folder='templates')

ALLOWED_EXTENSIONS = set(['wav', 'txt'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect('/machinelearning')
        else:
            flash('Allowed file types are txt, wav')
            return redirect(request.url)



