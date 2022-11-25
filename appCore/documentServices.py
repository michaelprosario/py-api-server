import time
from marshmallow import Schema, fields, validate
import re

class AppResponse:
  def __init__(self):
    self.message = "ok"
    self.statusCode = 200
    self.errors = {}

class GetRecordResponse:
  def __init__(self):
    self.message = "ok"
    self.statusCode = 200
    self.data = {}

class GetRecordsResponse:
  def __init__(self):
    self.message = "ok"
    self.statusCode = 200
    self.data = []

class AddDocumentCommand:
  def __init__(self, data, createdBy,id ):
    self.createdAt = time.time()
    self.createdBy = createdBy
    self.data = data
    self.id = id

class AddDocumentCommandSchema(Schema):
  createdAt = fields.Number(Required=True)
  createdBy = fields.Str(validate=validate.Length(min=1))
  id = fields.Str(validate=validate.Length(min=36))
  data = fields.Dict(Required=True)

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

class GetDocumentsQuery:
  def __init__(self, userId):
    self.keyword = ""
    self.createdBy = userId

class GetDocumentQuery:
  def __init__(self, userId, id):
    self.id = id
    self.createdBy = userId

class DocumentRepository:
  def addDocument(self,command):
    response = AppResponse()
    return response

  def deleteDocument(self,id):
    response = AppResponse()
    return response

  def getDocuments(self,query):
    response = GetRecordsResponse()
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

  def makeAppResponse(self,message,statusCode):
      appResponse = AppResponse()
      appResponse.message = "validation error"
      appResponse.statusCode = 400
      return appResponse

  def addDocument(self,command):
    if command == None:
      return self.makeAppResponse('command is none', 400)

    validationResponse = AddDocumentCommandSchema().validate(command.__dict__)
    if validationResponse != {}:
      errorResponse = self.makeAppResponse('validation error', 400)
      errorResponse.errors = validationResponse
      return errorResponse

    if not self.isUUID(command.id):
      return self.makeAppResponse('uuid not valid', 400)

    command.data['id'] = command.id
    response = self.documentRepository.addDocument(command)
    return response

  def deleteDocument(self,id):
    response = self.documentRepository.deleteDocument(id)
    return response

  def getDocuments(self,query):
    response = self.documentRepository.getDocuments(query)
    return response

  def getDocument(self,query):
    response = self.documentRepository.getDocument(query)
    return response

  def recordExists(self,query):
    return self.documentRepository.recordExists(query)
