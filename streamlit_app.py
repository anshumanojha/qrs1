import streamlit as st
import sqlite3
import re
from reportlab.pdfgen import canvas
import os

# Resume Generator
class ResumeGenerator:
    def __init__(self):
        self.details = {}

    def collect_details(self, name, email, phone, education, experience, skills):
        self.details['Name'] = name
        self.details['Email'] = email
        self.details['Phone'] = phone
        self.details['Education'] = education
        self.details['Experience'] = experience
        self.details['Skills'] = skills

    def generate_pdf(self):
        pdf_filename = f"{self.details['Name']}_Resume.pdf"
        pdf_filepath = os.path.join(os.path.dirname(__file__), pdf_filename)

        # Create a PDF document
        pdf_canvas = canvas.Canvas(pdf_filepath)

        # Add content to the PDF
        pdf_canvas.drawString(100, 800, f"Resume for {self.details['Name']}")
        pdf_canvas.drawString(100, 780, f"Email: {self.details['Email']} | Phone: {self.details['Phone']}")
        pdf_canvas.drawString(100, 760, f"Education: {self.details['Education']}")
        pdf_canvas.drawString(100, 740, f"Experience: {self.details['Experience']}")
        pdf_canvas.drawString(100, 720, f"Skills: {self.details['Skills']}")

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
    education = st.text_area("Education:")
    experience = st.text_area("Experience:")
    skills = st.text_area("Skills:")

    # Resume Generator
    resume_generator = ResumeGenerator()

    if st.button("Generate Resume (PDF)"):
        resume_generator.collect_details(name, email, phone, education, experience, skills)
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
