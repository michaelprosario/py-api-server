from appCore.documentServices import AddDocumentCommand
from appCore.documentServices import DocumentServices
from appCore.documentServices import GetDocumentQuery
from appCore.documentServices import GetDocumentsQuery
from appInfra.documentFileRepository import DocumentFileRepository
from appInfra.documentSqlLiteRepository import DocSqlLiteRepository
import uuid

from fastapi import FastAPI

def getService():
    repo = DocSqlLiteRepository()
    repo.setupAppDatabase()
    service = DocumentServices(repo)
    return service

service = getService()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server ok"}

@app.post("/add-document")
async def addDocument(command: AddDocumentCommand):      
    response = service.addDocument(command)
    return response

@app.post("/get-documents")
async def getDocuments(query: GetDocumentsQuery):
    response = service.getDocuments(query)
    return response

@app.post("/get-document")
async def getDocument(query: GetDocumentQuery):
    response = service.getDocument(query)
    return response

@app.post("/delete-document")
async def deleteDocument(query: GetDocumentQuery):
    response = service.deleteDocument(query)
    return response