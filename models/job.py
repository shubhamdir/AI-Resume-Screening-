from sqlalchemy import Column, Integer, String, Text
from database.base import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255))

    domain = Column(String(100))

    description = Column(Text)