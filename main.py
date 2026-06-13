from fastapi import FastAPI
from models.job import Job
from database.base import Base
from database.session import engine
from api.ranking import router as ranking_router
from models.resume import Resume

# Import Models so SQLALchemy can create tables
from models.user import User
from api.resume import router as resume_router
from api.auth import router as auth_router
from api.job import router as job_router
from api.analysis import router as analysis_router
app = FastAPI()
app.include_router(analysis_router)
app.include_router(resume_router)
app.include_router(auth_router)
app.include_router(job_router)
app.include_router(ranking_router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "AI Resume Screening System Running"
    }