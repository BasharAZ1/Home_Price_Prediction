from flask import render_template, request, redirect,flash,session,url_for
import numpy as np
import pickle
import sklearn



model_components = {
    'rent': {'poly': None, 'lin': None, 'scaler': None},
    'buy': {'poly': None, 'lin': None, 'scaler': None}
}


def load_model_components(model_type):
    base_path = f"{model_type}_model/"
    with open(f'{base_path}poly_transformer_{model_type}.pkl', 'rb') as f:
        model_components[model_type]['poly'] = pickle.load(f)
    with open(f'{base_path}trained_model_{model_type}.pkl', 'rb') as f:
        model_components[model_type]['lin'] = pickle.load(f)
    with open(f'{base_path}scaler_{model_type}.pkl', 'rb') as f:
        model_components[model_type]['scaler'] = pickle.load(f)




def homepage():
    return render_template("index.html")


def rent():
    return render_template("listing_input.html", action="/predict", title="Enter Rent Details")

def buy():
    return render_template("listing_input.html", action="/predict_buy", title="Enter Buy Details")




def predict(model_type):
    load_model_components(model_type)

    baths = request.form.get('baths', type=int)
    area = request.form.get('area', type=float)
    city = request.form.get('city')
    bedrooms = request.form.get('bedrooms', type=int)

    city_map = {
        'Islamabad': [1, 0, 0, 0],
        'Karachi': [0, 1, 0, 0],
        'Rawalpindi': [0, 0, 1, 0],
        'Faisalabad': [0, 0, 0, 1]
    }
    
    if model_type == 'rent':
        city_features = city_map[city][:3]  # Only first three cities for rent
    else:
        city_features = city_map[city]      # All four cities for buy

    # Preprocess the data
    features = np.array([[bedrooms, baths, area] + city_features])
    features_scaled = model_components[model_type]['scaler'].transform(features)
    features_poly = model_components[model_type]['poly'].transform(features_scaled)

    # Predict
    prediction = model_components[model_type]['lin'].predict(features_poly)
    return render_template('result.html', prediction=round(prediction[0], 2))



