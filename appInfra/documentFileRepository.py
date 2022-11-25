import sys
import os
sys.path.append('../appCore')

import json
from appCore.documentServices import AppResponse
from appCore.documentServices import GetRecordResponse
from appCore.documentServices import GetRecordsResponse
from appCore.documentServices import GetDocumentQuery
from os.path import exists

class DocumentFileRepository:
  def __init__(self, dataFolder):
    self.dataFolder = dataFolder
  
  def getFileName(self, id):
    fileName = self.dataFolder + "/" + id
    return fileName

  def addDocument(self,command):
    fileName = self.getFileName(command.id)
    strData = json.dumps(command.data)

    with open(fileName, 'w') as f:
        f.write(strData)

    response = AppResponse()
    return response

  def deleteDocument(self,query):
    if self.recordExists(query):
      fileName = self.getFileName(id)
      os.remove(fileName)
      response = AppResponse()
      return response

  def getDocuments(self,query):
    # make response object
    records = []

    # get list of files
    fileList = os.listdir(self.dataFolder)

    # iterate over list
    for file in fileList:
      query = GetDocumentQuery(userId="system", id=file)
      getResponse = self.getDocument(query)
      if getResponse.status == 200:
        records.append(getResponse.record)

    response = GetRecordsResponse(data=records, userId=query.userId)
    
    return response

  def getDocument(self,query):
    fileName = self.getFileName(query.id)
    fileHandle = open(fileName, "r")
    strContent = fileHandle.read()
    dictionary = json.loads(strContent)

    response = GetRecordResponse(record=dictionary, userId="system")
    
    fileHandle.close()

    return response

  def recordExists(self,query):
    fileName = self.getFileName(query.id)
    file_exists = exists(fileName)
    return file_exists

