import tensorflow as tf
from flask import Flask, request, jsonify
import numpy as np

# Load the model (ensure the file path is correct)
model = tf.keras.models.load_model("final_model.keras")  # Update this with the actual model path

# Initialize the Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # Get the input data (assuming it's JSON format with a 'data' field)
    data = request.json.get("data", [])
    
    # Check if input data is provided
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    
    # Preprocess data if necessary (e.g., reshape it into the correct input format for the model)
    # Example: Convert to numpy array or reshape as needed
    try:
        input_data = np.array(data)  # Modify based on actual model input requirements
    except Exception as e:
        return jsonify({"error": f"Error processing input data: {str(e)}"}), 400
    
    # Make predictions using the model
    try:
        predictions = model.predict(input_data)
    except Exception as e:
        return jsonify({"error": f"Error making predictions: {str(e)}"}), 500

    # Post-process predictions if necessary
    response = {
        "predictions": predictions.tolist()  # Convert predictions to list for JSON serialization
    }

    return jsonify(response)

if __name__ == "__main__":
    # You can set the host and port as required, e.g., host="0.0.0.0" to allow external access
    app.run(debug=True, host="0.0.0.0", port=5000)
