from flask import Flask
# from flask_uploads import UploadSet, configure_uploads
from flaskext.mysql import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

mysql = MySQL()
mysql.init_app(app)
    
from emblaze.views import views_common