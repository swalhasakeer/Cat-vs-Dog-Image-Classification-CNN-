from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Load your trained model
model = load_model('cat_dog_cnn_model.h5')
class_names = ['Cat', 'Dog']  # Adjust if needed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    if not file:
        return "No file uploaded"

    # Read image in memory (no saving to disk)
    img = Image.open(BytesIO(file.read()))
    img = img.resize((150, 150))  # Match your model input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize if your model was trained this way

    prediction = model.predict(img_array)
    result = class_names[int(prediction[0][0] > 0.5)]  # Binary classification

    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
