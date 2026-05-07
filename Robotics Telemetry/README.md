🤖 Robotics Telemetry Monitoring System

A real-time robotics telemetry monitoring platform built using Python, Streamlit, SQLite, and Azure IoT-inspired analytics workflows.

This project simulates robotic telemetry data and provides live industrial monitoring dashboards for robotics and Industry 4.0 scenarios.

---

# 🚀 Features

- Real-time robotics telemetry simulation
- Live telemetry monitoring dashboard
- Temperature analytics
- Battery monitoring
- CPU usage tracking
- Motor speed analytics
- Robot status monitoring
- Historical telemetry storage
- Industrial IoT-style architecture

---

# 🏗️ Project Architecture

```text
Robot Simulator
        ↓
Telemetry Generator
        ↓
SQLite Database
        ↓
Streamlit Dashboard
        ↓
Real-Time Monitoring & Analytics
```

---

# 📂 Project Structure

```text
robotics-telemetry-azure/
│
├── simulator/
│   └── robot_simulator.py
│
├── dashboard/
│   └── dashboard.py
│
├── database/
│   ├── db_setup.py
│   └── telemetry.db
│
├── screenshots/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# 🛠️ Technologies Used

- Python
- Streamlit
- SQLite
- Pandas
- Plotly
- FastAPI
- MQTT
- Azure IoT Concepts
- Industry 4.0 Monitoring Concepts

---

# 📊 Telemetry Metrics

The simulator generates:

- Robot Temperature
- Battery Level
- CPU Usage
- Motor Speed
- Robot Position
- Robot Status

---

# ▶️ How to Run the Project

## 1. Clone Repository

```bash
git clone https://github.com/Vigneshkumarcvk/Robotics-Projects.git
```

---

## 2. Navigate to Project

```bash
cd Robotics-Projects/robotics-telemetry-azure
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\\Scripts\\Activate.ps1
```

---

## 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 5. Create Database

```bash
python database/db_setup.py
```

---

## 6. Run Robot Simulator

```bash
python simulator/robot_simulator.py
```

---

## 7. Run Dashboard

Open new terminal:

```bash
python -m streamlit run dashboard/dashboard.py
```

---

# 📸 Dashboard Screenshots

## Dashboard Overview

Add screenshot here.

---

## Telemetry Analytics

Add screenshot here.

---

# 📈 Future Enhancements

- MQTT Telemetry Streaming
- Azure IoT Hub Integration
- ROS2 Integration
- AI-Based Predictive Maintenance
- Real-Time Alerts
- Docker Deployment
- Kubernetes Deployment
- Cloud Telemetry Pipelines

---

# 🌐 Industry Use Cases

- Industrial Robotics Monitoring
- Smart Manufacturing
- Warehouse Robotics
- Industry 4.0 Analytics
- IoT Device Monitoring
- Robotics Telemetry Analytics

---

# 👨‍💻 Author

Vignesh Kumar

GitHub:
https://github.com/Vigneshkumarcvk

---

# ⭐ Project Highlights

- Real-time robotics telemetry generation
- Industrial monitoring dashboard
- Industry 4.0 inspired architecture
- Scalable telemetry analytics design
- Portfolio-ready robotics analytics project
