# SkyCast - Weather App

SkyCast is a Flask-based web application that provides current weather information and a 5-day forecast for any city or your current location. Built for Tech Assessments 1 and 2, it integrates a SQLite database for CRUD operations, Google Maps for location visualization, and CSV export functionality.

## Features

### Tech Assessment 1
- **Current Weather**: Enter a city name to get real-time weather data (temperature, description, icon) using the OpenWeatherMap API.
- **5-Day Forecast**: Displays a 5-day weather forecast with daily details.
- **Geolocation**: Use your current location to fetch weather data with a single click.
- **Visual Appeal**: Weather icons enhance the user interface.

### Tech Assessment 2
- **CRUD Operations**:
  - **Create**: Add weather requests with optional start and end dates for planning.
  - **Read**: View a persistent history of all requests.
  - **Update**: Edit location names and refresh temperature data.
  - **Delete**: Remove entries from the history.
- **Date Range**: Input start and end dates (stored for planning; weather data is current due to API limits).
- **API Integration**: Links to Google Maps for each location’s coordinates.
- **Data Export**: Export request history as a CSV file.

## Prerequisites
- Python 3.8+
- An OpenWeatherMap API key (free tier)

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ahmed20455/SkyCast---Weather-App
   cd SkyCast---Weather-App
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
3. **Run the App**:
   ```bash
   python app.py
  - Open your browser to http://127.0.0.1:5000.
  
## Usage
- **Search Weather**: Enter a city name (e.g., "Tokyo") and optional dates, then click "Get Weather".
- **Use My Location**: Click "Use My Location" to fetch weather based on your geolocation.
- **Manage History**: Update or delete past requests from the history section.
- **Export Data**: Click "Export History as CSV" to download your request log.
- **View Map**: Click "View on Google Maps" to see the location on a map.

## Project Structure
- **app.py**: Main Flask application with routes and logic.
- **database.py**: SQLite database setup and CRUD functions.
- **index.html**: Main page template.
- **style.css**: Styling for the UI.
- **script.js**: JavaScript for geolocation functionality.
- **requirements.txt**: Python dependencies.

## Notes
- **Date Range**: Stored for planning purposes; weather data reflects current conditions and a 5-day forecast due to free API limitations.
- **Database**: Persists in weather.db and retains history across sessions.
