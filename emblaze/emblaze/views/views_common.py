import subprocess
from emblaze import app

from emblaze.models import models_common 
from emblaze.views import dictToYaml
from emblaze.views import writeToYaml

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

nameList = [
    "firstName",
    "lastName",
    "emailID",
    "phoneNO",
    "address",
    "street",
    "city",
    "pinCode",
    "state",
    "countries",
    "dateOfBirth",
    "placeOfBirth",
    "Message",
    "aboutMe",
    "expCompName",
    "expCompPos",
    "expCompTime",
    "expCompSite",
    "Message",
    "expCompDescr",
    "eduDegree",
    "eduDetails",
    "eduSite",
    "eduTime",
    "skillName",
    "skillVal",
    "otherNotes",
    "projName",
    "projURL",
    "projPlatform",
    "projDescr",
    "hobbyName",
    "hobbyURL",
    "contactStreet",
    "contactCity",
    "contactWebsite",
    "contactGithubLink"
]

@app.route("/detailsToYaml",methods=["GET","POST"])
def detailsToYaml():
    if(request.method == "POST"):
        nameValueList = {}
        for name in nameList:
            if(name=="dateOfBirth"):
                nameValueList[name] = datetime.datetime.strptime(request.form.getlist(name)[0], "%Y-%m-%d")
                continue
            nameValueList[name] = request.form.getlist(name)
        print(nameValueList)
        res = dictToYaml.dictToYaml(nameValueList)
        writeToYaml.writeToYaml(res)
    return redirect("http://localhost:8080/")


def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route('/<filename>')
def viewUploadedFile(filename):
    parser.main()

    df = pd.read_csv(app.open_resource("ResumeParser/data/output/resume_summary.csv").name,delimiter=";")
    print("df['candidate_name'][0]:",df["candidate_name"][0])

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
        programming     = list(ast.literal_eval(df["programming"][0]))
    except Exception as e:
        programming = list(df["programming"][0])    
        
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
    
    if(programming == ['s', 'e', 't', '(', ')']):
        programming = [""]
    if(languages == ['s', 'e', 't', '(', ')']):
        languages = [""]
    if(platforms == ['s', 'e', 't', '(', ')']):
        platforms = [""]
    if(experience == ['s', 'e', 't', '(', ')']):
        experience = [""]
    if(database == ['s', 'e', 't', '(', ')']):
        database = [""]
    if(openSource == ['s', 'e', 't', '(', ')']):
        openSource = [""]
    if(hobbies == ['s', 'e', 't', '(', ')']):
        hobbies = [""]
    if(machinelearning == ['s', 'e', 't', '(', ')']):
        machinelearning = [""]
    if(universities == ['s', 'e', 't', '(', ')']):
        universities = [""]
    print("programming:",programming)
    print("languages:",languages)
    print("platforms:",platforms)
    print("experience:",experience)
    print("database:",database)
    print("openSource:",openSource)
    print("hobbies:",hobbies)
    print("machinelearning:",machinelearning)
    print("universities:",universities)
    skill = programming + platforms + machinelearning + database

    return render_template("detailFiller.html",
                            firstName=firstName,
                            lastName=lastName,
                            emailID=df["email"][0],
                            phoneNO=df["phone"][0],
                            experience=experience,
                            universities=universities,
                            skills=skill,
                            hobbies=hobbies,
                            openSource=openSource,
                            text = df["text"][0]
                        )

@app.route('/uploadPDF', methods=['GET', 'POST'])
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
            file.save(os.path.join(app.config["UPLOAD_PDF_FOLDER"], "resume.pdf"))
            return redirect(url_for('viewUploadedFile',
                                    filename=filename))
    flash("Error")

@app.route('/uploadImage', methods=['GET', 'POST'])
def uploadImage():
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
            file.save(os.path.join(app.config["UPLOAD_IMAGE_FOLDER"], "id.jpg"))
            return redirect(url_for("home"))
    flash("Error")

@app.route("/getAboutContents",methods=["GET"])
def getAboutContents():
    # <div class='bg-img bg-half overlay' style='background-image:url({{url_for(' static ',filename='img/about4.jpg ')}})'></div>\
    res = "\
    <div class='section md-section bg-grey'>\
        <div class='bg-img bg-half overlay' id='back1'></div>\
            <div class='container'>\
                <div class='row'>\
                    <div class='col-md-offset-7 col-md-6'>\
                        <h2 class='title'>About Us</h2>\
                        <p class='lead'>We are the class leader in making a resume shine its way through</p>\
                        <p>In this highly competitive world where getting your resume to from the reception to the recruiters hands are highly tough, the last thing you want is your resume to be like a notepad document. Use our tool and make a fancy one!</p>\
                    </div>\
                </div>\
            </div>\
    </div>\
    "
    res = {
        "content":res
    }
    return jsonify(res)

@app.route("/getClientContents",methods=["GET"])
def getClientContents():
    # <div class='bg-img bg-half overlay' style='background-image:url({{url_for(' static ',filename='img/about4.jpg ')}})'></div>\
    res ="\
            <div class='bg-img overlay' id='back2')></div>\
            <div id='testimonial' class='section sm-section'>\
                <div class='container'>\
                    <div class='row'>\
                        <div class='section-header text-center'>\
                            <h2 class='title'>Happy Clients</h2>\
                        </div>\
                        <div class='col-md-8 col-md-offset-2'>\
                                <div class='testimonial'>\
                                    <div class='testimonial-quote'>\
                                        <p>My resume just sailed through.</p>\
                                    </div>\
                                    <div class='testimonial-meta'>\
                                        <h3>Jon Snow</h3>\
                                        <span>Ally House Stark</span>\
                                    </div>\
                                </div>\
                                <div class='testimonial'>\
                                    <div class='testimonial-quote'>\
                                        <p>Tony stark hired me after seeing my resume</p>\
                                    </div>\
                                    <div class='testimonial-meta'>\
                                        <h3>Tom Holland</h3>\
                                        <span>Spiderman</span>\
                                    </div>\
                                </div>\
                                <div class='testimonial'>\
                                    <div class='testimonial-quote'>\
                                        <p>Marvel rejected me after seeing my resume, I am coming Marvel</p>\
                                    </div>\
                                    <div class='testimonial-meta'>\
                                        <h3>Thanos</h3>\
                                        <span>CEO Mr-Snaps-My-Finger</span>\
                                    </div>\
                                </div>\
                        </div>\
                    </div>\
                </div>\
            </div>\
        "    

    res = {
        "content":res
    }
    return jsonify(res)


@app.route("/getInfo")
def getInfo():
    infoType = request.args.get("infoType","",type=str)
    search = request.args.get("search","",type=str)
    res = models_common.getInfo(infoType,search)

    return jsonify(res)