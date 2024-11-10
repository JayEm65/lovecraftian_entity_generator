import tensorflow as tf
from flask import Flask, request, jsonify

# Load the model (make sure the file path is correct)
model = tf.keras.models.load_model("final_model.keras")  # Ensure this points to your actual model file

# Initialize the Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # Assume the input data is in JSON and includes a 'data' field with the input for the model
    data = request.json.get("data", [])
    
    # Check if input data is provided
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    
    # Preprocess data if necessary (ensure it's in the shape expected by the model)
    # Example: Convert to numpy array or reshape as needed
    # input_data = preprocess_data(data)

    # Make prediction
    predictions = model.predict([data])  # Ensure data format matches model input requirements

    # Post-process predictions if needed
    # Example: Convert predictions to a list
    response = {
        "predictions": predictions.tolist()  # Convert to list for JSON serialization
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
