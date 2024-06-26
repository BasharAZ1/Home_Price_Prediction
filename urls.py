from flask import Flask
from views import homepage,rent,predict,buy

def configure_routes(app):
    app.add_url_rule('/', 'homepage', homepage)
    app.add_url_rule('/rent', 'rent', rent)
    app.add_url_rule('/buy', 'buy', buy)
    app.add_url_rule('/predict', 'predict', predict, methods=["POST"], defaults={'model_type': 'rent'})
    app.add_url_rule('/predict_buy', 'predict_buy', predict, methods=["POST"], defaults={'model_type': 'buy'})
    