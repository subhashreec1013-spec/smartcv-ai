import streamlit as st
from datetime import date

st.set_page_config(page_title="SmartCV AI")

st.title("SmartCV – AI Resume & Portfolio Builder")

with st.form("form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    education = st.text_area("Education")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")
    experience = st.text_area("Experience")
    role = st.text_input("Target Job Role")

    submit = st.form_submit_button("Generate")

if submit:
    resume = f"""
{name}
Email: {email}
Phone: {phone}

Objective:
Seeking a position as {role} to apply my skills.

Education:
{education}

Skills:
{skills}

Projects:
{projects}

Experience:
{experience}

Date: {date.today()}
"""

    st.success("Resume Generated Successfully!")

    st.text_area("Generated Resume", resume, height=300)

    st.download_button("Download Resume", resume, "resume.txt")

    portfolio = f"""
<html>
<body>
<h1>{name}</h1>
<p>{email} | {phone}</p>

<h2>Education</h2>
<p>{education}</p>

<h2>Skills</h2>
<p>{skills}</p>

<h2>Projects</h2>
<p>{projects}</p>

<h2>Experience</h2>
<p>{experience}</p>

</body>
</html>
"""

    st.download_button("Download Portfolio Website", portfolio, "portfolio.html")
