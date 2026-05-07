import json
import random
import time
import sqlite3

from datetime import datetime

ROBOT_ID = "RB-101"


def generate_robot_telemetry():

    telemetry = {

        "robot_id": ROBOT_ID,

        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "temperature": round(random.uniform(40, 90), 2),

        "battery_level": round(random.uniform(20, 100), 2),

        "motor_speed": random.randint(800, 2000),

        "cpu_usage": round(random.uniform(10, 95), 2),

        "position_x": round(random.uniform(0, 100), 2),

        "position_y": round(random.uniform(0, 100), 2),

        "status": random.choice([
            "ACTIVE",
            "IDLE",
            "MOVING",
            "CHARGING",
            "ERROR"
        ])
    }

    return telemetry


def save_to_database(data):

    connection = sqlite3.connect("database/telemetry.db")

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO robot_telemetry (

        robot_id,
        timestamp,
        temperature,
        battery_level,
        motor_speed,
        cpu_usage,
        position_x,
        position_y,
        status

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        data["robot_id"],
        data["timestamp"],
        data["temperature"],
        data["battery_level"],
        data["motor_speed"],
        data["cpu_usage"],
        data["position_x"],
        data["position_y"],
        data["status"]

    ))

    connection.commit()

    connection.close()


def main():

    print("Robot Telemetry Simulator Started...\n")

    while True:

        telemetry_data = generate_robot_telemetry()

        print(json.dumps(telemetry_data, indent=4))

        save_to_database(telemetry_data)

        print("Telemetry stored in database.\n")

        time.sleep(3)


if __name__ == "__main__":
    main()