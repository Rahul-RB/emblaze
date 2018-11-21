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
import pandas as pd
import ast

app.secret_key = 'secretkeyhereplease'

# Rahul's
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detailFiller")
def detailFiller():
    # return render_template("detailFiller.html")
    return render_template("detailFiller.html")

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route('/uploads/<filename>')
def viewUploadedFile(filename):
    parser.main()

    df = pd.read_csv(app.open_resource("ResumeParser/data/output/resume_summary.csv").name,delimiter=";")
    print("df['candidate_name'][0]:",df["candidate_name"][0])
    # return
    # return send_file("ResumeParser/data/output/resume_summary.csv")
    # return send_file("ResumeParser/data/output/resume_summary.csv",
    #                  mimetype='text/csv',
    #                  attachment_filename='Outputs.csv',
    #                  as_attachment=True)
    # p = subprocess.Popen(["npm", "run", "dev"], cwd=rgPath)
    # time.sleep(10)
    name = df["candidate_name"][0].split(" ")

    if(len(name)==3):
        firstName = name[0]+" "+name[1]
        lastName = name[2]
    
    elif(len(name)==2):
        firstName = name[0]
        lastName = name[1]
    
    elif(len(name)==1):
        firstName = name[0]
        lastName = ""
    print("df['programming'][0]:",df["programming"][0])
    print("df['languages'][0]:",df["languages"][0])
    print("df['platforms'][0]:",df["platforms"][0])
    print("df['experience'][0]:",df["experience"][0])
    print("df['database'][0]:",df["database"][0])
    print("df['open-source'][0]:",df["open-source"][0])
    print("df['hobbies'][0]:",df["hobbies"][0])
    print("df['machinelearning'][0]:",df["machinelearning"][0])
    print("df['universities'][0]:",df["universities"][0])

    try:
        skill           = list(ast.literal_eval(df["programming"][0]))
    except Exception as e:
        skill = list(df["programming"][0])    
        
    try:
        languages       = list(ast.literal_eval(df["languages"][0]))
    except Exception as e:
        languages = list(df["languages"][0])    
        
    try:
        platforms       = list(ast.literal_eval(df["platforms"][0]))
    except Exception as e:
        platforms = list(df["platforms"][0])    
        
    try:
        experience      = list(ast.literal_eval(df["experience"][0]))
    except Exception as e:
        experience = list(df["experience"][0])    
        
    try:
        database        = list(ast.literal_eval(df["database"][0]))
    except Exception as e:
        database = list(df["database"][0])    
        
    try:
        openSource      = list(ast.literal_eval(df["open-source"][0]))
    except Exception as e:
        openSource = list(["open-source"][0])    
        
    try:
        hobbies         = list(ast.literal_eval(df["hobbies"][0]))
    except Exception as e:
        hobbies = list(df["hobbies"][0])    
        
    try:
        machinelearning = list(ast.literal_eval(df["machinelearning"][0]))
    except Exception as e:
        machinelearning = list(df["machinelearning"][0])    
        
    try:
        universities    = list(ast.literal_eval(df["universities"][0]))
    except Exception as e:
        universities = list(df["universities"][0])    
        


    return render_template("detailFiller.html",
                            firstName=firstName,
                            lastName=lastName,
                            emailID=df["email"][0],
                            phoneNO=df["phone"][0],
                            skills=skill,
                            experience=experience,
                            universities=universities
                        )

@app.route('/uploader', methods=['GET', 'POST'])
def uploadPDF():
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