from appCore.documentServices import AddDocumentCommand
from appCore.documentServices import DocumentServices
from appCore.documentServices import GetDocumentQuery
from appCore.documentServices import GetDocumentsQuery
from appInfra.documentInfraRepository import DocumentInfraRepository
import unittest
import uuid

class DocumentServicesTests(unittest.TestCase):
    def getService(self):
        repo = DocumentInfraRepository("data")      
        service = DocumentServices(repo)
        return service


    def createNewDocument(self):
        data = {
            'title': "post title",
            'content': "content"
        }
        createdBy = 'test'
        id = str(uuid.uuid4())
        command = AddDocumentCommand(data, createdBy, id)
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
        command = AddDocumentCommand(data, createdBy, id)  

        service = self.getService() 

        # act
        response = service.addDocument(command)

        # assert
        self.assertTrue(response.statusCode == 200)

    def test_DocumentServices__GetDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        id = self.createNewDocument()
        
        # act
        userId = "mrosario"
        query = GetDocumentQuery(userId, id)
        service = self.getService() 
        response = service.getDocument(query)

        # assert
        self.assertTrue(response.statusCode == 200)

    def test_DocumentServices__RecordExists__ReturnValidResponseWithGoodInput(self):
        # arrange
        id = self.createNewDocument()
        
        # act
        userId = "mrosario"
        query = GetDocumentQuery(userId, id)
        service = self.getService() 
        response = service.recordExists(query)

        # assert
        self.assertTrue(response)

    def test_DocumentServices__RecordExists__ReturnValidResponseWithGoodInput(self):
        # arrange
        id = self.createNewDocument()
        
        # act
        userId = "mrosario"
        query = GetDocumentQuery(userId, id)
        service = self.getService() 
        response = service.deleteDocument(id)
        recordExists = service.recordExists(query)

        # assert
        self.assertFalse(recordExists)

    # def test_DocumentServices__DeleteDocument__ReturnValidResponseWithGoodInput(self):
    #     # arrange
    #     id = "recordId"
    #     repo = DocumentRepository()      
    #     service = DocumentServices(repo)
        
    #     # act
    #     response = service.deleteDocument(id)

    #     # assert
    #     self.assertTrue(response.statusCode == 200)

    # def test_DocumentServices__GetDocuments__ReturnValidResponseWithGoodInput(self):
    #     # arrange
    #     query = GetDocumentsQuery('system')

    #     repo = DocumentRepository()      
    #     service = DocumentServices(repo)
        
    #     # act
    #     response = service.getDocuments(query)

    #     # assert
    #     self.assertTrue(response.statusCode == 200)


if __name__ == '__main__':
    unittest.main()