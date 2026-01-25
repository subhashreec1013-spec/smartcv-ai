def calculate_ats_score(resume_text, job_role):

    resume_text = resume_text.lower()

    ROLE_KEYWORDS = {
        "ai engineer": [
            "python", "machine learning", "ml", "deep learning", "dl",
            "nlp", "sql", "tensorflow", "pytorch", "pandas", "numpy",
            "scikit-learn", "flask", "streamlit", "git", "api", "data analysis"
        ],

        "software developer": [
            "python", "java", "c++", "sql", "git", "api", "backend",
            "frontend", "javascript", "html", "css", "database", "oop"
        ],

        "data analyst": [
            "python", "sql", "excel", "power bi", "tableau", "statistics",
            "data analysis", "pandas", "numpy", "visualization"
        ]
    }

    role_key = job_role.lower()
    required_skills = ROLE_KEYWORDS.get(role_key, [])

    matched = []
    missing = []

    for skill in required_skills:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    total_skills = len(required_skills)
    found_skills = len(matched)

    # ---------- BASE SCORE ----------
    if total_skills == 0:
        score = 60
    else:
        score = int((found_skills / total_skills) * 70)

    # ---------- BONUS POINTS ----------
    if "project" in resume_text:
        score += 10

    if "experience" in resume_text or "intern" in resume_text:
        score += 10

    if len(resume_text) > 800:
        score += 5

    score = min(score, 95)

    # ---------- SUGGESTIONS ----------
    suggestions = []

    if missing:
        suggestions.append("Add missing job-specific technical skills.")

    if "project" not in resume_text:
        suggestions.append("Include relevant technical projects.")

    if "experience" not in resume_text and "intern" not in resume_text:
        suggestions.append("Add internship or work experience section.")

    if score < 70:
        suggestions.append("Optimize resume keywords to improve ATS compatibility.")

    return score, missing[:6], suggestions
