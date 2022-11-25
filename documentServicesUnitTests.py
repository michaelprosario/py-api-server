import unittest
from appCore.documentServices import AddDocumentCommand
from appCore.documentServices import DocumentServices
from appCore.documentServices import DocumentRepository


class DocumentServicesTests(unittest.TestCase):

    def test_DocumentServices__AddDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        data = {
            'title': "post title",
            'content': "content"
        }
        createdBy = 'test'
        command = AddDocumentCommand(data, createdBy)  

        repo = DocumentRepository()      
        service = DocumentServices(repo)
        
        # act
        response = service.addDocument(command)

        # assert
        self.assertTrue(response.statusCode == 200)

    def test_DocumentServices__DeleteDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        id = "recordId"
        repo = DocumentRepository()      
        service = DocumentServices(repo)
        
        # act
        response = service.deleteDocument(id)

        # assert
        self.assertTrue(response.statusCode == 200)


if __name__ == '__main__':
    unittest.main()