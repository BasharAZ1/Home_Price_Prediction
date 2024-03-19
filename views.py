from flask import render_template, request, redirect,flash,session,url_for
import numpy as np
import pickle
import sklearn



poly = None
lin = None
scaler = None

def load_model_components():
    global poly, lin, scaler
    with open('poly_transformer_rent.pkl', 'rb') as f:
        poly = pickle.load(f)
    with open('trained_model_rent.pkl', 'rb') as f:
        lin = pickle.load(f)
    with open('scaler_rent.pkl', 'rb') as f:
        scaler = pickle.load(f)



def homepage():
    return render_template("index.html")


def rent():
    return render_template("rent.html")




def predict():
    load_model_components()

    baths = request.form.get('baths', type=int)
    area = request.form.get('area', type=float)
    city = request.form.get('city')
    bedrooms = request.form.get('bedrooms', type=int)
    
    city_Islamabad = 0
    city_Karachi = 0
    city_Rawalpindi = 0

    # One-hot encode the city input
    if city == 'Islamabad':
        city_Islamabad = 1
    elif city == 'Karachi':
        city_Karachi = 1
    elif city == 'Rawalpindi':
        city_Rawalpindi = 1

    # Preprocess the data
    features = np.array([[bedrooms, baths, area, city_Islamabad, city_Karachi, city_Rawalpindi]])
    features_scaled = scaler.transform(features)
    features_poly = poly.transform(features_scaled)
    
    # Predict
    prediction = lin.predict(features_poly)
    
    return render_template('result.html', prediction=round(prediction[0], 2))