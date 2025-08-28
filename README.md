# Crop Health System

A web application for crop disease detection using deep learning.  
Upload an image of a crop leaf and get a prediction of its health status.

## Features

- **Image Upload:** Users can upload crop leaf images via the web interface.
- **Disease Prediction:** The app uses a trained MobileNetV2 model to classify crop diseases.
- **Confidence Score:** Each prediction includes a confidence percentage.

## Project Structure

- `app.py` — Flask web application for prediction.
- `split_dataset.py` — Script to split the PlantVillage dataset into training and validation sets.
- `train_crop_model.ipynb` — Jupyter notebook to train the deep learning model.
- `static/uploads/` — Folder for uploaded images.
- `model/crop_model.h5` — Trained model file .
- `dataset/` — Training and validation image folders.

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Srijaanaa/crop-health-detection-system.git
   cd crop-health-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the dataset**
   - Download the PlantVillage dataset (or your own crop images).
   - Place the images in the `PlantVillage/` folder.
   - Run the split script:
     ```bash
     python split_dataset.py
     ```
   - This will create `dataset/train` and `dataset/val` folders.

4. **Train the model**
   - Open and run `train_crop_model.ipynb` in Jupyter Notebook.
   - This will save the trained model as `model/crop_model.h5`.

5. **Run the web app**
   ```bash
   python app.py
   ```
   - Visit `http://127.0.0.1:5000` in your browser.

## Usage

- On the homepage, upload a crop leaf image.
- The app will display the predicted disease class and confidence score.


## License

This project is licensed under the MIT License.

## Acknowledgements

- [PlantVillage Dataset](https://plantvillage.psu.edu/)
- [TensorFlow](https://www.tensorflow.org/)
- [Flask](https://flask.palletsprojects.com/)
