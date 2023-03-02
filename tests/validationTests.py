import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from appCore.documentServices import AddDocumentCommand
from appCore.documentServices import DocumentRepository
from appCore.documentServices import DocumentServices
from appCore.documentServices import GetDocumentsQuery
from appCore.validators import StoreDocumentCommandValidator
import typing
import unittest
import uuid


class DocumentServicesTests(unittest.TestCase):

    def makePerfectCommand(self):
        id = '62ab14c7-9e57-4655-ac4d-777ba710c65f'
        
        data = {
            'title': "post title",
            'content': "content"
        }
        
        createdBy = 'test'
        command = AddDocumentCommand(data=data, userId=createdBy, id=id, collection="c1", name="name1")  

        return command

    def test_StoreDocumentCommandValidator__GivenGoodInputReturnNoErrors(self):
        # arrange
        command = self.makePerfectCommand()
        validator = StoreDocumentCommandValidator()
        results = validator.validate(command)

        self.assertTrue(len(results) == 0)

    def test_StoreDocumentCommandValidator__GivenNoCollectionReturnError(self):
        # arrange
        command = self.makePerfectCommand()
        command.collection = ''

        validator = StoreDocumentCommandValidator()
        results = validator.validate(command)

        self.assertTrue(len(results) == 1)

    def test_StoreDocumentCommandValidator__GivenNoNameReturnError(self):
        # arrange
        command = self.makePerfectCommand()
        command.name = ''

        validator = StoreDocumentCommandValidator()
        results = validator.validate(command)

        self.assertTrue(len(results) == 1)

    def test_StoreDocumentCommandValidator__GivenNoUserIdReturnError(self):
        # arrange
        command = self.makePerfectCommand()
        command.userId = ''

        validator = StoreDocumentCommandValidator()
        results = validator.validate(command)

        self.assertTrue(len(results) == 1)

if __name__ == '__main__':
    unittest.main()