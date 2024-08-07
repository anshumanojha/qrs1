import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO

dynamic_bg = """
<style>
@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}
body:before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    height: 100vh;
    width: 100vw;
    z-index: -1;
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

/* Override Streamlit's default background color for the root element */
.css-18e3th9 {
    background-color: transparent !important;
}

/* Override Streamlit's default background color for the main content area */
.stApp {
    background-color: transparent !important;
}
</style>
"""

# Inject custom CSS with markdown
st.markdown(dynamic_bg, unsafe_allow_html=True)

# Text Variables
Header = '>>>This resume was generated entirely in Python. For the full source code, view my portfolio.'
Name = 'Anshuman Ojha'
Title = 'Finops and Revenue Analyst'
Contact = 'Bengaluru, GA\n404-XXX-XXXX\nwekrklndATgmailDOTcom\nlinkedin.com/in/ekirkland\ngithub.com/e-kirkland'
ProjectsHeader = 'PROJECTS/PUBLICATIONS'
ProjectOneTitle = 'Increasing Kaggle Revenue'
ProjectOneDesc = '- Published by Towards Data Science\n- Analyzed user survey to recommend the most profitable future revenue source\n- Cleaned/visualized data using pandas/matplotlib libraries in Python'
ProjectTwoTitle = 'NYC School Data Cleaning & Analysis'
ProjectTwoDesc = '- Cleaned and combined several tables using pandas library in Python\n- Used PDE and visualization to determine correlations for future study'
ProjectThreeTitle = 'Pandas Cleaning and Visualization'
ProjectThreeDesc = '- Cleaned data for analysis using pandas library in Python\n- Used pandas and matplotlib to explore which cars hold the most value over time'
Portfolio = 'Portfolio: rebrand.ly/ekirkland'
WorkHeader = 'EXPERIENCE'
WorkOneTitle = 'Example Company / Example Position'
WorkOneTime = '8/2013-Present'
WorkOneDesc = '- Raised $350k in startup funds, recruited/organized launch team\n- Coordinated branding and communication strategy for organization\n- Led a team of 80 volunteer and staff leaders'
WorkTwoTitle = 'Second Company / Second Position'
WorkTwoTime = '2/2007-8/2013'
WorkTwoDesc = '- Led a team of over 100 full-time and contract staff\n- Helped create branding and messaging for weekly content\n- Created/directed musical elements at weekly events for up to 10,000 people'
WorkThreeTitle = 'Third Company / Third Position'
WorkThreeTime = '6/2004-2/2007'
WorkThreeDesc = '- Planned/Coordinated Toronto arena event and South Africa speaking tour\n- Oversaw research for published products'
EduHeader = 'EDUCATION'
EduOneTitle = 'Example University, Bachelor of Business Administration'
EduOneTime = '2000-2004'
EduOneDesc = '- Major: Management, Minor: Statistics'
EduTwoTitle = 'Example University, Master of Arts'
EduTwoTime = '2013-2017'
SkillsHeader = 'Skills'
SkillsDesc = '- Python\n- Pandas\n- NumPy\n- Data Visualization\n- Data Cleaning\n- Command Line\n- Git and Version Control\n- SQL\n- APIs\n- Probability/Statistics\n- Data Manipulation\n- Excel'
ExtrasTitle = 'DataQuest\nData Scientist Path'
ExtrasDesc = 'Learned popular data science\nlanguages, data cleaning and\nmanipulation, machine learning \nand statistical analysis'
CodeTitle = 'View Portfolio'

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
plt.annotate(Title, (.02, .91), weight='regular', fontsize=14)
plt.annotate(Contact, (.7, .906), weight='regular', fontsize=8, color='#ffffff')
plt.annotate(ProjectsHeader, (.02, .86), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(ProjectOneTitle, (.02, .832), weight='bold', fontsize=10)
plt.annotate(ProjectOneDesc, (.04, .78), weight='regular', fontsize=9)
plt.annotate(ProjectTwoTitle, (.02, .745), weight='bold', fontsize=10)
plt.annotate(ProjectTwoDesc, (.04, .71), weight='regular', fontsize=9)
plt.annotate(ProjectThreeTitle, (.02, .672), weight='bold', fontsize=10)
plt.annotate(ProjectThreeDesc, (.04, .638), weight='regular', fontsize=9)
plt.annotate(Portfolio, (.02, .6), weight='bold', fontsize=10)
plt.annotate(WorkHeader, (.02, .54), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(WorkOneTitle, (.02, .508), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02, .493), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.04, .445), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02, .4), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.02, .385), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.04, .337), weight='regular', fontsize=9)
plt.annotate(WorkThreeTitle, (.02, .295), weight='bold', fontsize=10)
plt.annotate(WorkThreeTime, (.02, .28), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkThreeDesc, (.04, .247), weight='regular', fontsize=9)
plt.annotate(EduHeader, (.02, .185), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(EduOneTitle, (.02, .155), weight='bold', fontsize=10)
plt.annotate(EduOneTime, (.02, .14), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduOneDesc, (.04, .125), weight='regular', fontsize=9)
plt.annotate(EduTwoTitle, (.02, .08), weight='bold', fontsize=10)
plt.annotate(EduTwoTime, (.02, .065), weight='regular', fontsize=9, alpha=.6)
plt.annotate(SkillsHeader, (.7, .8), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7, .56), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(ExtrasTitle, (.7, .43), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(ExtrasDesc, (.7, .345), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(CodeTitle, (.7, .2), weight='bold', fontsize=10, color='#ffffff')

# Display the plot using Streamlit
st.pyplot(fig)
