from flask import Flask

UPLOAD_FOLDER = r'C:\Users\tondi\OneDrive\Documents\GitHub\CSEE5590-IOT-Robotics\ICP 9\downloads'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024
