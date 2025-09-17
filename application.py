from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load model and data
try:
    model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
    print("Model loaded successfully. Type:", type(model))
except Exception as e:
    print("Error loading model:", e)
    model = None

car = pd.read_csv('Cleaned_Car_data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()

    companies.insert(0, 'Select company')
    return render_template('index.html',
                           companies=companies,
                           car_models=car_models,
                           years=years,
                           fuel_types=fuel_types)

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        company = request.form.get('company')
        car_model = request.form.get('car_models')
        year = int(request.form.get('year'))
        fuel_type = request.form.get('fuel_type')
        driven = int(request.form.get('kilo_driven'))

        # Input to DataFrame
        input_df = pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                data=[[car_model, company, year, driven, fuel_type]])

        prediction = model.predict(input_df)
        price = np.round(prediction[0], 2)

        return f"Estimated Car Price: ₹ {price} Lakh"

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
