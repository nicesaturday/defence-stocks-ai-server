from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.infrastructure.database.session import Base


class AccountORM(Base):
    __tablename__ = "members"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    kakao_id = Column(String(64), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
