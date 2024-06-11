import tensorflow as tf

# Load the Keras model
model = tf.keras.models.load_model('Model/combined_model.h5')

# Print model summary to identify potential issues
model.summary()

# Create a TFLiteConverter object
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Enable optimizations (optional)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Use only supported TensorFlow Lite operations
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,  # TensorFlow Lite builtin operations
    tf.lite.OpsSet.SELECT_TF_OPS     # TensorFlow operations
]

# Enable experimental new converter if needed
converter.experimental_new_converter = True

# Convert the model
try:
    tflite_model = converter.convert()
    # Save the converted model
    with open("Model/combined_model.tflite", "wb") as f:
        f.write(tflite_model)
    print("Model conversion successful.")
except Exception as e:
    print("Error during model conversion:", str(e))
