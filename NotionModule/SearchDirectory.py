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