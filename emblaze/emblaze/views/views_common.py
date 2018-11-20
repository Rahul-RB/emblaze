import subprocess
from emblaze import app

from emblaze.models import models_common 

from flask import Flask,render_template,redirect,url_for,flash, redirect, request, session, abort, jsonify, Response
from werkzeug import secure_filename
from flask import send_from_directory, send_file

from emblaze.ResumeParser.bin import main as parser
from emblaze import ResumeGenerator
rgPath = ResumeGenerator.__path__._path[0]
import os
import datetime
import time

app.secret_key = 'secretkeyhereplease'

# Rahul's
@app.route("/")
def home():
    return render_template("index.html")

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route('/uploads/<filename>')
def viewUploadedFile(filename):
    parser.main()
    # return
    # return send_file("ResumeParser/data/output/resume_summary.csv")
    # return send_file("ResumeParser/data/output/resume_summary.csv",
    #                  mimetype='text/csv',
    #                  attachment_filename='Outputs.csv',
    #                  as_attachment=True)
    # p = subprocess.Popen(["npm run dev"], cwd="../../../../Test-Resume-Generator/ResumeGenerator/")
    # p = subprocess.Popen(["npm run dev"], cwd=app.open_resource("ResumeGenerator/").name)
    p = subprocess.Popen(["npm", "run", "dev"], cwd=rgPath)
    time.sleep(10)
    return redirect("http://localhost:8080")

@app.route('/uploader', methods=['GET', 'POST'])
def uploadFile():
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
        if file and allowedFile(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], "resume.pdf"))
            return redirect(url_for('viewUploadedFile',
                                    filename=filename))
    flash("Error")