from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

model = load_model('model/crop_model.h5')
class_names = sorted(os.listdir('dataset/train'))  # make sure this matches your class folders

def prepare_image(img_path):
    img = load_img(img_path, target_size=(224, 224))
    img = img_to_array(img) / 255.0
    return np.expand_dims(img, axis=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    img = prepare_image(filepath)
    pred = model.predict(img)[0]
    predicted_class = class_names[np.argmax(pred)]
    confidence = round(np.max(pred) * 100, 2)

    return render_template('result.html',
                           image=filepath,
                           label=predicted_class,
                           confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)
