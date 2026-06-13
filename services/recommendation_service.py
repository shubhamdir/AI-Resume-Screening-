def generate_recommendations(
    missing_skills
):
    recommendations = []

    for skill in missing_skills:

        recommendations.append(
            f"Learn {skill}"
        )

        recommendations.append(
            f"Add a project demonstrating {skill}"
        )

        recommendations.append(
            f"Include {skill} in your resume if you have experience"
        )

    return recommendations