def calculate_ats_score(resume_text, job_role):

    keywords = {
        "AI Engineer": ["python", "machine learning", "deep learning", "nlp", "data", "api"],
        "Software Developer": ["python", "java", "sql", "git", "api", "backend"],
        "Data Analyst": ["python", "sql", "excel", "data analysis", "statistics", "visualization"]
    }

    role_keywords = keywords.get(job_role, [])

    resume_lower = resume_text.lower()
    match_count = 0

    for word in role_keywords:
        if word in resume_lower:
            match_count += 1

    skill_score = (match_count / len(role_keywords)) * 100 if role_keywords else 50

    length_score = min(len(resume_text) / 1000 * 20, 20)

    ats_score = int(skill_score * 0.7 + length_score)

    missing_skills = [w for w in role_keywords if w not in resume_lower]

    suggestions = []

    if ats_score < 60:
        suggestions.append("Add more job-specific technical skills.")
        suggestions.append("Include measurable project outcomes.")
        suggestions.append("Use clear section headings.")

    if missing_skills:
        suggestions.append("Consider adding these skills: " + ", ".join(missing_skills))

    return ats_score, missing_skills, suggestions
