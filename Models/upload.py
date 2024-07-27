from sqlalchemy import Column, Integer, String, DateTime
from .base import BaseModel, db
from datetime import datetime


class Upload(BaseModel):
    __tablename__ = 'uploads'

    id = Column(Integer, primary_key=True)
    file_name = Column(String(256), nullable=False)
    file_path = Column(String(256), nullable=False)
    createdAt = Column(DateTime, default=datetime.now)

    @classmethod
    def create(cls, file_name, file_path):
        new_upload = cls(file_name=file_name, file_path=file_path)
        db.session.add(new_upload)
        db.session.commit()
        return new_upload



