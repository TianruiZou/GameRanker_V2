from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import api
from app.database import engine, Base

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 创建FastAPI应用
app = FastAPI(title="Game Leaderboard API", description="API for submitting and querying game player scores")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允Allow all origins, should be restricted in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(api.router, prefix="/api")

# 根路径
@app.get("/")
def read_root():
    """
     * API root path
     * @returns {dict} Welcome message
     """
    return {"message": "Welcome to Game Leaderboard API"}