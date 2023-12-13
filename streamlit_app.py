import streamlit as st
import matplotlib.pyplot as plt

# Text Variables
Header = '>>>This resume was generated entirely in Python. For the full source code, view my portfolio.'
Name = 'Anshuman Ojha'
Title = 'Finops Analyst'
Contact = 'Bangalore\n877743144\nanshumanojha94@gmail.com\nlinkedin.com/in/anshumanojha\ngithub.com/anshumanojha'
ProjectsHeader = 'PROJECTS/PUBLICATIONS'
ProjectOneTitle = 'Finops(Revenue&Recon Analyst) - Freo'
ProjectOneDesc = '- MIS\n- Revenue automation\n- Partner onboarding\n- Made dashboards to check repayment\n- Day-to-day repayment recon\n- Solving payments disputes\n- Development and verification of monthly partner invoices\n- Handling Data required for partners and vendors\n- Data verification and analysis\n- Data correction'
ProjectTwoTitle = 'Associate(Operations) - Freo'
ProjectTwoDesc = '- Description: Add relevant details about the role'
CertificationsHeader = 'CERTIFICATIONS'
CertificationOneTitle = 'Data Science Certification'
CertificationOneDesc = 'Certified by IBM in association with Coursera\nLink: [IBM Data Science Certification](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)'
CertificationTwoTitle = 'Python for Data Science and AI Development'
CertificationTwoDesc = 'Lead\nLink: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)'
CertificationThreeTitle = 'Databases and SQL with Python'
CertificationThreeDesc = 'Lead\nLink: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX)'
CertificationFourTitle = 'Data Visualization with Python'
CertificationFourDesc = 'Lead\nLink: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V)'

# Set page layout
st.set_page_config(
    page_title="Anshuman Ojha's Resume",
    page_icon=":clipboard:",
    layout="wide",
)

# Anshuman's Resume
st.title("Anshuman Ojha's Resume")

# Personal Information
st.header("Personal Information")

# Location Input
location = st.write("Location:", "Bangalore")

# Display other personal information
st.write(f"Name: {Name}")
st.write("Designation: Finops Analyst")
st.write("Contact: 877743144")
st.write("Email: anshumanojha94@gmail.com")

# Work Experience
st.header("Work Experience")

# Finops(Revenue&Recon Analyst) - Freo
st.subheader("Finops(Revenue&Recon Analyst) - Freo")
st.write("Duration: Dec 2020 - Present")
st.write("Description:")
st.write(ProjectOneDesc)

# Associate(Operations) - Freo
st.subheader("Associate(Operations) - Freo")
st.write("Duration: Dec 2019 - Nov 2020")
st.write("Description:")
st.write(ProjectTwoDesc)

# Projects
st.header(ProjectsHeader)
st.subheader(ProjectOneTitle)
st.write("Link: [GitHub - Anshuman Ojha](https://github.com/anshumanojha)")

# Certifications
st.header(CertificationsHeader)
st.write(f"{CertificationOneTitle}: {CertificationOneDesc}")
st.write(f"{CertificationTwoTitle}: {CertificationTwoDesc}")
st.write(f"{CertificationThreeTitle}: {CertificationThreeDesc}")
st.write(f"{CertificationFourTitle}: {CertificationFourDesc}")

# Generate PDF button at the top-right corner
if st.button("Generate PDF", key="generate-pdf-btn", help="Generate and download PDF"):
    # Create a PDF object
    pdf = plt.figure(figsize=(8.5, 11))
    plt.axis('off')  # Turn off axis
    plt.annotate(Header, (.02, .98), weight='regular', fontsize=8, alpha=.6)
    plt.annotate(Name, (.02, .94), weight='bold', fontsize=20)
    plt.annotate(Title, (.02, .91), weight='regular', fontsize=14)
    plt.annotate(Contact, (.7, .906), weight='regular', fontsize=8, color='#ffffff')
    plt.annotate(ProjectsHeader, (.02, .86), weight='bold', fontsize=10, color='#58C1B2')
    plt.annotate(ProjectOneTitle, (.02, .832), weight='bold', fontsize=10)
    plt.annotate(ProjectOneDesc, (.04, .78), weight='regular', fontsize=9)

    # Save the figure as a PDF
    pdf.savefig('Anshuman_Ojha_Resume.pdf', bbox_inches='tight')
    st.success("PDF generated successfully. You can now view and download the PDF.")
