import streamlit as st
import plotly.express as px

# Streamlit app title and input widgets
st.title("Weather Forecast for Upcoming Days")
location = st.text_input("Location")
forecast_duration = st.slider("Forecast Duration (Days)",
                              min_value=1,
                              max_value=5,
                              help="Select the number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {forecast_duration} days in {location}")


def generate_weather_data(days):
    # Dummy weather data for demonstration purposes
    dates = ["2023-25-10", "2023-26-10", "2023-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * temp for temp in temperatures]
    return dates, temperatures


# Generate weather data for plotting
forecast_dates, forecast_temperatures = generate_weather_data(forecast_duration)

# Create a Plotly line chart based on the selected data
weather_chart = px.line(x=forecast_dates,
                        y=forecast_temperatures,
                        labels={"x": "Date", "y": "Temperature (C)"})

# Display the Plotly chart using Streamlit
st.plotly_chart(weather_chart)
