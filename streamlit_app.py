import streamlit as st
import requests
import pandas as pd
import random

# Odd One Out Game Logic
class OddOneOutGame:
    def __init__(self):
        self.sets = [
            ['Python', 'JavaScript', 'Java', 'C#'],
            ['Frontend', 'Backend', 'Database', 'UI/UX'],
            ['Git', 'Docker', 'AWS', 'Kubernetes']
        ]
        self.correct_answers = ['C#', 'UI/UX', 'AWS']
        self.current_set = None
        self.answer = None

    def new_round(self):
        self.current_set = random.choice(self.sets)
        self.answer = None

# Streamlit App
def main():
    # Customizing the background color to dark green
    bg_color = '#006400'  # Dark Green
    st.markdown(f"""
        <style>
            .reportview-container {{
                background-color: {bg_color};
                color: #FFFFFF;  /* Text color */
            }}
        </style>
    """, unsafe_allow_html=True)

    st.title("Andrew's Developer Portfolio with Odd One Out Game")

    # Odd One Out Game
    game = OddOneOutGame()

    # Button to start a new round
    if st.button("Start New Round - Odd One Out Game"):
        game.new_round()

    # Display the current set for Odd One Out Game
    if game.current_set:
        st.write("Which one is the odd one out?")
        selected_option = st.radio("Select one:", game.current_set)

        # Check user's answer for Odd One Out Game
        game.answer = selected_option

        if game.answer in game.correct_answers:
            st.success("Correct! Well done! You can now view the portfolio.")
        else:
            st.error("Oops! That's not the odd one out. Try again!")

    # Rest of your existing code for the portfolio display
    st.title("Andrew's Developer Portfolio")
    st.markdown(
        "<p style='font-size: 20px;'>Software Developer | Experience: 2+ years</p>",
        unsafe_allow_html=True
    )
    # Add links to LinkedIn and GitHub profiles
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/andrew)")
    st.markdown("[GitHub Profile](https://github.com/andrew)")

    # Create bar chart for tools data
    tools_data = [9, 8, 7, 9]
    tools_labels = ['Python', 'JavaScript', 'Git', 'Docker']
    tools_chart = dict(zip(tools_labels, tools_data))

    # Create line chart for technology data
    technology_data = [8, 9, 7, 8, 9]
    technology_labels = ['React', 'Node.js', 'Spring Boot', 'AWS', 'Databases']
    technology_chart = dict(zip(technology_labels, technology_data))

    # Create pie chart for skills data
    skills_data = [60, 50, 70, 40, 55]
    skills_labels = ['Web Development', 'API Integration', 'Microservices', 'Cloud Computing', 'Database Management']
    skills_chart = dict(zip(skills_labels, skills_data))

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header('Tools Known')
        st.bar_chart(tools_chart, use_container_width=True)

    with col2:
        st.header('Technology Known')
        st.line_chart(technology_chart, use_container_width=True)

    with col3:
        st.header('Skills Proficiency')
        st.bar_chart(skills_chart, use_container_width=True)

    st.header('Projects')
    st.subheader('Project 1: E-commerce Website')
    st.write("Description: Developed a scalable e-commerce website with payment gateway integration.")

    st.subheader('Project 2: Chat Application')
    st.write("Description: Implemented a real-time chat application using WebSocket technology.")

if __name__ == "__main__":
    main()
