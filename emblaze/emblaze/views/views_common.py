from emblaze import app

from emblaze.models import models_common 

from flask import Flask,render_template,redirect,url_for,flash, redirect, request, session, abort, jsonify, Response
from werkzeug import secure_filename
from flask import send_from_directory, send_file
import os
import datetime

app.secret_key = 'secretkeyhereplease'

# Rahul's
@app.route("/")
def home():
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file("uploads/"+str(filename))

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    flask("Error")