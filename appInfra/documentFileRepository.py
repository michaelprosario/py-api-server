import sys
import os
sys.path.append('../appCore')

import json
from appCore.documentServices import AppResponse
from appCore.documentServices import GetRecordResponse
from appCore.documentServices import GetDocumentQuery
from os.path import exists

class DocumentFileRepository:
  def __init__(self, dataFolder):
    self.dataFolder = dataFolder
  
  def getFileName(self, id):
    fileName = self.dataFolder + "/" + id + ".json"
    return fileName

  def addDocument(self,command):
    fileName = self.getFileName(command.id)
    strData = json.dumps(command.data)

    with open(fileName, 'w') as f:
        f.write(strData)

    response = AppResponse()
    return response

  def deleteDocument(self,id):
    query = GetDocumentQuery("system", id)

    if self.recordExists(query):
      fileName = self.getFileName(id)
      os.remove(fileName)
      response = AppResponse()
      return response

  def getDocuments(self,query):
    response = AppResponse()
    return response

  def getDocument(self,query):
    fileName = self.getFileName(query.id)
    fileHandle = open(fileName, "r")
    strContent = fileHandle.read()
    dictionary = json.loads(strContent)

    response = GetRecordResponse()
    response.data = dictionary
    fileHandle.close()

    return response

  def recordExists(self,query):
    fileName = self.getFileName(query.id)
    file_exists = exists(fileName)
    return file_exists

