from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
import datetime
from app.database import Base


class Player(Base):
    """
     * Player Model
     """
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    score = Column(Float, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow) 