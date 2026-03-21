from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

from app.infrastructure.database.session import Base


class BoardORM(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    account_id = Column(Integer, ForeignKey("members.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
