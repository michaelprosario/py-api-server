from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy import JSON
from sqlalchemy import Text
from sqlalchemy import TIMESTAMP
from sqlalchemy import func


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

from typing import List
from typing import Optional
import time
import json
import sys
import os

sys.path.append('../appCore')
from appCore.responses import AppResponse
from appCore.responses import GetRecordResponse
from appCore.responses import GetRecordsResponse
from appCore.documentServices import GetDocumentQuery
sys.path.append('../appInfra')

PgBase = declarative_base()
Session = sessionmaker()

class PgDoc(PgBase):
    __tablename__ = 'docs'

    id = Column(String, primary_key=True)
    name = Column(String)
    collection = Column(String)
    content = Column(Text)
    tags = Column(JSON)
    created_by = Column(String)
    updated_by = Column(String)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

connectionString = "postgresql://docs:docs@localhost/docs"
class DocPgRepository():
    def setupMemoryDatabase(self):
        self.engine = create_engine(connectionString, echo=True)
        PgBase.metadata.create_all(self.engine)

    def setupAppDatabase(self):
        self.engine = create_engine(connectionString, echo=True)
        PgBase.metadata.create_all(self.engine)
        Session.configure(bind=self.engine)
    
    def addDocument(self,command):
        timeStamp = func.now()

        #command.data['createdAt'] = timeStamp

        strData = json.dumps(command.data)

        with Session() as session:
            record = PgDoc(
                id=command.id, 
                name=command.name, 
                collection=command.collection,
                content=strData,
                tags = command.tags,
                created_by='system',
                updated_by='system', 
                created_at=timeStamp, 
                updated_at=timeStamp
                )
            session.add_all([record])
            session.commit()

        response = AppResponse()
        return response

    def updateDocument(self,command):
        timeStamp = func.now()
        #command.data['updatedAt'] = timeStamp

        strData = json.dumps(command.data)

        with Session() as session:
            record = session.get(PgDoc, command.id)
            record.content = strData
            record.name = command.name
            record.tags = command.tags
            record.updated_at = timeStamp
            session.commit()

        response = AppResponse()
        return response

    def deleteDocument(self,query):
        if self.recordExists(query):
            with Session() as session:
                record = session.get(PgDoc, query.id)
                session.delete(record)
                session.commit()
        
        response = AppResponse()
        return response

    def getDocuments(self,query):
        records = []
        print(query)

        with Session() as session:
            if len(query.keyword) > 0:
                search = "%{}%".format(query.keyword)
                recordSet = session.query(PgDoc).filter(PgDoc.content.like(search))            
            elif len(query.collection) > 0:
                recordSet = session.query(PgDoc).filter(PgDoc.collection == query.collection)            
            else:
                recordSet = session.query(PgDoc).all()

            for record in recordSet:
                query = GetDocumentQuery(userId="system", id=record.id)
                getResponse = self.getDocument(query)
                if getResponse.status == 200:
                    records.append(getResponse.record)

        response = GetRecordsResponse(data=records, userId=query.userId)
        return response

    def getDocument(self,query):
        with Session() as session:
            record = session.get(PgDoc, query.id)
            if( record == None):
                return AppResponse(status=404, message="Record not found")
            
            dictionary = json.loads(record.content)
            dictionary['createdAt'] = record.created_at
            dictionary['updatedAt'] = record.updated_at

            response = GetRecordResponse(record=dictionary, userId="system")
        return response

    def recordExists(self,query):
        if query == None:
            raise Exception("Query is not defined")

        with Session() as session:
            record = session.get(PgDoc, query.id)

        return record != None

