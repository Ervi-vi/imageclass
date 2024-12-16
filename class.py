!pip install tensorflow==2.12.0
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("/content/drive/MyDrive/dataset/converted_kerascatdog/keras_model.h5", compile=False)

# Load the labels
class_names = open("/content/drive/MyDrive/dataset/converted_kerascatdog/labels.txt", "r").readlines()

# Replace this with the path to your image
image = Image.open('/content/drive/MyDrive/cattest.jpeg').convert("RGB")

# resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Load the image into the array
data[0] = normalized_image_array

# Predicts the model
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Print prediction and confidence score
print("Class:", class_name[2:], end="")
print("Confidence Score:", confidence_score)