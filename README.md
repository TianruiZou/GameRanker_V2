# GameRanker API

A scalable leaderboard backend service built with FastAPI and PostgreSQL.  
Designed for competitive games, this backend allows players to submit scores, retrieve leaderboards, and view their global rankings.

## Features
- Submit or update player scores
- Paginated leaderboard (sorted by highest score)
- Global rank lookup for specific users
- PostgreSQL + SQLAlchemy backend
- Docker-based database setup
- Pydantic schema validation
- Modular architecture with routing and CRUD separation

## Tech Stack
- Python 3.11
- FastAPI
- PostgreSQL (via Docker)
- SQLAlchemy
- Pydantic
- dotenv

## Quickstart

1. Start PostgreSQL database:
   ```bash
   docker-compose up -d
