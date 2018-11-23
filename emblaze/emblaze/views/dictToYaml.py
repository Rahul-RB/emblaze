def dictToYaml(inpDict):
    opDict = {
        "name": {
            "first": inpDict["firstName"][0],
            "middle": "null",
            "last": inpDict["lastName"][0]
          },
          "about": inpDict["aboutMe"][0],
          "position": "Software Developer",
          "birth": {
            "year": inpDict["dateOfBirth"].year,
            "location": inpDict["placeOfBirth"][0]
          },
          "knowledge": inpDict["otherNotes"][0],

          "contact": {
            "email": inpDict["emailID"][0],
            "phone": inpDict["phoneNO"][0],
            "street": inpDict["street"][0],
            "city": inpDict["city"][0]+" "+inpDict["countries"][0],
            "website": inpDict["contactWebsite"][0],
            "github": inpDict["contactGithubLink"][0]
          },
          "lang": "en"
    }

    opDict["experience"]=[]
    opDict["education"]=[]
    opDict["skills"]=[]
    opDict["projects"]=[]
    opDict["hobbies"]=[]

    for name,pos,time,descr,site in zip(inpDict["expCompName"],inpDict["expCompPos"],inpDict["expCompTime"],inpDict["expCompDescr"],inpDict["expCompSite"]):
        opDict["experience"].append({
            "company": name,
            "position": pos,
            "timeperiod": time,
            "description": descr,
            "website": site
        })
    
    for degree,descr,time,site in zip(inpDict["eduDegree"],inpDict["eduDetails"],inpDict["eduTime"],inpDict["eduSite"]):
        opDict["education"].append({
            "degree": degree,
            "timeperiod": time,
            "description": descr,
            "website": site
        })    
    for name,level in zip(inpDict["skillName"],inpDict["skillVal"]):
        opDict["skills"].append({
            "name": name,
            "level": int(level)
        })
    
    for name,url,platform,descr in zip(inpDict["projName"],inpDict["projURL"],inpDict["projPlatform"],inpDict["projDescr"]):
        opDict["projects"].append({
            "name":name,
            "platform":platform,
            "description":descr,
            "url":url
        })

    for name,url in zip(inpDict["hobbyName"],inpDict["hobbyURL"]):
        opDict["hobbies"].append({
            "name": name,
            "iconClass": "fa fa-gamepad",
            "url": url
        })

    return opDict

# inpDict =  {
#             'contactStreet': ['Uttaralala'],
#             'projName': ['Proj1'],
#             'contactCity': ['Benga'],
#             'otherNotes': ["I've knowledge i gueess"],
#             'expCompTime': ['Jan 2015 - July 2016'],
#             'contactGithubLink': ['githu.bom'],
#             'hobbyName': ['Hobby1'],
#             'expCompDescr': [],
#             'street': ['B 1001, The Gulmohar Apartments,Ceasar Road,Beside Filmalaya Studio, Amboli, Andheri(West)'
#                        ],
#             'countries': ['India'],
#             'eduTime': ['Jan 2005 - July 2013'],
#             'contactWebsite': ['lvh.me'],
#             'pinCode': ['400058'],
#             'text': ['2018-05-18'],
#             'projDescr': ['Projec1'],
# --            'aboutMe': [],
#             'expCompName': ['Pull'],
#             'phoneNO': ["('415', '582', '7457')"],
#             'emailID': ['13herger@gmail.com'],
# --            'lastName': ['Herger'],
#             'eduDegree': ['Some degree'],
#             'city': ['Mumbai'],
#             'projURL': ['lvh.me'],
#             'expCompPos': ['developer'],
#             'hobbyURL': ['lvh.me'],
#             'placeOfBirth': ['Mumbai'],
#             'address': ['B 1001, The Gulmohar Apartments,Ceasar Road,Beside Filmalaya Studio, Amboli, Andheri(West)'
#                         ],
# --            'firstName': ['Brendan'],
#             'skillVal': [],
#             'eduDetails': ['Vrije Univesriteit'],
#             'skillName': [
#                 'python',
#                 'R',
#                 'C',
#                 'java',
#                 '.NET',
#                 'Mac',
#                 'sklearn',
#                 'SQL',
#                 'MySQL',
#                 ],
#             'dateOfBirth': [],
#             'projPlatform': ['github'],
#             'state': ['Maharashtra'],
#             'Message': ["I'm what I've become", 'Did some work'],
#     }
