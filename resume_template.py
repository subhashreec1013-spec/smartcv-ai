def generate_resume_html(data):

    def to_list(text):
        if "\n" in text:
            items = text.split("\n")
        else:
            items = text.split(",")

        return "".join([f"<li>{i.strip()}</li>" for i in items if i.strip()])

    education_list = to_list(data["education"])
    skills_list = to_list(data["skills"])
    projects_list = to_list(data["projects"])
    experience_list = to_list(data["experience"])

    return f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
    font-family: Arial;
    background: #f4f6fb;
    margin: 0;
    padding: 20px;
}}

.container {{
    max-width: 800px;
    margin: auto;
    background: white;
    padding: 30px;
    border-radius: 10px;
}}

.header {{
    background: #4b6cff;
    color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}}

h2 {{
    border-bottom: 2px solid #ddd;
    padding-bottom: 5px;
    margin-top: 25px;
}}

ul {{
    padding-left: 20px;
}}

li {{
    margin-bottom: 8px;
}}
</style>
</head>

<body>

<div class="container">

<div class="header">
    <h1>{data["name"]}</h1>
    <p>{data["role"]}</p>
</div>

<h2>Education</h2>
<ul>{education_list}</ul>

<h2>Skills</h2>
<ul>{skills_list}</ul>

<h2>Projects</h2>
<ul>{projects_list}</ul>

<h2>Experience</h2>
<ul>{experience_list}</ul>

</div>

</body>
</html>
"""
