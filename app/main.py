
from appCore.commands import StoreDocumentCommand
from appCore.documentServices import DocumentServices
from appCore.commands import GetDocumentQuery
from appCore.commands import GetDocumentsQuery
from appInfra.documentPgRepository import DocPgRepository
import uuid

from fastapi import FastAPI

def getService():
    repo = DocPgRepository()
    repo.setupAppDatabase()
    service = DocumentServices(repo)
    return service

service = getService()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server ok"}

@app.post("/store-document")
async def storeDocument(command: StoreDocumentCommand):      
    return service.storeDocument(command)

@app.post("/get-documents")
async def getDocuments(query: GetDocumentsQuery):
    return service.getDocuments(query)

@app.post("/get-document")
async def getDocument(query: GetDocumentQuery):
    return service.getDocument(query)

@app.post("/delete-document")
async def deleteDocument(query: GetDocumentQuery):
    return service.deleteDocument(query)
