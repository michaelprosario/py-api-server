from appCore.documentServices import AddDocumentCommand
from appCore.documentServices import DocumentServices
from appCore.documentServices import GetDocumentQuery
from appCore.documentServices import GetDocumentsQuery
from appInfra.documentFileRepository import DocumentFileRepository
import unittest
import uuid

class DocumentServicesTests(unittest.TestCase):
    def getService(self):
        repo = DocumentFileRepository("data")      
        service = DocumentServices(repo)
        return service


    def createNewDocument(self):
        data = {
            'title': "post title",
            'content': "content"
        }
        createdBy = 'test'
        id = str(uuid.uuid4())
        command = AddDocumentCommand(data=data, createdBy=createdBy, id=id)
        service = self.getService()  
        response = service.addDocument(command)
        return id

    def test_DocumentServices__AddDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        data = {
            'title': "post title",
            'content': "content"
        }
        createdBy = 'test'
        id = str(uuid.uuid4())
        command = AddDocumentCommand(data=data, createdBy=createdBy, id=id)  

        service = self.getService() 

        # act
        response = service.addDocument(command)

        # assert
        self.assertTrue(response.status == 200)

    def test_DocumentServices__GetDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        id = self.createNewDocument()
        
        # act
        userId = "mrosario"
        query = GetDocumentQuery(userId=userId, id=id)
        service = self.getService() 
        response = service.getDocument(query)

        # assert
        self.assertTrue(response.status == 200)

    def test_DocumentServices__GetDocuments__ReturnValidResponseWithGoodInput(self):
        # arrange
        id = self.createNewDocument()
        
        # act
        userId = "mrosario"
        query = GetDocumentsQuery(userId=userId)
        service = self.getService() 
        response = service.getDocuments(query)

        # assert
        self.assertTrue(response.status == 200)

    def test_DocumentServices__RecordExists__ReturnValidResponseWithGoodInput(self):
        # arrange
        id = self.createNewDocument()
        
        # act
        userId = "mrosario"
        query = GetDocumentQuery(userId=userId, id=id)
        service = self.getService() 
        response = service.recordExists(query)

        # assert
        self.assertTrue(response)

    def test_DocumentServices__RecordExists__ReturnValidResponseWithGoodInput(self):
        # arrange
        id = self.createNewDocument()
        
        # act
        userId = "mrosario"
        query = GetDocumentQuery(userId=userId, id=id)
        service = self.getService() 
        response = service.deleteDocument(id)
        recordExists = service.recordExists(query)

        # assert
        self.assertFalse(recordExists)


if __name__ == '__main__':
    unittest.main()