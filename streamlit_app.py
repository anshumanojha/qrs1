import streamlit as st
import requests
import pandas as pd
import random

# URL Shortener Function
def get_smaller_urls(search_query):
    url = "https://google.com/search?q=" + search_query
    request_result = requests.get(url)
    search_results = request_result.text
    start_index = search_results.find("https://www.zomato.com/")
    end_index = search_results.find("&", start_index)
    smaller_url = search_results[start_index:end_index]
    return smaller_url

# Odd One Out Game Logic
class OddOneOutGame:
    def __init__(self):
        self.sets = [
            ['Apple', 'Banana', 'Orange', 'Carrot'],
            ['Dog', 'Cat', 'Fish', 'Bird'],
            ['Red', 'Blue', 'Green', 'Chair']
        ]
        self.correct_answers = ['Carrot', 'Fish', 'Chair']
        self.current_set = None
        self.answer = None

    def new_round(self):
        self.current_set = random.choice(self.sets)
        self.answer = None

# Streamlit App
def main():
    st.title("Anshuman's Portfolio with Odd One Out Game")

    # URL Shortener
    st.header('URL Shortener')
    search_query = st.text_input("Enter a search query:")
    if st.button("Shorten URL"):
        smaller_url = get_smaller_urls(search_query)
        st.success(f"Shortened URL: {smaller_url}")

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
    st.title("Anshuman's Portfolio")
    st.markdown(
        "<p style='font-size: 20px; color: #555555;'>Finops & Revenue Analyst | Experience: 3+ years</p>",
        unsafe_allow_html=True
    )
    # Add links to LinkedIn and GitHub profiles
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/anshuman-ojha-34093885/)")
    st.markdown("[GitHub - Python Projects Automated Google Search](https://github.com/anshumanojha/pythonprojects/blob/master/Googlewebsearchauto.ipynb)")
    st.markdown("[GitHub - Python Projects Automated Location Automate](https://github.com/anshumanojha/pythonprojects/blob/master/browser.py)")

    # Create bar chart for tools data
    tools_data = [10, 10, 8, 9, 7]
    tools_labels = ['MYSQL', 'Python', 'Dashboard Development', 'Power Bi']
    tools_chart = dict(zip(tools_labels, tools_data))

    # Create line chart for technology data
    technology_data = [9, 10, 10, 8, 7, 10]
    technology_labels = ['Superset', 'SQL', 'Python', 'AWS', 'AI', 'ML']
    technology_chart = dict(zip(technology_labels, technology_data))

    # Example of finding errors in SQL code
    st.header('Example: Finding Errors in SQL Code')
    sql_code = st.text_area("Enter your SQL code:")
    
    if st.button("Find Errors"):
        # Replace this part with your actual logic for finding errors in SQL code
        # For now, let's assume any code containing the word 'error' is incorrect
        if 'error' in sql_code.lower():
            st.error("Error found in SQL code. Please review and correct.")
        else:
            st.success("No errors found in SQL code. Looks good!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header('Tools Known')
        st.bar_chart(tools_chart, use_container_width=True)

    with col2:
        st.header('Technology Known')
        st.line_chart(technology_chart, use_container_width=True)

    with col3:
        st.header('Skills Proficiency')
        st.write("Example: Ability to find errors in SQL code")

    st.header('Certifications')
    st.markdown(
        "<ul style='font-size: 18px; color: #333333; list-style-type: square;'>"
        "<li><a href='https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V' target='_blank'>IBM-Data Analysis certificate</a></li>"
        "<li><a href='https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX' target='_blank'>IBM-Data Visualization with Python</a></li>"
        "<li><a href='https://www.coursera.org/account/accomplishments/certificate/ST57AP42DMXS' target='_blank'>Databases and SQL for Data Science with Python</a></li>"
        "<li><a href='https://www.coursera.org/account/accomplishments/certificate/PWQGKGYMMMQU' target='_blank'>Machine Learning with Python</a></li>"
        "<li><a href='https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV' target='_blank'>Python for Data Science, AI & Development</a></li>"
        "<li><a href='https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9' target='_blank'>IBM Data Science Specialization</a></li>"
        "</ul>",
        unsafe_allow_html=True
    )
    # Map section
    st.header('Location - Bengaluru')
    # Create a DataFrame with your location data
    location_df = pd.DataFrame({'LATITUDE': [12.9716], 'LONGITUDE': [77.5946]})
    st.map(location_df, zoom=10)

    # Project 2: Weather App
    st.subheader('Project 2: Weather App')
    st.write("Description: A Python script to fetch weather information for a given city.")

    def get_weather(city):
        api_key = "4cb3a44e7cab1adb19e17ecc44c6da11"  # Replace with your OpenWeatherMap API key

        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if data["cod"] == 200:
                city_name = data["name"]
                temperature = data["main"]["temp"]
                weather_desc = data["weather"][0]["description"]

                weather_info = f"City: {city_name}\nTemperature: {temperature}°C\nWeather: {weather_desc}"
                st.info(weather_info)
            else:
                st.error(f"Failed to fetch weather data: {data['message']}")

        except Exception as e:
            st.error(f"Failed to fetch weather data: {e}")

    city = st.text_input("Enter city name:")
    if st.button("Get Weather"):
        get_weather(city)

if __name__ == "__main__":
    main()
