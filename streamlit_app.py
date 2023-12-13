import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

# Function to generate PDF
def generate_pdf():
    buffer = BytesIO()

    # Create a PDF object
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 8)  # Change the font and size as needed

    # Add borders to the PDF
    page_width, page_height = letter
    pdf.line(0, page_height, page_width, page_height)  # Top border
    pdf.line(0, page_height, 0, 0)                     # Left border
    pdf.line(0, 0, page_width, 0)                      # Bottom border
    pdf.line(page_width, 0, page_width, page_height)   # Right border

    # Set up the PDF content with left alignment
    pdf.drawString(20, page_height - 20, ">>>This resume was generated entirely in Python. For full source code, view my portfolio.")
    pdf.drawString(20, page_height - 40, "Anshuman Ojha's Resume")
    pdf.line(0, page_height - 45, page_width, page_height - 45)  # Top border for header

    # Personal Information
    pdf.drawString(20, page_height - 70, "Personal Information:")
    pdf.drawString(20, page_height - 90, "Location: Bangalore")
    pdf.drawString(20, page_height - 110, "Name: Anshuman")
    pdf.drawString(20, page_height - 130, "Designation: Finops Analyst")
    pdf.drawString(20, page_height - 150, "Contact: 877743144")
    pdf.drawString(20, page_height - 170, "Email: anshumanojha94@gmail.com")

    # Work Experience
    pdf.drawString(20, page_height - 210, "Work Experience:")
    pdf.drawString(20, page_height - 230, "Finops(Revenue&Recon Analyst) - Freo")
    pdf.drawString(40, page_height - 250, "Duration: Dec 2020 - Present")
    pdf.drawString(40, page_height - 270, "Description:")
    pdf.drawString(60, page_height - 290, "- MIS")
    pdf.drawString(60, page_height - 310, "- Revenue automation")
    pdf.drawString(60, page_height - 330, "- Partner onboarding")
    pdf.drawString(60, page_height - 350, "- Made dashboards to check repayment")
    pdf.drawString(60, page_height - 370, "- Day-to-day repayment recon")
    pdf.drawString(60, page_height - 390, "- Solving payments disputes")
    pdf.drawString(60, page_height - 410, "- Development and verification of monthly partner invoices")
    pdf.drawString(60, page_height - 430, "- Handling Data required for partners and vendors")
    pdf.drawString(60, page_height - 450, "- Data verification and analysis")
    pdf.drawString(60, page_height - 470, "- Data correction")

    pdf.drawString(20, page_height - 510, "Associate(Operations) - Freo")
    pdf.drawString(40, page_height - 530, "Duration: Dec 2019 - Nov 2020")
    pdf.drawString(40, page_height - 550, "Description:")
    # Add relevant details about the role

    # Projects
    pdf.drawString(20, page_height - 590, "Projects:")
    pdf.drawString(40, page_height - 610, "Data Science Certification Lead - May 2020")
    pdf.drawString(60, page_height - 630, "Link: [GitHub - Anshuman Ojha](https://github.com/anshumanojha)")

    # Certifications
    pdf.drawString(20, page_height - 670, "Certifications:")
    pdf.drawString(40, page_height - 690, "Data Science Certification:")
    pdf.drawString(60, page_height - 710, "Certified by IBM in association with Coursera")
    pdf.drawString(60, page_height - 730, "Link: [IBM Data Science Certification](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)")

    pdf.drawString(40, page_height - 750, "Additional Certifications:")
    pdf.drawString(60, page_height - 770, "Python for Data Science and AI Development:")
    pdf.drawString(60, page_height - 790, "Lead")
    pdf.drawString(60, page_height - 810, "Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)")

    pdf.drawString(60, page_height - 830, "Databases and SQL with Python:")
    pdf.drawString(60, page_height - 850, "Lead")
    pdf.drawString(60, page_height - 870, "Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX)")

    pdf.drawString(60, page_height - 890, "Data Visualization with Python:")
    pdf.drawString(60, page_height - 910, "Lead")
    pdf.drawString(60, page_height - 930, "Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V)")

    pdf.save()

    # Set up download button
    st.download_button(
        "Download PDF",
        buffer.getvalue(),
        file_name="Anshuman_Ojha_Resume.pdf",
        key="pdf-download",
    )

# Set page layout
st.set_page_config(
    page_title="Anshuman Ojha's Resume",
    page_icon=":clipboard:",
    layout="wide",
)

# Anshuman's Resume
st.title("Anshuman Ojha's Resume")

# Generate PDF button at the top-right corner
if st.button("Generate PDF", key="generate-pdf-btn", help="Generate and download PDF"):
    generate_pdf()

# Personal Information
st.header("Personal Information")

# Location Input
location = st.write("Location:", "Bangalore")

# Display other personal information
st.write("Name: Anshuman")
st.write("Designation: Finops Analyst")
st.write("Contact: 877743144")
st.write("Email: anshumanojha94@gmail.com")

# Work Experience
st.header("Work Experience")

# Finops(Revenue&Recon Analyst) - Freo
st.subheader("Finops(Revenue&Recon Analyst) - Freo")
st.write("Duration: Dec 2020 - Present")
st.write("Description:")
st.write("- MIS")
st.write("- Revenue automation")
st.write("- Partner onboarding")
st.write("- Made dashboards to check repayment")
st.write("- Day-to-day repayment recon")
st.write("- Solving payments disputes")
st.write("- Development and verification of monthly partner invoices")
st.write("- Handling Data required for partners and vendors")
st.write("- Data verification and analysis")
st.write("- Data correction")

# Associate(operations) - Freo
st.subheader("Associate(Operations) - Freo")
st.write("Duration: Dec 2019 - Nov 2020")
st.write("Description:")
# Add relevant details about the role

# Projects
st.header("Projects")
st.subheader("Data Science Certification Lead - May 2020")
st.write("Link: [GitHub - Anshuman Ojha](https://github.com/anshumanojha)")

# Certifications
st.header("Certifications")
st.write("Data Science Certification:")
st.write("Certified by IBM in association with Coursera")
st.write("Link: [IBM Data Science Certification](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)")

# Additional Certifications
st.write("Python for Data Science and AI Development:")
st.write("Lead")
st.write("Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)")

st.write("Databases and SQL with Python:")
st.write("Lead")
st.write("Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX)")

st.write("Data Visualization with Python:")
st.write("Lead")
st.write("Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V)")
