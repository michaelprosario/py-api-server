import time

class AppResponse:
  def __init__(self):
    self.message = "ok"
    self.statusCode = 200

class AddDocumentCommand:
  def __init__(self, data, createdBy ):
    self.data = data
    self.createdBy = createdBy
    self.createdAt = time.time()

class DocumentRepository:
  def addDocument(self,command):
    response = AppResponse()
    return response

class DocumentServices:
  def __init__(self, documentRepository ):
    self.documentRepository = documentRepository

  def addDocument(self,command):
    response = self.documentRepository.addDocument(command)
    return response
