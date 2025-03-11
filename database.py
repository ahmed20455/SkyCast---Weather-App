import sqlite3

def init_db():
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS weather_requests (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 location TEXT NOT NULL,
                 temperature REAL,
                 start_date TEXT,
                 end_date TEXT,
                 local_time TEXT,
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)""")
    conn.commit()
    conn.close()

def add_weather_request(location, temp, start_date=None, end_date=None, local_time=None):
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("INSERT INTO weather_requests (location, temperature, start_date, end_date, local_time) VALUES (?, ?, ?, ?, ?)",
              (location, temp, start_date, end_date, local_time))
    conn.commit()
    conn.close()

def get_all_requests():
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("SELECT * FROM weather_requests")
    rows = c.fetchall()
    conn.close()
    return rows

def update_request(id, new_location, new_temp=None):
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    if new_temp is not None:
        c.execute("UPDATE weather_requests SET location = ?, temperature = ? WHERE id = ?", (new_location, new_temp, id))
    else:
        c.execute("UPDATE weather_requests SET location = ? WHERE id = ?", (new_location, id))
    conn.commit()
    conn.close()

def delete_request(id):
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("DELETE FROM weather_requests WHERE id = ?", (id,))
    conn.commit()
    conn.close()
