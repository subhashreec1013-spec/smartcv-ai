import streamlit as st
import os
from datetime import date
from ats_analyzer import calculate_ats_score
from resume_template import generate_resume_html

# ---------- OPENAI SETUP ----------
try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    OPENAI_AVAILABLE = True
except:
    OPENAI_AVAILABLE = False

st.set_page_config(page_title="SmartCV AI", page_icon="🎓", layout="centered")

# ---------- SIDEBAR ----------
st.sidebar.markdown("""
<h2 style='color:#4b6cff;'>SmartCV Pro</h2>
<p style='font-size:14px;'>AI Career Assistant</p>
<hr>
""", unsafe_allow_html=True)

st.sidebar.success("IBM Edunet Skills Project")
st.sidebar.info("AI Resume Generator + ATS Analyzer")
st.sidebar.markdown("Version: 1.0")

# ---------- HEADER ----------
st.title("🎓 SmartCV – AI Resume & Portfolio Builder")
st.caption("Create professional resumes and portfolios using Artificial Intelligence")

st.markdown("""
<div style="
background: linear-gradient(90deg, #4b6cff, #6a5acd);
padding: 15px;
border-radius: 10px;
color: white;
margin-bottom: 20px;
">
<h3>🚀 Build smart resumes. Beat ATS. Get hired.</h3>
<p>AI-powered resume generation, ATS analysis, and portfolio creation platform.</p>
</div>
""", unsafe_allow_html=True)

# ---------- FORM ----------
with st.form("resume_form"):
    name = st.text_input("Full Name")
    education = st.text_area("Education")
    skills = st.text_area("Skills (one per line)")
    projects = st.text_area("Projects (one per line)")
    experience = st.text_area("Experience (one per line)")
    role = st.text_input("Target Job Role")

    submit = st.form_submit_button("🚀 Generate Resume")

# ---------- HELPERS ----------
def smart_split(text):
    if "\n" in text:
        parts = text.split("\n")
    else:
        parts = text.split(",")

    return [p.strip() for p in parts if p.strip()]

def to_list_html(text):
    return "".join([f"<li>{item}</li>" for item in smart_split(text)])

def offline_resume():
    return f"""
{name}

OBJECTIVE:
Seeking a position as {role} to apply my technical and problem-solving skills.

EDUCATION:
{education}

SKILLS:
{skills}

PROJECTS:
{projects}

EXPERIENCE:
{experience}

Generated on: {date.today()}
"""

# ---------- MAIN ----------
if submit:

    # ----- Resume Generation -----
    if OPENAI_AVAILABLE and os.getenv("OPENAI_API_KEY"):
        try:
            prompt = f"""
Create a professional resume for:

Name: {name}
Education: {education}
Skills: {skills}
Projects: {projects}
Experience: {experience}
Job Role: {role}

Use proper sections and bullet points.
"""
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            resume_text = response.choices[0].message.content
            st.success("Resume generated using AI!")

        except:
            st.warning("OpenAI quota exceeded. Switching to offline mode.")
            resume_text = offline_resume()
    else:
        resume_text = offline_resume()

    # ---------- DISPLAY RESUME ----------
    st.markdown("## 📄 Generated Resume")

    st.text_area("", resume_text, height=320)

    # ---------- ATS ----------
    st.markdown("## 📊 ATS Resume Analysis")

    ats_score, missing_skills, suggestions = calculate_ats_score(resume_text, role)

    st.metric("ATS Score", f"{ats_score} / 100")

    if missing_skills:
        st.warning("Missing Skills: " + ", ".join(missing_skills))
    else:
        st.success("No critical skills missing.")

    st.subheader("💡 Suggestions")
    for s in suggestions:
        st.write("•", s)

    # ---------- Styled Resume ----------
    resume_data = {
        "name": name,
        "role": role,
        "skills": skills,
        "education": education,
        "projects": projects,
        "experience": experience
    }

    resume_html = generate_resume_html(resume_data)

    st.download_button(
        "📥 Download Styled Resume (HTML)",
        resume_html,
        file_name="resume.html",
        mime="text/html"
    )

    # ---------- Portfolio ----------
    skills_list = to_list_html(skills)
    projects_list = to_list_html(projects)
    experience_list = to_list_html(experience)

    portfolio_html = f"""
<!DOCTYPE html>
<html>
<head>
<title>{name} - Portfolio</title>
<style>
body {{ font-family: Arial; background:#f4f6fb; margin:0; }}
header {{ background:#4b6cff; color:white; padding:30px; text-align:center; }}
section {{ background:white; margin:20px; padding:20px; border-radius:10px; }}
ul {{ padding-left:20px; }}
li {{ margin-bottom:8px; }}
</style>
</head>
<body>

<header>
<h1>{name}</h1>
<p>{role}</p>
</header>

<section>
<h2>Skills</h2>
<ul>{skills_list}</ul>
</section>

<section>
<h2>Projects</h2>
<ul>{projects_list}</ul>
</section>

<section>
<h2>Experience</h2>
<ul>{experience_list}</ul>
</section>

<section>
<h2>Education</h2>
<p>{education}</p>
</section>

</body>
</html>
"""

    st.download_button(
        "🌐 Download Portfolio Website",
        portfolio_html,
        file_name="portfolio.html",
        mime="text/html"
    )

# ---------- FOOTER ----------
st.markdown("---")
st.caption("© 2026 SmartCV | AI Project for IBM Edunet Skills Internship")
