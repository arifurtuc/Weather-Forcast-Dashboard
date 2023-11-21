# What is this project?

This app fetches weather forecasts for a specific location and displays temperature or sky conditions for the next few days based on user selection.

## Setup
1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Obtain an API key from OpenWeatherMap and save it in a `.env` file as `API_KEY=your_api_key`.
4. Run the app using `streamlit run main.py`.

## Usage
1. Enter the desired location in the provided input field.
2. Use the slider to select the number of forecast days.
3. Choose between viewing temperature or sky conditions for the forecasted days.
4. The app will display the selected weather information.

## Technologies Used
- Python
- Streamlit
- Plotly Express
- Requests

## File Structure
- `main.py`: Main application file containing the Streamlit app.
- `function.py`: Contains function to fetch weather data using API.
- `requirements.txt`: Contains the necessary Python libraries.
