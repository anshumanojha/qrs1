import streamlit as st
import sqlite3
import re

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
        self.current_set = self.sets.pop(0) if self.sets else None
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

    # Portfolio Details
    st.title("Andrew's Developer Portfolio")
    st.markdown(
        "<p style='font-size: 20px;'>Software Developer | Experience: 2+ years</p>",
        unsafe_allow_html=True
    )
    # Add links to LinkedIn and GitHub profiles
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/andrew)")
    st.markdown("[GitHub Profile](https://github.com/andrew)")

    # Text-based Excel Formula Suggestor
    st.header('Project-1-Text-based Excel Formula Suggestor')
    excel_query = st.text_input("Describe the operation you want (e.g., add two cells):")

    if st.button("Get Suggested Formula"):
        try:
            # Extract keywords from the user's input
            keywords = re.findall(r'\b\w+\b', excel_query.lower())

            # Map keywords to Excel functions
            excel_functions = {
                'add': '+',
                'subtract': '-',
                'multiply': '*',
                'divide': '/',
                'round': 'ROUND',
                'ceil': 'CEIL',
                'concatenate': 'CONCATENATE',
                'vlookup': 'VLOOKUP'
            }

            # Generate the suggested Excel formula
            suggested_formula = ' '.join([excel_functions[keyword] if keyword in excel_functions else keyword for keyword in keywords])
            st.success(f"Suggested Formula: {suggested_formula}")

        except Exception as e:
            st.error(f"Error generating suggested formula: {e}")

    # SQL Query Submission
    st.header('Project2-SQL syntax checker')
    sql_code = st.text_area("Enter your SQL code:")

    # Button to submit SQL query
    if st.button("Submit Query"):
        try:
            # Connect to an in-memory SQLite database
            conn = sqlite3.connect(':memory:')
            cursor = conn.cursor()

            # Execute the SQL query
            result = cursor.execute(sql_code)

            # Fetch and display the result
            if result is not None:
                result = result.fetchall()
                st.success("Query executed successfully!")
                st.table(result)
            else:
                st.warning("Query executed successfully, but no results to display.")

            # Close the database connection
            conn.close()
        except sqlite3.Error as e:
            error_message = str(e)
            if "no such table" in error_message.lower():
                st.warning("Ignoring table-related errors. Focus on syntax and symbols.")
            else:
                st.error(f"Error executing SQL query: {error_message}")

if __name__ == "__main__":
    main()
