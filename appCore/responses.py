from pydantic import BaseModel,ValidationError
from typing import Optional, List

class AppResponse(BaseModel):
  message: str = 'ok'
  status: int = 200
  errors = []

class GetRecordResponse(BaseModel):
  message: str = 'ok'
  status: int = 200
  record: dict 

class GetRecordsResponse(BaseModel):
  message: str = 'ok'
  status: int = 200
  data: List[dict]