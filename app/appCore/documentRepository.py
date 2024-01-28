import abc

class DocumentRepository(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def addDocument(self,command):
    return AppResponse()

  @abc.abstractmethod
  def updateDocument(self,command):
    return AppResponse()

  @abc.abstractmethod
  def deleteDocument(self,command):
    return AppResponse()

  @abc.abstractmethod
  def getDocuments(self,query):
    response = GetRecordsResponse(data=[])
    response.status = 200
    return response

  @abc.abstractmethod
  def getDocument(self,query):
    response = AppResponse()
    return response

  @abc.abstractmethod
  def recordExists(self,query):
    return false