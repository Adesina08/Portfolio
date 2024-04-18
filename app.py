from pathlib import Path

import streamlit as st
from PIL import Image



#------PATH SETTINGS -----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Adesina Adeyemo-CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"



#-------GENERAL SETTINGS ------
PAGE_TITLE = "Digital CV | Adesina Adeyemo"
PAGE_ICON = ":wave:"
NAME = "Adesina Adeyemo"
DESCRIPTION = """Detail-oriented data analyst with expertise in analytics, visualization, and problem-solving. Assisting enterprises by supporting data-driven decision-making."""

EMAIL = "seun080ade@gmail.com"
SOCIAL_MEDIA = {
	"LinkedIn": "https://www.linkedin.com/in/adesina-adeyemo-a27924264?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app",
	"GitHub": "https://github.com/Adesina08",
	"Twitter": "https://twitter.com/xPliot888_",
}
PROJECTS = {
	"🏆 Google Data Analytics Professional Certificate-Google - Issued by Coursea": "https://www.credly.com/badges/0639f257-4e90-48a0-b5c0-97dadf7c4d8c/public_url",
	"🏆 Excel Skills for Data Analytics and Visualization Specialization-Macquarie University -Issued by Coursera ": "https://coursera.org/share/8ee8843bb097c1042fcb8dacb93aaf35",
	"🏆 Data Science Math Skills-Duke University -Issued by Coursera": "https://coursera.org/share/b1a79388ce1a483dbe8c6e85373db8ad",
	"🏆 Customer Analytics-University of Pennsylvania -Issued by Cousera": "https://coursera.org/share/1a340c793ad22c97b85f4e0afda967a6",
    "🏆 Data-Driven Process Improvement-University of Buffalo -Issued by Cousera": "https://coursera.org/share/c30a4fccb9959045417a6ccb009b4b8e",
    "🏆 Introduction to Structured Query Language (SQL)-University of Michigan -Issued by Cousera": "https://coursera.org/share/48c11329a93c87bf11737306f9904996",
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



# ---- LOAD CSS, PDF & PROFILE PICTURE -----
with open(css_file) as f:
	st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
	PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



# ----- HERO SECTION -----
col1, col2 = st.columns(2, gap="small")
with col1:
	st.image(profile_pic, width=300)

with col2:
	st.title(NAME)
	st.write(DESCRIPTION)
	st.download_button(
		label="📜 Download Resume",
		data=PDFbyte,
		file_name=resume_file.name,
		mime="application/octet-stream",
	)
	st.write("📧", EMAIL)




# ------ SOCIAL LINKS ------
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
	cols[index].write(f"[{platform}]({link})")



# ----- EXPERIENCE & QUALIFICATIONS ------
st.write("#")
st.header("Experience & Qualifications")
st.write(
	"""
	- ☑️ Notable experience extracting actionable insights from data
	- ☑️ Strong hands on experience and knowledge in Excel and Python
	- ☑️ Good understanding of statistical principles and their respective applications
	- ☑️ Excellent team-player and displaying strong sense of initiative on tasks
	"""
	)


# ----- SKILLS -----
st.write("#")
st.subheader("Hard Skills")
st.write(
	"""
	- 👨‍💻 Programming: Python (Numpy, Pandas, Streamlit, Scikit-learn), SQL
	- 📊 Data Visulaization: PowerBI, MS Excel, Plotly
	- 📚 Modeling: Logistic Regression, Linear Regression, Decision Trees
	- 🗄️ Databases: MS SQL server, MySQL
	"""
	)




# ----- WORK HISTORY ------
st.write("#")
st.subheader("Work History")
st.write("---")


# --- JOB 1
st.write("🖥️", "**Assistant Data Management Executive | Ipsos, Nigeria**")
st.write("05/2023 - Present")
st.write(
	"""
	- ▶️ Led the MIS team to create standard report and revamped existing QC report to deliver to stakeholders to better understand precise business information and insights.
	- ▶️ Utilized a curated set of cutting-edge software, resulting in a 15% improvement in data interpretation accuracy and informed strategic decisions.
	- ▶️ Developed and maintained automated reporting systems, achieving a 30% reduction in manual effort and ensuring timely and precise information delivery.
	"""
	)


# --- JOB 2
st.write("#")
st.write("🖥️", "**Data Analyst | Accenture, North America (Virtual Internship)**")
st.write("December 2023(completed)")
st.write(
	"""
	- ▶️ Completed a simulation focused on advising a hypothetical social media client as a data analyst at Accenture.
	- ▶️ Cleaned, modelled and analyzed seven datasets in Microsoft Excel to uncover insights into content trends to inform strategic decisions.
	- ▶️ Prepared a PowerPoint deck and video presentation to communicate key insights for the clients and internal stake holders.
	"""
	)


# --- JOB 3
st.write("#")
st.write("🖥️", "**Data Analyst | MeriSKILL, India (Virtual Internship)**")
st.write("November 2023(completed)")
st.write(
	"""
	- ▶️ Developed a sales dashboard in Microsoft Excel to be able to analyze and visualize sales data to identify trends like top-selling products, and revenue metrics for business decision-making. 
	- ▶️ Created a predictive analysis model with Python in Jupyter Notebook to predict potential diabetes patients.
	- ▶️ Cleaned and visualized a HR analytics dataset to enable HR to understand some trend using various metrics like Overtime, Marital Status, Gender, Job roles and other important metrics to enable make certain decisions on behalf of the employees. 
	"""
	)


# ------ Projects & Accomplishments ----
st.write("#")
st.subheader("Projects &  Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
	st.write(f"[{project}]({link})")












