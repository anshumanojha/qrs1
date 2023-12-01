import streamlit as st
import sqlite3

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

    # Rest of your existing code for the portfolio display
    st.title("Andrew's Developer Portfolio")
    st.markdown(
        "<p style='font-size: 20px;'>Software Developer | Experience: 2+ years</p>",
        unsafe_allow_html=True
    )
    # Add links to LinkedIn and GitHub profiles
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/andrew)")
    st.markdown("[GitHub Profile](https://github.com/andrew)")

    # SQL Query Submission
    st.header('SQL Query Submission')
    sql_code = st.text_area("Enter your SQL code:")

    # Button to submit SQL query
    if st.button("Submit Query"):
        try:
            # Connect to an in-memory SQLite database
            conn = sqlite3.connect(':memory:')
            cursor = conn.cursor()

            # Execute the SQL query
            cursor.execute(sql_code)

            # Fetch and display the result
            result = cursor.fetchall()
            st.success("Query executed successfully!")
            st.table(result)

            # Close the database connection
            conn.close()
        except Exception as e:
            st.error(f"Error executing SQL query: {e}")

if __name__ == "__main__":
    main()
