from flask import Flask
from views import homepage,rent,predict

def configure_routes(app):
    app.add_url_rule('/', 'homepage', homepage)
    app.add_url_rule('/rent', 'rent', rent)
    app.add_url_rule('/predict', 'predict', predict,methods=[ "POST"])
    