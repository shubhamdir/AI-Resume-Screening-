from sqlalchemy import Column, Integer, String, Text
from database.base import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String(255))
    filepath = Column(String(500))

    email = Column(String(255))
    phone = Column(String(20))

    skills = Column(Text)

    resume_text = Column(Text)