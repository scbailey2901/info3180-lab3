from flask import Flask
from flask_mail import Mail
from config import Config


SECRET_KEY="648e7a5b4d86411ef59828dba6f08e20bb2801951aa20591b733e2e6deca9e51"

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
from app import views
