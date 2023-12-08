from flask import Flask, jsonify, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

app = Flask(__name__)

# Load the dataset from "idsdataset.csv" and clean up column names
dataset = pd.read_csv("idsdataset.csv")
dataset.columns = dataset.columns.str.strip()  # Remove leading and trailing spaces

# Assuming the target column is named "target" (adjust as per your data)
X_train = dataset.drop(columns=["target"])
y_train = dataset["target"]

# Train your Random Forest Classifier
clf1 = RandomForestClassifier()
clf1.fit(X_train, y_train)

# Save the trained classifier to a file
joblib.dump(clf1, "trained_classifier.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Create a DataFrame from the received data
        df = pd.DataFrame([data])

        # Perform the prediction using the trained classifier
        prediction = clf1.predict(df)

        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)