from typing import Optional, List
import time
import datetime
from pydantic import BaseModel,ValidationError
import re

class AppResponse(BaseModel):
  message: str = 'ok'
  status: int = 200
  errors: dict = {}

class GetRecordResponse(BaseModel):
  message: str = 'ok'
  status: int = 200
  record: dict 

class GetRecordsResponse(BaseModel):
  message: str = 'ok'
  status: int = 200
  data: List[dict]

class AddDocumentCommand(BaseModel):
  createdAt: float = 0
  createdBy: str 
  data: dict
  id:str

class GetDocumentsQuery(BaseModel):
  keyword:str = ''
  userId:str 

class GetDocumentQuery(BaseModel):
  id: str
  userId: str

class DocumentRepository:
  def addDocument(self,command):
    response = AppResponse()
    return response

  def deleteDocument(self,id):
    response = AppResponse()
    return response

  def getDocuments(self,query):
    response = GetRecordsResponse(data=[])
    response.status = 200
    return response

  def getDocument(self,query):
    response = AppResponse()
    return response

  def recordExists(self,query):
    return false

class DocumentServices:
  def __init__(self, documentRepository ):
    self.documentRepository = documentRepository

  def isUUID(self,input):
    if input == None:
      return False

    guid_pattern = "^(?:\\{{0,1}(?:[0-9a-fA-F]){8}-(?:[0-9a-fA-F]){4}-(?:[0-9a-fA-F]){4}-(?:[0-9a-fA-F]){4}-(?:[0-9a-fA-F]){12}\\}{0,1})$"
    return re.match(guid_pattern, input) != None

  def makeAppResponse(self,message,statusCode, error):
      appResponse = AppResponse(message=message, statusCode=statusCode, error=error)
      appResponse.status = statusCode
      return appResponse

  def addDocument(self,command):
    if command == None:
      return self.makeAppResponse('command is none', 400, None)

    try:
      if not self.isUUID(command.id):
        return self.makeAppResponse('uuid not valid', 400, None)

      command.data['id'] = command.id
      response = self.documentRepository.addDocument(command)
      return response
    except ValidationError as e:
      errorResponse = self.makeAppResponse('validation error', 400, e)
      return errorResponse

  def deleteDocument(self,id):
    if id == None:
      return self.makeAppResponse('id is none', 400, None)

    if not self.isUUID(id):
      return self.makeAppResponse('id is bad', 400, None)

    response = self.documentRepository.deleteDocument(id)
    return response

  def getDocuments(self,query):
    if query == None:
      return self.makeAppResponse('query is none', 400, None)

    if query.userId == None:
      return self.makeAppResponse('query.userId should be defined', 400, None)

    response = self.documentRepository.getDocuments(query)
    return response

  def getDocument(self,query):
    if query == None:
      return self.makeAppResponse('query is none', 400, None)

    try:
      response = self.documentRepository.getDocument(query)
      return response
    except ValidationError as e:
      errorResponse = self.makeAppResponse('validation error', 400, e)
      return errorResponse

  def recordExists(self,query):
    if query == None:
      return self.makeAppResponse('query is none', 400, None)
    try:
      return self.documentRepository.recordExists(query)
    except ValidationError as e:
      errorResponse = self.makeAppResponse('validation error', 400, e)
      return errorResponse