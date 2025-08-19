import os
import shutil
import random

# Define source and destination paths
dataset_path = r"C:\Users\HP\OneDrive\Desktop\Cat vs Dog CNN\PetImages"
train_path = r"C:\Users\HP\OneDrive\Desktop\Cat vs Dog CNN\PetImages\train"
val_path = r"C:\Users\HP\OneDrive\Desktop\Cat vs Dog CNN\PetImages\test"

# Define categories
categories = ["Cat", "Dog"]


split_ratio = 0.8  

# Create train and val directories
for category in categories:
    os.makedirs(os.path.join(train_path, category), exist_ok=True)
    os.makedirs(os.path.join(val_path, category), exist_ok=True)

    # Get all images in category folder
    images = os.listdir(os.path.join(dataset_path, category))
    random.shuffle(images)

    # Split data
    train_size = int(len(images) * split_ratio)
    train_images = images[:train_size]
    val_images = images[train_size:]

    # Move images to train and val folders
    for img in train_images:
        shutil.move(os.path.join(dataset_path, category, img), os.path.join(train_path, category, img))

    for img in val_images:
        shutil.move(os.path.join(dataset_path, category, img), os.path.join(val_path, category, img))

print("Dataset successfully split into train and validation sets!")