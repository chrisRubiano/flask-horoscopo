from flask import Flask
from decouple import config
from flask_restx import Api

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version='1.0',
    title='Horoscope API',
    description='Get horoscope data easily using the below APIs',
    license='MIT',
    contact='Cristian Samaniego',
    contact_url='github.com/chrisrubiano',
    contact_email='chris.rubiano42@gmail.com',
    doc='/',
    prefix='/api/v1'
)

from core import routes
