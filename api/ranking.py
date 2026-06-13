from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from models.resume import Resume
from models.job import Job

router = APIRouter()


@router.get("/rank/{job_id}")
def rank_candidates(
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

    resumes = db.query(Resume).all()

    ranking = []

    job_skills = [
        skill.strip().lower()
        for skill in job.description.split(",")
    ]

    for resume in resumes:

        resume_skills = [
            skill.strip().lower()
            for skill in resume.skills.split(",")
        ]

        matched = len(
            set(resume_skills)
            &
            set(job_skills)
        )

        score = (
            matched / len(job_skills)
        ) * 100

        ranking.append({
            "resume_id": resume.id,
            "email": resume.email,
            "score": round(score, 2)
        })

    ranking.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranking