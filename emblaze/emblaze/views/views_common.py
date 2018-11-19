from emblaze import app

from emblaze.models import models_common 

from flask import Flask,render_template,redirect,url_for,flash, redirect, request, session, abort, jsonify, Response
from werkzeug import secure_filename
from flask import send_from_directory
import os
import datetime

app.secret_key = 'secretkeyhereplease'

# Rahul's
@app.route("/")
def home():
    return render_template("index.html")

