import streamlit as st
import plotly.express as px
from function import generate_weather_data

# Streamlit app title and input widgets
st.title("Weather Forecast for Upcoming Days")
location = st.text_input("Location")
forecast_duration = st.slider("Forecast Duration (Days)",
                              min_value=1,
                              max_value=5,
                              help="Select the number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {forecast_duration} days in {location}")

if location:
    # Fetch weather data for plotting
    filtered_data = generate_weather_data(location, forecast_duration)

    if option == "Temperature":
        forecast_temperatures = [dict["main"]["temp"] for dict in filtered_data]
        forecast_dates = [dict["dt_txt"] for dict in filtered_data]

        # Create a Plotly line chart based on the selected data
        weather_chart = px.line(x=forecast_dates,
                                y=forecast_temperatures,
                                labels={"x": "Date", "y": "Temperature (C)"})
        # Display the Plotly chart using Streamlit
        st.plotly_chart(weather_chart)

    if option == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
        st.image()

