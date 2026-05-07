import sqlite3

connection = sqlite3.connect("database/telemetry.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS robot_telemetry (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    robot_id TEXT,

    timestamp TEXT,

    temperature REAL,

    battery_level REAL,

    motor_speed INTEGER,

    cpu_usage REAL,

    position_x REAL,

    position_y REAL,

    status TEXT
)
""")

connection.commit()

connection.close()

print("Database and table created successfully.")