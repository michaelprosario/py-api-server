import sys
sys.path.append('../appCore')

import json
from appCore.documentServices import AppResponse
from appCore.documentServices import GetRecordResponse
from os.path import exists

class DocumentInfraRepository:
  def __init__(self, dataFolder):
    self.dataFolder = dataFolder

  def addDocument(self,command):
    
    fileName = self.dataFolder + "/" + command.id + ".json"
    strData = json.dumps(command.data)

    with open(fileName, 'w') as f:
        f.write(strData)

    response = AppResponse()
    return response

  def deleteDocument(self,id):
    response = AppResponse()
    return response

  def getDocuments(self,query):
    response = AppResponse()
    return response

  def getDocument(self,query):
    fileName = self.dataFolder + "/" + query.id + ".json"
    fileHandle = open(fileName, "r")
    strContent = fileHandle.read()
    print(strContent)
    dictionary = json.loads(strContent)

    response = GetRecordResponse()
    response.data = dictionary

    return response

  def recordExists(self,query):
    fileName = self.dataFolder + "/" + query.id + ".json"
    file_exists = exists(fileName)
    return file_exists

