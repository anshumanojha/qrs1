import streamlit as st
import sqlite3
import re
from reportlab.pdfgen import canvas
import os

# Resume Generator
class ResumeGenerator:
    def __init__(self):
        self.details = {}

    def collect_details(self, name, email, phone, education, experience, skills, current_education, current_work):
        self.details['Name'] = name
        self.details['Email'] = email
        self.details['Phone'] = phone
        self.details['Education'] = education
        self.details['Experience'] = experience
        self.details['Skills'] = skills
        self.details['CurrentEducation'] = current_education
        self.details['CurrentWork'] = current_work

    def generate_pdf(self):
        pdf_filename = f"{self.details['Name']}_Resume.pdf"
        pdf_filepath = os.path.join(os.path.dirname(__file__), pdf_filename)

        # Create a PDF document
        pdf_canvas = canvas.Canvas(pdf_filepath)

        # Add content to the PDF
        pdf_canvas.setFont("Helvetica-Bold", 14)
        pdf_canvas.drawString(100, 800, f"Resume for {self.details['Name']}")
        pdf_canvas.setFont("Helvetica", 12)

        # Contact Information
        pdf_canvas.drawString(100, 780, f"Email: {self.details['Email']} | Phone: {self.details['Phone']}")

        # Education
        pdf_canvas.setFont("Helvetica-Bold", 12)
        pdf_canvas.drawString(100, 760, "Education:")
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(120, 740, f"School: {self.details['Education']['School']}")
        pdf_canvas.drawString(120, 720, f"Years: {self.details['Education']['StartYear']} - {self.details['Education']['EndYear']}")
        if self.details['CurrentEducation']:
            pdf_canvas.drawString(120, 700, "Currently pursuing")

        # Experience
        pdf_canvas.setFont("Helvetica-Bold", 12)
        pdf_canvas.drawString(100, 670, "Experience:")
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(120, 650, f"Company: {self.details['Experience']['Company']}")
        pdf_canvas.drawString(120, 630, f"Years: {self.details['Experience']['StartYear']} - {self.details['Experience']['EndYear']}")
        if self.details['CurrentWork']:
            pdf_canvas.drawString(120, 610, "Currently working here")

        # Skills
        pdf_canvas.setFont("Helvetica-Bold", 12)
        pdf_canvas.drawString(100, 580, "Skills:")
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(120, 560, self.details['Skills'])

        # Save the PDF
        pdf_canvas.save()

        return pdf_filepath

# Streamlit App
def main():
    # ... (previous code)

    # Project 3 - Resume Generator
    st.header('Project 3 - Resume Generator')

    # Collect user details
    name = st.text_input("Full Name:")
    email = st.text_input("Email:")
    phone = st.text_input("Phone:")

    # Education Details
    st.subheader('Education Details')
    school = st.text_input("School:")
    start_year_edu = st.text_input("Start Year:")
    end_year_edu = st.text_input("End Year:")
    current_education = st.checkbox("Currently pursuing this education")

    # Experience Details
    st.subheader('Experience Details')
    company = st.text_input("Company:")
    start_year_exp = st.text_input("Start Year:")
    end_year_exp = st.text_input("End Year:")
    current_work = st.checkbox("Currently working here")

    # Skills
    st.subheader('Skills')
    skills = st.text_area("Skills:")

    # Resume Generator
    resume_generator = ResumeGenerator()

    if st.button("Generate Resume (PDF)"):
        resume_generator.collect_details(
            name, email, phone,
            {'School': school, 'StartYear': start_year_edu, 'EndYear': end_year_edu},
            {'Company': company, 'StartYear': start_year_exp, 'EndYear': end_year_exp},
            skills, current_education, current_work
        )
        pdf_filepath = resume_generator.generate_pdf()

        # Provide a download button for the generated PDF
        st.download_button(
            label="Download Resume (PDF)",
            data=open(pdf_filepath, "rb").read(),
            file_name=f"{name}_Resume.pdf",
            key="download_resume_button"
        )

    # Rest of the code remains the same

if __name__ == "__main__":
    main()
