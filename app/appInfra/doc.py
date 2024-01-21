from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class Doc(Base):
    __tablename__ = "doc"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(1024))
    collection: Mapped[str] = mapped_column(String(1024))
    content: Mapped[str] = mapped_column(String(1024))
    tags: Mapped[str] = mapped_column(String(1024))
    created_by: Mapped[str] = mapped_column(String(1024))
    updated_by: Mapped[str] = mapped_column(String(1024))
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
