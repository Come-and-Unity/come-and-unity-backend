from flask import Flask
from constants import APP_NAME
from api.landing import LandingPage

app = Flask(APP_NAME)
app.add_url_rule('/', view_func=LandingPage.get, methods=['GET'])
