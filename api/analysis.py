from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.recommendation_service import generate_recommendations
from database.dependencies import get_db
from models.resume import Resume
from models.job import Job
from schemas.analyze import AnalyzeRequest

from services.ats_service import calculate_ats_score
from services.nlp_service import calculate_similarity

router = APIRouter()


@router.get("/analyze/{resume_id}/{job_id}")
def analyze_resume(
    resume_id: int,
    job_id: int,
    db: Session = Depends(get_db)
):
    resume = db.query(Resume).filter(
        Resume.id == resume_id
    ).first()

    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if not resume:
        return {
            "message": "Resume Not Found"
        }

    if not job:
        return {
            "message": "Job Not Found"
        }

    resume_skills = [
        skill.strip()
        for skill in resume.skills.split(",")
    ]

    job_skills = [
        skill.strip()
        for skill in job.description.split(",")
    ]

    result = calculate_ats_score(
        resume_skills,
        job_skills
    )

    similarity_score = calculate_similarity(
        resume.resume_text,
        job.description
    )

    result["similarity_score"] = similarity_score
    final_score = round(
    (result["ats_score"] * 0.7)
    +
    (similarity_score * 0.3),
    2
    )
    result["final_ai_score"] = final_score
    
    selection_probability = round(
        min(final_score * 1.2, 100),
        2
    )
    
    result["selection_probability"] = selection_probability
    recommendations = generate_recommendations(
        result["missing_skills"]
    )
    result["recommendations"] = recommendations
    return result

@router.post("/analyze-direct")
def analyze_direct(
    data: AnalyzeRequest,
    db: Session = Depends(get_db)
):
    # Get resume from database
    resume = db.query(Resume).filter(
        Resume.id == data.resume_id
    ).first()

    if not resume:
        return {
            "message": "Resume Not Found"
        }

    # Extract skills from resume
    resume_skills = [
        skill.strip()
        for skill in resume.skills.split(",")
    ]

    # Extract skills from job description
    job_skills = [
        skill.strip()
        for skill in data.job_description.split(",")
    ]

    # ATS Score Calculation
    result = calculate_ats_score(
        resume_skills,
        job_skills
    )

    # Similarity Score Calculation
    similarity_score = calculate_similarity(
        resume.resume_text,
        data.job_description
    )

    result["similarity_score"] = similarity_score

    # Final AI Score
    final_score = round(
        (result["ats_score"] * 0.7) +
        (similarity_score * 0.3),
        2
    )

    result["final_ai_score"] = final_score

    # Selection Probability
    selection_probability = round(
        min(final_score * 1.2, 100),
        2
    )

    result["selection_probability"] = selection_probability

    # Recommendations
    recommendations = generate_recommendations(
        result["missing_skills"]
    )

    result["recommendations"] = recommendations

    return result 
    