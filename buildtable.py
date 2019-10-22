import json


with open('usergroups.json') as json_file:
    data = json.load(json_file)
    values = data["values"]
    print("| Name | Description | Country | Twitter |")
    print("|------|-------------|---------|---------|")
    for c in values:
        print("| %s | %s | %s | %s |" % (c["name"],c["description"],c["geometry"]["country"],c["contact"]["twitter"]))

