from flask import Flask
# from flask_uploads import UploadSet, configure_uploads
from config import Config

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
    
from emblaze.views import views_common