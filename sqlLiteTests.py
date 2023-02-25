from appCore.documentServices import AddDocumentCommand
from appCore.documentServices import DocumentServices
from appCore.documentServices import GetDocumentQuery
from appCore.documentServices import GetDocumentsQuery
from appInfra.documentFileRepository import DocumentFileRepository
from appInfra.documentSqlLiteRepository import DocSqlLiteRepository
import unittest
import uuid

class DocumentServicesTests(unittest.TestCase):
    def getService(self):
        repo = DocSqlLiteRepository()
        repo.setupMemoryDatabase()
        service = DocumentServices(repo)
        return service

    def makeAddCommand(self):
        data = {
            'title': "post title",
            'content': "content"
        }
        createdBy = 'test'
        id = str(uuid.uuid4())
        command = AddDocumentCommand(data=data, createdBy=createdBy, id=id)  
        command.collection = 'test'
        command.id = id
        command.name = 'doc1'
        return command

    def test_DocumentServices__AddDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        command = self.makeAddCommand()
        service = self.getService() 

        # act
        response = service.addDocument(command)

        # assert
        self.assertTrue(response.status == 200)

    def test_DocumentServices__GetDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        command = self.makeAddCommand()
        service = self.getService() 
        response = service.addDocument(command)

        # act
        query = GetDocumentQuery(
            id=command.id,
            userId = "system"
            )
        response = service.getDocument(query)

        # assert
        print(response)
        self.assertTrue(response.status == 200)

    def test_DocumentServices__RecordExists__ReturnValidResponseWithGoodInput(self):
        # arrange
        command = self.makeAddCommand()
        service = self.getService() 
        response = service.addDocument(command)

        # act
        query = GetDocumentQuery(
            id=command.id,
            userId = "system"
            )
        response = service.recordExists(query)

        # assert
        self.assertTrue(response)

if __name__ == '__main__':
    unittest.main()