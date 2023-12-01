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

    # Portfolio Details
    st.title("Andrew's Developer Portfolio")
    st.markdown(
        "<p style='font-size: 20px;'>Software Developer | Experience: 2+ years</p>",
        unsafe_allow_html=True
    )
    # Add links to LinkedIn and GitHub profiles
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/andrew)")
    st.markdown("[GitHub Profile](https://github.com/andrew)")

    # Excel Formula Suggestor
    st.header('Excel Formula Suggestor')
    formula_type = st.selectbox("Select formula type:", ["ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "ROUND", "CEIL", "CONCATENATE", "VLOOKUP"])

    if formula_type == "ADD":
        cell1 = st.text_input("Enter first cell:")
        cell2 = st.text_input("Enter second cell:")
        formula_output = f"= {cell1} + {cell2}"
        st.success(f"Suggested Formula: {formula_output}")

    elif formula_type == "SUBTRACT":
        cell1 = st.text_input("Enter first cell:")
        cell2 = st.text_input("Enter second cell:")
        formula_output = f"= {cell1} - {cell2}"
        st.success(f"Suggested Formula: {formula_output}")

    elif formula_type == "MULTIPLY":
        cell1 = st.text_input("Enter first cell:")
        cell2 = st.text_input("Enter second cell:")
        formula_output = f"= {cell1} * {cell2}"
        st.success(f"Suggested Formula: {formula_output}")

    elif formula_type == "DIVIDE":
        cell1 = st.text_input("Enter numerator:")
        cell2 = st.text_input("Enter denominator:")
        formula_output = f"= {cell1} / {cell2}"
        st.success(f"Suggested Formula: {formula_output}")

    elif formula_type == "ROUND":
        cell = st.text_input("Enter cell:")
        digits = st.number_input("Enter the number of digits:")
        formula_output = f"= ROUND({cell}, {digits})"
        st.success(f"Suggested Formula: {formula_output}")

    elif formula_type == "CEIL":
        cell = st.text_input("Enter cell:")
        formula_output = f"= CEIL({cell})"
        st.success(f"Suggested Formula: {formula_output}")

    elif formula_type == "CONCATENATE":
        num_cells = st.number_input("Enter the number of cells to concatenate:")
        cells = [st.text_input(f"Enter cell {i + 1}:") for i in range(num_cells)]
        formula_output = "= CONCATENATE(" + ", ".join(cells) + ")"
        st.success(f"Suggested Formula: {formula_output}")

    elif formula_type == "VLOOKUP":
        lookup_value = st.text_input("Enter lookup value:")
        table_range = st.text_input("Enter table range:")
        col_index = st.number_input("Enter column index:")
        formula_output = f"= VLOOKUP({lookup_value}, {table_range}, {col_index}, FALSE)"
        st.success(f"Suggested Formula: {formula_output}")

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
