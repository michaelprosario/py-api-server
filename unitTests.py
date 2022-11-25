import unittest
from appCore.documentServices import AddDocumentCommand
from appCore.documentServices import AddDocumentCommandSchema
from appCore.documentServices import DocumentServices
from appCore.documentServices import DocumentRepository
from appCore.documentServices import GetDocumentsQuery
import uuid

class DocumentServicesTests(unittest.TestCase):

    def test_DocumentServices__AddDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        id = '62ab14c7-9e57-4655-ac4d-777ba710c65f'

        data = {
            'title': "post title",
            'content': "content"
        }
        createdBy = 'test'
        command = AddDocumentCommand(data, createdBy, id)  

        repo = DocumentRepository()      
        service = DocumentServices(repo)
        
        # act
        response = service.addDocument(command)

        # assert
        self.assertTrue(response.statusCode == 200)

    def test_DocumentServices__AddDocument__FailIdNotValid(self):
        # arrange
        data = {
            'title': "post title",
            'content': "content"
        }
        createdBy = 'test'
        command = AddDocumentCommand(data, createdBy, 'id')  

        repo = DocumentRepository()      
        service = DocumentServices(repo)
        
        # act
        response = service.addDocument(command)

        # assert
        self.assertTrue(response.statusCode == 400)


    def test_DocumentServices__DeleteDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        id = "recordId"
        repo = DocumentRepository()      
        service = DocumentServices(repo)
        
        # act
        response = service.deleteDocument(id)

        # assert
        self.assertTrue(response.statusCode == 200)

    def test_DocumentServices__GetDocuments__ReturnValidResponseWithGoodInput(self):
        # arrange
        query = GetDocumentsQuery('system')

        repo = DocumentRepository()      
        service = DocumentServices(repo)
        
        # act
        response = service.getDocuments(query)

        # assert
        self.assertTrue(response.statusCode == 200)

    def test_AddValidator__ValidateAddDocumentCommand(self):
        # arrange
        id = '62ab14c7-9e57-4655-ac4d-777ba710c65f'
        userId = 'mrosario'
        data = { 'text': 'foo' }
        command = AddDocumentCommand(data, 'mrosario', id)

        # act
        response = AddDocumentCommandSchema().validate(command.__dict__)

        # assert
        self.assertTrue(response == {})

    def test_AddValidator__ValidateAddDocumentCommand__HandleBadUserId(self):
        # arrange
        id = '62ab14c7-9e57-4655-ac4d-777ba710c65f'
        userId = ''
        data = { 'text': 'foo' }
        command = AddDocumentCommand(data, userId, id)

        # act
        response = AddDocumentCommandSchema().validate(command.__dict__)
  
        # assert
        self.assertTrue(response['createdBy'] != None)

    def test_AddValidator__ValidateAddDocumentCommand__HandleBadId(self):
        # arrange
        id = ''
        userId = 'mrosario'
        data = { 'text': 'foo' }
        command = AddDocumentCommand(data, 'mrosario', id)

        # act
        response = AddDocumentCommandSchema().validate(command.__dict__)

        # assert
        self.assertTrue(response['id'] != None)


if __name__ == '__main__':
    unittest.main()