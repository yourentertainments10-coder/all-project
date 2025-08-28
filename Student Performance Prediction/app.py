from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
MODEL_PATH = 'model.pkl'
model = None
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            int(request.form['age']),
            int(request.form['study_time']),
            int(request.form['failures']),
            int(request.form['absences']),
            int(request.form['G1']),
            int(request.form['G2']),
            int(request.form['G3'])
        ]
        features = np.array([features])
        prediction = model.predict(features)[0] if model else 0
        result = 'Pass' if prediction == 1 else 'Fail'
        return render_template('result.html', result=result)
    except Exception as e:
        return render_template('result.html', result=f'Error: {e}')

if __name__ == '__main__':
    app.run(debug=True)
