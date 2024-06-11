from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

img_width, img_height = 224, 224

loaded_combined_model = tf.keras.models.load_model("Model/combined_model.h5")

# Load an example image from the dataset
image_path = "Test/test1.jpg" 
test_image = image.load_img(image_path, target_size=(img_width, img_height))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)

# Preprocess the image
test_image = test_image / 255.0  # Normalize pixel values to [0, 1]

# Make predictions using the combined model
predictions = loaded_combined_model.predict(test_image)

# Interpret the predictions
scenery_prediction = predictions[0]  # Output for scenery
environment_prediction = predictions[1]  # Output for environment
category_prediction = predictions[2]  # Output for category

# Example: Print the predicted labels
print("Scenery Prediction:", scenery_prediction)
print("Environment Prediction:", environment_prediction)
print("Category Prediction:", category_prediction)

# Define the class labels for interpretation
scenery_classes = ['Nature', 'Urban']
environment_classes = ['Land', 'Water']
category_classes = ['Attraction', 'Greenery', 'Historical']

# Show the image
plt.imshow(test_image[0])
plt.axis('off')

# Add text annotations for predictions
scenery_label = scenery_classes[np.argmax(scenery_prediction)]
environment_label = environment_classes[np.argmax(environment_prediction)]
category_label = category_classes[np.argmax(category_prediction)]

plt.text(10, 30, f"Scenery Prediction: {scenery_label}", fontsize=12, color='white', backgroundcolor='black')
plt.text(10, 60, f"Environment Prediction: {environment_label}", fontsize=12, color='white', backgroundcolor='black')
plt.text(10, 90, f"Category Prediction: {category_label}", fontsize=12, color='white', backgroundcolor='black')

plt.show()
