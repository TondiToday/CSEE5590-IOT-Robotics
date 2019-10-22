import os
from os import walk

import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from app import app
from flask import Flask, flash, request, redirect, render_template, Blueprint
from werkzeug.utils import secure_filename

machinelearning = Blueprint('machinelearning',__name__, template_folder='templates')
@machinelearning.route('/machinelearning')
def upload_machinelearning_form():
    flash('File successfully uploaded')
    return render_template('machinelearning.html')


#@app.route('/machinelearning', methods=['POST'])
