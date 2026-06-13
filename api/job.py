from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from models.job import Job
from schemas.job import JobCreate

router = APIRouter()


@router.post("/upload-job")
def upload_job(
    job: JobCreate,
    db: Session = Depends(get_db)
):
    new_job = Job(
        title=job.title,
        domain=job.domain,
        description=job.description
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return {
        "job_id": new_job.id,
        "title": new_job.title,
        "domain": new_job.domain,
        "message": "Job Uploaded Successfully"
    }


@router.get("/job/{job_id}")
def get_job(
    job_id: int,
    db: Session = Depends(get_db)
):
    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if not job:
        return {
            "message": "Job Not Found"
        }

    return {
        "id": job.id,
        "title": job.title,
        "domain": job.domain,
        "description": job.description
    }