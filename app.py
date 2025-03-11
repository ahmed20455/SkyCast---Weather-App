from flask import Flask, render_template, request, jsonify, redirect, url_for, Response, session
import requests
import os
from dotenv import load_dotenv
from database import init_db, add_weather_request, get_all_requests, update_request, delete_request
from datetime import datetime, timedelta
import pytz
from io import StringIO
import csv

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for session
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/"

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = session.pop('weather_data', None)
    forecast_data = session.pop('forecast_data', None)
    local_time = session.pop('local_time', None)  # Already a string
    map_link = session.pop('map_link', None)

    if request.method == "POST":
        location = request.form.get("location")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        if location:
            weather_url = f"{BASE_URL}weather?q={location}&appid={API_KEY}&units=metric"
            response = requests.get(weather_url)
            if response.status_code == 200:
                weather_data = response.json()
                utc_time = datetime.utcfromtimestamp(weather_data["dt"])
                timezone_offset = weather_data["timezone"]
                local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("UTC")).replace(tzinfo=None) + timedelta(seconds=timezone_offset)
                forecast_url = f"{BASE_URL}forecast?q={location}&appid={API_KEY}&units=metric"
                forecast_response = requests.get(forecast_url)
                if forecast_response.status_code == 200:
                    forecast_data = forecast_response.json()["list"][::8]
                lat = weather_data["coord"]["lat"]
                lon = weather_data["coord"]["lon"]
                map_link = f"https://www.google.com/maps?q={lat},{lon}"
                if start_date and end_date:
                    try:
                        start = datetime.strptime(start_date, "%Y-%m-%d")
                        end = datetime.strptime(end_date, "%Y-%m-%d")
                        if start > end:
                            return "Error: Start date must be before end date", 400
                    except ValueError:
                        return "Error: Invalid date format (use YYYY-MM-DD)", 400
                add_weather_request(location, weather_data["main"]["temp"], start_date, end_date, local_time.strftime('%Y-%m-%d %H:%M'))
                session['weather_data'] = weather_data
                session['forecast_data'] = forecast_data
                session['local_time'] = local_time.strftime('%Y-%m-%d %H:%M')  # Consistent string
                session['map_link'] = map_link
                return redirect(url_for("index"))
            else:
                return f"Error: Could not find weather for {location}", 400
    
    requests_history = get_all_requests()
    return render_template("index.html", weather=weather_data, forecast=forecast_data, history=requests_history, local_time=local_time, map_link=map_link)

@app.route("/current_location", methods=["POST"])
def current_location():
    lat = request.json["lat"]
    lon = request.json["lon"]
    weather_url = f"{BASE_URL}weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(weather_url)
    if response.status_code == 200:
        weather_data = response.json()
        utc_time = datetime.utcfromtimestamp(weather_data["dt"])
        timezone_offset = weather_data["timezone"]
        local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("UTC")).replace(tzinfo=None) + timedelta(seconds=timezone_offset)
        forecast_url = f"{BASE_URL}forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"  # Fixed to use lat/lon
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()["list"][::8]
        add_weather_request(f"Lat:{lat},Lon:{lon}", weather_data["main"]["temp"], None, None, local_time.strftime('%Y-%m-%d %H:%M'))
        session['weather_data'] = weather_data
        session['forecast_data'] = forecast_data
        session['local_time'] = local_time.strftime('%Y-%m-%d %H:%M')
        session['map_link'] = f"https://www.google.com/maps?q={lat},{lon}"
        return redirect(url_for("index"))
    return jsonify({"error": "Unable to fetch weather"}), 400

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    new_location = request.form.get("new_location")
    if not new_location.strip():
        return "Error: Location cannot be empty", 400
    if new_location:
        weather_url = f"{BASE_URL}weather?q={new_location}&appid={API_KEY}&units=metric"
        response = requests.get(weather_url)
        if response.status_code == 200:
            weather_data = response.json()
            new_temp = weather_data["main"]["temp"]
            update_request(id, new_location, new_temp)
        else:
            return f"Error: Could not find weather for {new_location}", 400
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    delete_request(id)
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/export/csv")
def export_csv():
    history = get_all_requests()
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Location", "Temperature", "Start Date", "End Date", "Local Time", "Requested"])
    for row in history:
        writer.writerow(row)
    return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=weather_history.csv"})

if __name__ == "__main__":
    app.run(debug=True)
