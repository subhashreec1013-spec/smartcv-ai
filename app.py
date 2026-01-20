import streamlit as st
import os
from datetime import date
from openai import OpenAI

# Create client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="SmartCV AI", page_icon="🎓", layout="centered")

# Sidebar
st.sidebar.title("SmartCV AI")
st.sidebar.markdown("AI Resume & Portfolio Builder")
st.sidebar.info("IBM Edunet Skills Internship Project")

st.title("🎓 SmartCV – AI Resume & Portfolio Builder")
st.caption("Create professional resumes and portfolios using Artificial Intelligence")

with st.form("resume_form"):
    st.subheader("Enter Your Details")

    name = st.text_input("Full Name")
    education = st.text_area("Education")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")
    experience = st.text_area("Experience")
    role = st.text_input("Target Job Role")

    submit = st.form_submit_button("🚀 Generate Resume using AI")

if submit:
    if not os.getenv("OPENAI_API_KEY"):
        st.error("API key not found. Set OPENAI_API_KEY environment variable.")
    else:
        prompt = f"""
Create a professional resume for:

Name: {name}
Education: {education}
Skills: {skills}
Projects: {projects}
Experience: {experience}
Target Job Role: {role}

Use clear section headings: Objective, Education, Skills, Projects, Experience.
"""

        with st.spinner("AI is generating your resume..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            resume_text = response.choices[0].message.content

        st.success("✅ Resume generated successfully!")

        st.subheader("Generated Resume")
        st.text_area("", resume_text, height=350)

        st.download_button("📥 Download Resume (TXT)", resume_text, "resume.txt")

        portfolio_html = f"""
        <html>
        <head><title>{name} Portfolio</title></head>
        <body>
            <h1>{name}</h1>
            <pre>{resume_text}</pre>
            <p>Generated on {date.today()}</p>
        </body>
        </html>
        """

        st.download_button("🌐 Download Portfolio Website (HTML)", portfolio_html, "portfolio.html")

st.markdown("---")
st.caption("© 2026 SmartCV | AI Project for IBM Edunet Skills Internship")
