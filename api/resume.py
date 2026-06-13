from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import shutil
import os

from database.dependencies import get_db
from models.resume import Resume

from services.resume_service import (
    extract_text_from_pdf,
    extract_email,
    extract_phone,
    extract_skills
)

router = APIRouter()

UPLOAD_DIR = "uploads"


@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    text = extract_text_from_pdf(
        file_path
    )

    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)

    resume = Resume(
        filename=file.filename,
        filepath=file_path,
        email=email,
        phone=phone,
        skills=", ".join(skills),
        resume_text=text
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return {
        "resume_id": resume.id,
        "filename": file.filename,
        "email": email,
        "phone": phone,
        "skills": skills
    }


@router.get("/resume/{resume_id}")
def get_resume(
    resume_id: int,
    db: Session = Depends(get_db)
):
    resume = db.query(Resume).filter(
        Resume.id == resume_id
    ).first()

    if not resume:
        return {
            "message": "Resume Not Found"
        }

    return {
        "id": resume.id,
        "filename": resume.filename,
        "email": resume.email,
        "phone": resume.phone,
        "skills": resume.skills
    }