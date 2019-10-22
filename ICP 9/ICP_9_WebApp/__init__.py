from flask import Flask
from ICP_9_WebApp.webApp import main
from ICP_9_WebApp.MachineLearning import machinelearning

app = Flask(__name__)

app.register_blueprint(webApp.main)
app.register_blueprint(machinelearning.machinelearning, url_prefix='/machinelearning')