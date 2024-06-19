from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import requests
from io import BytesIO

img_width, img_height = 224, 224

scenery_model = tf.keras.models.load_model("Model20/sce_model.h5")
environment_model = tf.keras.models.load_model("Model20/env_model.h5")
category_model = tf.keras.models.load_model("Model20/cat_model.h5")

# Load image from url
image_url = "https://upload.wikimedia.org/wikipedia/commons/7/77/Stupa_Borobudur.jpg"
response = requests.get(image_url)
img = image.load_img(BytesIO(response.content), target_size=(img_width, img_height))

# Preprocess the image
test_image = image.img_to_array(img)
test_image = np.expand_dims(test_image, axis=0)
test_image = test_image / 255.0  # Normalize pixel values to [0, 1]

# Make predictions using each of the model
scenery_predict = scenery_model.predict(test_image)
environment_predict = environment_model.predict(test_image)
category_predict = category_model.predict(test_image)

# Example: Print the predicted labels
print("Scenery Prediction:", scenery_predict)
print("Environment Prediction:", environment_predict)
print("Category Prediction:", category_predict)

# Define the class labels for interpretation
scenery_classes = ['Nature', 'Urban']
environment_classes = ['Land', 'Water']
category_classes = ['Attraction', 'Greenery', 'Historical']

# Show the image
plt.imshow(test_image[0])
plt.axis('off')

# Add text annotations for predictions
scenery_label = scenery_classes[np.argmax(scenery_predict)]
environment_label = environment_classes[np.argmax(environment_predict)]
category_label = category_classes[np.argmax(category_predict)]

plt.text(10, 30, f"Scenery Prediction: {scenery_label}", fontsize=12, color='white', backgroundcolor='black')
plt.text(10, 60, f"Environment Prediction: {environment_label}", fontsize=12, color='white', backgroundcolor='black')
plt.text(10, 90, f"Category Prediction: {category_label}", fontsize=12, color='white', backgroundcolor='black')

plt.show()

# Print the labels as string
print("Scenery Prediction:", scenery_label)
print("Environment Prediction:", environment_label)
print("Category Prediction:", category_label)