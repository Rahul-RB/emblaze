from emblaze.ResumeGenerator import resume
rgPath = resume.__path__._path[0]

import yaml
def writeToYaml(inpDict):
    print(inpDict)
    with open(rgPath+"/data.yml", "w") as outfile:
        outfile.write("/* #*/ export const PERSON = `\n")
    with open(rgPath+"/data.yml", "a") as outfile:
        yaml.dump(inpDict, outfile, default_flow_style=False)
        outfile.write("`")