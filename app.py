import os
import json
import pandas as pd

FOLDER_PATH = '<folder Path>'

def localDir(dir):
    createObjs=[]
    for path, subdirs, files in os.walk(dir):
        for name in files:
            createObj = {"Name" : name,"Path" : os.path.join(path, name)}
            createObjs.append(createObj)
    with open('data.json', 'w') as json_file:
        json.dump(createObjs, json_file)
    pd.read_json('data.json').to_csv('data.csv')
    pd.read_json('data.json').to_excel('data.xls')

        
if __name__ == '__main__':
    localDir(FOLDER_PATH)