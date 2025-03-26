from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import get_db


router = APIRouter()

@router.post("/submit", response_model=schemas.PlayerOut)

def submit_player_score(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    """
    * Submit player score
    * @param {PlayerCreate} player - Player data
    * @param {Session} db - Database session
    * @returns {PlayerOut} Player information
    """
    return crud.submit_score(db=db, player_data=player)

@router.get("/leaderboard", response_model=List[schemas.PlayerOut])


def get_leaderboard(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    """
    * Get player leaderboard
    * @param {int} page - Page number, starts from 1
    * @param {int} size - Records per page
    * @param {Session} db - Database session
    * @returns {List[PlayerOut]} List of players
    """
    # 计算需要跳过的记录数
    skip = (page - 1) * size
    return crud.get_leaderboard(db=db, skip=skip, limit=size) 

@router.get("/rank/{username}", response_model=schemas.PlayerRank)
def get_player_rank(username: str, db: Session = Depends(get_db)):
    """
    * Get player ranking information
    * @param {str} username - Player username
    * @param {Session} db - Database session
    * @returns {PlayerRank} Player ranking information
    """
    result = crud.get_player_rank(db=db, username=username)
    if result is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return result 