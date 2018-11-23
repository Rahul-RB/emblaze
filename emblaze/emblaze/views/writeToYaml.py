import yaml
def writeToYaml(inpDict):
    print(inpDict)
    with open("test.yml", "w") as outfile:
        outfile.write("/* #*/ export const PERSON = `\n")
    with open("test.yml", "a") as outfile:
        yaml.dump(inpDict, outfile, default_flow_style=False)
        outfile.write("`")