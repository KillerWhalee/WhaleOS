import os
import requests
import json

#Basic Variable to treat NotionAPI
rootPath = os.getcwd()
url = f"https://api.notion.com/v1/databases"

#Load Essential Variable from JSON
with open(f"{rootPath}/NotionModule/json/fileData.json", "r") as fileDataJSON:
    fileData = json.load(fileDataJSON)
    databasePath = fileData["DatabasePath"]

with open(f"{rootPath}/NotionModule/json/databaseMap.json", "r") as databaseMapJSON:
    databaseMap = json.load(databaseMapJSON)
    databaseId = databaseMap["문항 데이터"]

with open(f"{rootPath}/NotionModule/json/header.json") as headerJSON:
    header = json.load(headerJSON)

#Function Definition
def addData(folder, databaseId, header):
    for file in os.listdir(folder):
        fileName, fileExt = os.path.splitext(file)

        if not fileExt:
            addData(f"{folder}/{file}", databaseId, header)
            continue
        
        fileNameList = fileName.split("_")
        fileTheme = int(fileNameList[1])
        fileAuthor = fileNameList[2]
        fileDate = f"20{fileNameList[3][0:2]}-{fileNameList[3][2:4]}-{fileNameList[3][4:6]}"

        with open(f"{rootPath}/json/filePage.json") as filePage:
            payload = json.load(filePage)
            payload["parent"]["database_id"] = databaseId
            payload["properties"]["문항코드"]["title"][0]["text"]["content"] = fileName
            payload["properties"]["테마"]["number"] = fileTheme
            payload["properties"]["출제자"]["select"]["name"] = fileAuthor
            payload["properties"]["출제일"]["date"]["start"] = fileDate
            payload["properties"]["분류"]["select"]["name"] = "배치됨"
            payload["properties"]["현재 위치"]["rich_text"][0]["text"]["content"] = folder.split("/")[-1]

        request = requests.post(url, json = payload, headers = header)
        print(f"{request.status_code}:{fileName}")
    
    print(f"Wrote file in {folder.split('/')[-1]}")