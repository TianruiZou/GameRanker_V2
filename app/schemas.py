from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PlayerCreate(BaseModel):
    """
     * Request model for creating player
     """
    username: str
    score: int = 0


class PlayerOut(BaseModel):
    """
     * Player response model
     """
    id: int
    username: str
    score: float
    created_at: datetime

    class Config:
        orm_mode = True 

class PlayerRank(BaseModel):
    """
    * Player ranking information response model
    """
    username: str
    score: float
    rank: int 