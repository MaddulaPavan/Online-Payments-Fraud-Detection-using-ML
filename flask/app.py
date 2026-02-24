from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model and label encoder
model_path = os.path.join(os.path.dirname(__file__), 'payments.pkl')
le_path = os.path.join(os.path.dirname(__file__), 'label_encoder.pkl')

model = pickle.load(open(model_path, 'rb'))
le = pickle.load(open(le_path, 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_page')
def predict_page():
    return render_template('predict.html')

@app.route('/submit', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get data from form
        step = int(request.form['step'])
        type_str = request.form['type']
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])
        oldbalanceDest = float(request.form['oldbalanceDest'])
        newbalanceDest = float(request.form['newbalanceDest'])
        
        # Transform categorical 'type'
        try:
            type_encoded = le.transform([type_str])[0]
        except:
            # Fallback if type not in training
            type_encoded = 0
            
        features = np.array([[step, type_encoded, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]])
        
        prediction = model.predict(features)
        
        result = "Fraudulent" if prediction[0] == 1 else "Legit"
        
        return render_template('submit.html', prediction_text=f'This transaction is predicted to be: {result}')

if __name__ == "__main__":
    app.run(debug=True)
