import sqlite3

DB = "weather.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS weather_requests (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 location TEXT NOT NULL,
                 temperature REAL,
                 start_date TEXT,
                 end_date TEXT,
                 local_time TEXT,
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                 owner TEXT NOT NULL)""")
    conn.commit()
    conn.close()

def add_weather_request(owner,location, temp, start_date=None, end_date=None, local_time=None):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO weather_requests (owner,location, temperature, start_date, end_date, local_time) VALUES (?, ?, ?, ?, ?, ?)",
              (owner, location, temp, start_date, end_date, local_time))
    conn.commit()
    conn.close()

def get_all_requests(owner):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, location, temperature, start_date, end_date, local_time, timestamp "
              "FROM weather_requests WHERE owner = ? ORDER BY id DESC LIMIT 50",(owner,))
    rows = c.fetchall()
    conn.close()
    return rows

def update_request(owner,id, new_location, new_temp=None):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    if new_temp is not None:
        c.execute("UPDATE weather_requests SET location = ?, temperature = ? WHERE id = ? AND owner= ?", (new_location, new_temp, id, owner))
    else:
        c.execute("UPDATE weather_requests SET location = ? WHERE id = ? AND owner = ?", (new_location, id,owner))
    conn.commit()
    conn.close()

def delete_request(owner,id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM weather_requests WHERE id = ? AND owner = ?", (id,owner))
    conn.commit()
    conn.close()
