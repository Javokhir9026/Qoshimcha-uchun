import os
import json
os.system("cls")

d = {
    "ismi" : "Behruz",
    "yoshi" : 16,
    "Guruh" : "Faundation XN2",
}
l = json.dumps(d, indent=3)


f = open("1_json.json","w+")
f.write(l)
f.close()