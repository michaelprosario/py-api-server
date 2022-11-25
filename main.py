from appCore.documentServices import AddDocumentCommand
from appCore.documentServices import AddDocumentCommandSchema
from appCore.documentServices import DocumentServices
from appCore.documentServices import GetDocumentQuery
from appCore.documentServices import GetDocumentsQuery
from appInfra.documentFileRepository import DocumentFileRepository
import uuid

from fastapi import FastAPI

def getService():
    repo = DocumentFileRepository("data")      
    service = DocumentServices(repo)
    return service


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server ok"}

@app.post("/add-document")
async def addDocument(command):
    service = getService()  
    response = service.addDocument(command)
    return response