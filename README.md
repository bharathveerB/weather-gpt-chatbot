# Weather Chatbot 🌤️

A smart weather chatbot built with Streamlit that answers weather-related questions using real-time weather data from the Open-Meteo API.

## Features

- **Natural Language Processing**: Understands weather questions in natural language
- **Location-based Weather**: Get weather for any city or location worldwide
- **Current Weather & Forecasts**: Provides both current conditions and multi-day forecasts
- **Smart Intent Detection**: Only responds to weather-related questions
- **Interactive Chat Interface**: Clean, user-friendly Streamlit chat interface

## How It Works

1. **Question Analysis**: The bot analyzes your question to determine if it's weather-related
2. **Location Extraction**: Extracts location information from your question
3. **Weather Data Retrieval**: Fetches real-time weather data using Open-Meteo API
4. **Response Generation**: Formats and presents the weather information in a readable format

## Example Questions

### Current Weather
- "What's the weather in Paris?"
- "How's the temperature in Tokyo today?"
- "Is it raining in London?"

### Weather Forecasts
- "Show me the forecast for New York this week"
- "Weather forecast for Sydney"
- "Will it rain in Mumbai tomorrow?"

### Non-Weather Questions
The bot will politely decline to answer non-weather questions with: "I can answer only weather questions."

## Installation

1. Clone or download this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

Run the Streamlit app with:
```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## Project Structure

- `app.py` - Main Streamlit application with chat interface
- `weather_agent.py` - Weather data extraction and processing
- `requirements.txt` - Required Python packages
- `README.md` - This documentation file

## APIs Used

- **Open-Meteo API**: Free weather data API for current conditions and forecasts
- **Nominatim API**: Free geocoding service to convert location names to coordinates

## Deployment

This app can be deployed on various platforms:

### Streamlit Cloud
1. Push your code to GitHub
2. Connect your GitHub repository to Streamlit Cloud
3. Deploy with one click

### Other Platforms
- Heroku
- Railway
- Render
- Any platform that supports Python and Streamlit

## Technical Details

- **Framework**: Streamlit for web interface
- **Weather Data**: Open-Meteo API (no API key required)
- **Geocoding**: OpenStreetMap Nominatim API
- **Language Processing**: Custom keyword and pattern matching for intent detection

## License

This project is open source and available under the MIT License.
