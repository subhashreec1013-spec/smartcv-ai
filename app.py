import streamlit as st
import os
import openai
from datetime import date

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Page config
st.set_page_config(page_title="SmartCV AI", layout="centered")

st.title("🎓 SmartCV – AI Resume & Portfolio Builder")
st.write("Generate professional resumes and portfolios using Artificial Intelligence")

# Form
with st.form("resume_form"):
    name = st.text_input("Full Name")
    education = st.text_area("Education")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")
    experience = st.text_area("Experience")
    role = st.text_input("Target Job Role")

    submit = st.form_submit_button("🚀 Generate using AI")

# Generate Resume
if submit:
    if not openai.api_key:
        st.error("API key not found. Please set OPENAI_API_KEY environment variable.")
    else:
        prompt = f"""
Create a professional resume for the following candidate:

Name: {name}
Education: {education}
Skills: {skills}
Projects: {projects}
Experience: {experience}
Target Job Role: {role}

Format it properly with clear sections:
Objective, Education, Skills, Projects, Experience.
"""

        with st.spinner("AI is generating your resume..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            resume_text = response.choices[0].message.content

        st.success("✅ Resume generated successfully!")

        st.text_area("📄 Generated Resume", resume_text, height=350)

        st.download_button(
            label="📥 Download Resume (TXT)",
            data=resume_text,
            file_name="resume.txt"
        )

        # Portfolio HTML
        portfolio_html = f"""
        <html>
        <head><title>{name} Portfolio</title></head>
        <body>
            <h1>{name}</h1>
            <pre>{resume_text}</pre>
            <p>Generated on: {date.today()}</p>
        </body>
        </html>
        """

        st.download_button(
            label="🌐 Download Portfolio Website (HTML)",
            data=portfolio_html,
            file_name="portfolio.html"
        )
