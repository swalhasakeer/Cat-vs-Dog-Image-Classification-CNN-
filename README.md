# 🐾 **Cat vs Dog Image Classification (CNN)**

This project is a Deep Learning model that classifies images of cats and dogs using a Convolutional Neural Network (CNN).
The model is trained on the Cats vs Dogs dataset and can predict whether a given image is a Cat 🐱 or Dog 🐶.

## 📌 Project Structure
```bash
├── sorting.ipynb       # Jupyter notebook for building & training the CNN model
├── split.py            # Script to split dataset into train/test sets
├── cat_dog_cnn_model.h5 # Saved trained CNN model
```
## 🚀 Features

- Splits the dataset into training & testing sets (split.py)

- Trains a CNN model for binary classification

- Saves the trained model as .h5

- Achieves accurate predictions for Cat vs Dog classification

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/swalhasakeer/Cat-vs-Dog-Image-Classification-CNN.git
cd Cat-vs-Dog-Image-Classification-CNN
```

### 2️⃣ Install Dependencies
```bash 
pip install -r requirements.txt
```

### 3️⃣ Prepare Dataset

- Download the Cats vs Dogs dataset (e.g., from Kaggle Dogs vs Cats
).
- https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset

- Update dataset path in split.py if needed.

- Run:
```bash
python split.py
```

- This will create train/ and test/ directories with Cat and Dog images.

### 4️⃣ Train the Model

- Open and run sorting.ipynb in Jupyter Notebook/Colab to train the CNN.

- The trained model will be saved as:

- cat_dog_cnn_model.h5

## 📊 Model Architecture

- Input size: 150x150x3

- Layers: Convolution → MaxPooling → Flatten → Dense

- Output: Binary classification (Cat or Dog)

## 🔮 Future Improvements

- Add data augmentation for better generalization

- Use transfer learning (e.g., VGG16, ResNet)

- Extend to multi-class animal classification
