from pydantic import BaseModel,ValidationError
from typing import Optional, List

class AddDocumentCommand(BaseModel):
  collection: str
  userId: str
  name: str
  tags: str = ''
  data: dict
  id:str = ''

class StoreDocumentCommand(AddDocumentCommand):
  id:str

class GetDocumentsQuery(BaseModel):
  keyword:str = ''
  collection:str = ''
  userId:str 

class GetDocumentQuery(BaseModel):
  id: str
  userId: str