import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from io import BytesIO

# Text Variables
Header = '>>>This resume was generated entirely in Python. For full source code, view my portfolio.'
Name = 'EDDIE KIRKLAND'
Title = 'Data Science & Analytics'
Contact = 'Atlanta, GA\n404-XXX-XXXX\nwekrklndATgmailDOTcom\nlinkedin.com/in/ekirkland\ngithub.com/e-kirkland'
ProjectsHeader = 'PROJECTS/PUBLICATIONS'
ProjectOneTitle = 'Increasing Kaggle Revenue'
ProjectOneDesc = '- Published by Towards Data Science\n- Analyzed user survey to recommend the most profitable future revenue source\n- Cleaned/visualized data using pandas/matplotlib libraries in Python'
# (Other variable definitions remain unchanged)

# Set up the Streamlit app
st.set_page_config(
    page_title="Eddie Kirkland's Resume",
    page_icon=":clipboard:",
    layout="wide",
)

# Set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

# Create a plot
fig, ax = plt.subplots(figsize=(8.5, 11))

# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# Set background color
ax.set_facecolor('white')

# Remove axes
plt.axis('off')

# Add text
plt.annotate(Header, (.02, .98), weight='regular', fontsize=8, alpha=.6)
plt.annotate(Name, (.02, .94), weight='bold', fontsize=20)
# (Other text annotations remain unchanged)

# Display the plot using Streamlit
st.pyplot(fig)

# Create a BytesIO buffer for the PDF
pdf_buffer = BytesIO()

# Save the figure to the buffer
fig.savefig(pdf_buffer, format="pdf")

# Download the generated PDF
st.success("PDF generated successfully. You can now view and download the PDF.")
st.download_button(
    label="Download PDF",
    key="download-pdf-btn",
    on_click=None,  # Set to None or provide a callback function if needed
    args=(pdf_buffer,),
    file_name="Eddie_Kirkland_Resume.pdf",
    mime="application/pdf",
    help="Download the generated PDF",
)

# Close the buffer
pdf_buffer.close()
