from flask import Flask
from WebApp.main_page import main_page
from MachineLearning.machinelearning import machinelearning
app = Flask(__name__)

app.run()
app.register_blueprint(main_page)
app.register_blueprint(machinelearning)
