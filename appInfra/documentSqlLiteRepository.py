from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from typing import List
from typing import Optional
import json
import sys
import os
sys.path.append('../appCore')
from appCore.documentServices import AppResponse
from appCore.documentServices import GetRecordResponse
from appCore.documentServices import GetRecordsResponse
from appCore.documentServices import GetDocumentQuery

class Base(DeclarativeBase):
    pass

class Doc(Base):
    __tablename__ = "doc"

    id: Mapped[str] = mapped_column(primary_key=True)
    collection: Mapped[str] = mapped_column(String(1024))
    content: Mapped[str] = mapped_column(String(1024))
    name: Mapped[str] = mapped_column(String(1024))
    tags: Mapped[str] = mapped_column(String(1024))
    created_by: Mapped[str] = mapped_column(String(1024))
    updated_by: Mapped[str] = mapped_column(String(1024))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)

class DocSqlLiteRepository():
    def setupMemoryDatabase(self):
        self.engine = create_engine("sqlite://", echo=True)
        Base.metadata.create_all(self.engine)
    
    def addDocument(self,command):
        strData = json.dumps(command.data)

        with Session(self.engine) as session:
            record = Doc(id=command.id,collection=command.collection,content=strData,name=command.name,tags = '',created_by='system',updated_by='system', created_at=0, updated_at=0)
            session.add_all([record])
            session.commit()

        response = AppResponse()
        return response

    def deleteDocument(self,query):
        if self.recordExists(query):
            with Session(engine) as session:
                stmt = select(Doc).where(Doc.id == query.id)
        
        response = AppResponse()
        return response

    # def getDocuments(self,query):
    # # make response object
    # records = []

    # # get list of files
    # fileList = os.listdir(self.dataFolder)

    # # iterate over list
    # for file in fileList:
    # query = GetDocumentQuery(userId="system", id=file)
    # getResponse = self.getDocument(query)
    # if getResponse.status == 200:
    # records.append(getResponse.record)

    # response = GetRecordsResponse(data=records, userId=query.userId)

    # return response

    def getDocument(self,query):
        with Session(self.engine) as session:
            record = session.get(Doc, query.id)
            dictionary = json.loads(record.content)
            response = GetRecordResponse(record=dictionary, userId="system")
        return response

    def recordExists(self,query):
        if query == None:
            raise Exception("Query is not defined")

        with Session(engine) as session:
            record = select(Doc).where(Doc.c.id == query.id)
            dictionary = json.loads(record.content)

        return record != None

