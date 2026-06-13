def calculate_ats_score(
    resume_skills,
    job_skills
):
    matched_skills = []

    for skill in resume_skills:
        if skill.lower() in [
            s.lower() for s in job_skills
        ]:
            matched_skills.append(skill)

    missing_skills = []

    for skill in job_skills:
        if skill.lower() not in [
            s.lower() for s in resume_skills
        ]:
            missing_skills.append(skill)

    if len(job_skills) == 0:
        score = 0
    else:
        score = int(
            (len(matched_skills) / len(job_skills))
            * 100
        )

    return {
        "ats_score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }