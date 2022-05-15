import json
jsonfile = open('package.json')
jsondata = jsonfile.read()
obj = json.loads(jsondata)
print(obj['token'])