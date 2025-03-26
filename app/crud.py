from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional, List, Dict, Union
from app.models import Player  # 修改这里：使用绝对导入路径
from app.schemas import PlayerCreate


def submit_score(db: Session, player_data: PlayerCreate) -> Player:
    """
     * Submit player score
     * @param {Session} db - Database session
     * @param {PlayerCreate} player_data - Player data
     * @returns {Player} Updated player object
     * @raises {ValueError} When score format is invalid
     """
    try:
        score = float(player_data.score)
    except (ValueError, TypeError):
        raise ValueError("Invalid score format")

    # #Check if player exists in database
    db_player = db.query(Player).filter(Player.username == player_data.username).first()
    
    # If player doesn't exist, create new player
    if db_player is None:
        db_player = Player(
            username=player_data.username,
            score=score
        )
        db.add(db_player)
    elif score > db_player.score:
        db_player.score = score
    
    try:
        db.commit()
        db.refresh(db_player)
    except Exception as e:
        db.rollback()
        raise Exception(f"Database error: {str(e)}")
    
    return db_player

def get_leaderboard(db: Session, skip: int = 0, limit: int = 10) -> List[Player]:
    """
    * Get player leaderboard
    * @param {Session} db - Database session
    * @param {int} skip - Number of records to skip
    * @param {int} limit - Number of records to return
    * @returns {List[Player]} List of players
    * @raises {ValueError} When pagination parameters are invalid
    """
    if skip < 0 or limit < 1:
        raise ValueError("Invalid pagination parameters")
        
    try:
        return (
            db.query(Player)
            .order_by(Player.score.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
    except Exception as e:
        raise Exception(f"Database error: {str(e)}")

def get_player_rank(db: Session, username: str) -> Optional[Dict[str, Union[str, float, int]]]:
    """
     * Get player ranking information
     * @param {Session} db - Database session
     * @param {str} username - Player username
     * @returns {Optional[Dict]} Dictionary containing player info and rank, returns None if player not found
     * @raises {Exception} When database query fails
    """
    try:
        # First get player information
        player = db.query(Player).filter(Player.username == username).first()
        
        if not player:
            return None
            
        # Calculate rank (number of players with higher scores)
        rank = db.query(Player).filter(Player.score > player.score).count()
        
        return {
            "username": player.username,
            "score": player.score,
            "rank": rank + 1  # Add 1 because ranking starts from 1
        }
    except Exception as e:
        raise Exception(f"Database error: {str(e)}")