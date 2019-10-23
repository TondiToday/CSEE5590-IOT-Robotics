from flask import Flask, flash, render_template, Blueprint, session
from keras.applications.vgg19 import VGG19
from keras.preprocessing import image
from keras.applications.vgg19 import preprocess_input
from keras.models import Model
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# Variables
UPLOAD_FOLDER = 'C:/Users/tondi/OneDrive/Documents/GitHub/CSEE5590-IOT-Robotics/ICP 9/downloads'
machinelearning = Blueprint('machinelearning',__name__, template_folder='/templates')


# Model information
base_model = VGG19(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('flatten').output)


def get_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    flatten = model.predict(x)
    return list(flatten[0])


# plot waveforms


def plot_waveforms(file_name):
    audio = file_name[1]
    plt.plot(audio)
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.savefig("wavePlot/" + "test_sample.png")
    plt.close("all")
    with open(UPLOAD_FOLDER + "wavePlot/test_sample.png") as f:
        wave_form = f.read()
    return wave_form

# Flask


@machinelearning.route('/')
def upload_machinelearning_form():
    flash('File successfully uploaded and ready for machine learning')
    return render_template('machinelearning.html')


@machinelearning.route('/', methods=['POST'])
def run_machinelearning():
    filename = session.get('filename', None)

    with open(UPLOAD_FOLDER + "/" + filename) as f:
        file_content = f.read()
    X = []
    Y = []
    X.append(get_features(plot_waveforms(file_content)))
    Y.append(0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)
    clf = LinearSVC(random_state=0, tol=1e-5)
    clf.fit(X_train, y_train)
    predicted = clf.predict(X_test)
    # get the accuracy
    flash(accuracy_score(y_test, predicted))
    return render_template('machinelearning.html')
