import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from appCore.documentServices import AddDocumentCommand
from appCore.documentServices import StoreDocumentCommand
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
        command = AddDocumentCommand(data=data, userId=createdBy, id=id, name='testDoc', collection='test')  
        command.collection = 'test'
        command.id = id
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

    def test_DocumentServices__GetAll__ReturnValidResponseWithGoodInput(self):
        # arrange
        command = self.makeAddCommand()
        service = self.getService() 
        response = service.addDocument(command)

        query = GetDocumentsQuery(userId="system")

        # act
        response = service.getDocuments(query)

        # assert
        self.assertTrue(response)        

    def test_DocumentServices__DeleteDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        command = self.makeAddCommand()
        service = self.getService() 
        response = service.addDocument(command)

        # act
        query = GetDocumentQuery(
            id=command.id,
            userId = "system"
            )
        response = service.deleteDocument(query)
        recordExists = service.recordExists(query)

        # assert
        self.assertFalse( recordExists )

    def test_DocumentServices__StoreDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        data = {
            'title': "post from store",
            'content': "content from store"
        }
        createdBy = 'test'
        id = str(uuid.uuid4())
        command = StoreDocumentCommand(data=data, userId=createdBy, id =id,name='testDoc', collection='test')  

        service = self.getService() 

        # act
        response = service.storeDocument(command)

        # assert
        self.assertTrue(response.status == 200)

    def test_DocumentServices__StoreDocument__TestUpdateFlow(self):
        # arrange
        data = {
            'title': "post from store",
            'content': "content from store"
        }
        createdBy = 'test'
        id = str(uuid.uuid4())
        command = StoreDocumentCommand(data=data, userId=createdBy, id=id, name='testDoc', collection='test')  

        service = self.getService() 

        # act
        response = service.storeDocument(command)

        # make record record exists
        getRecordQuery = GetDocumentQuery(userId="test", id=id)

        # get the record back from the db
        recordDoesExist = service.recordExists(getRecordQuery)
        self.assertTrue(recordDoesExist)

        # change it a bit
        record2 = service.getDocument(getRecordQuery)
        data2 = record2.record
        newValue="newValue"
        data2['content'] = newValue

        # store it again
        command2 = StoreDocumentCommand(data=data2, userId=createdBy, id=id, name='testDoc', collection='test')
        storeResponse2 = service.storeDocument(command2)

        # get the record again
        getDocumentResponse3 = service.getDocument(getRecordQuery)

        # see if the change worked
        self.assertTrue(getDocumentResponse3.record['content']==newValue)

        # assert
        self.assertTrue(response.status == 200)


if __name__ == '__main__':
    unittest.main()