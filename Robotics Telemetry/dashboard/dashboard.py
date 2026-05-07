import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Robotics Telemetry Dashboard",
    layout="wide"
)

st.title("🤖 Robotics Telemetry Monitoring Dashboard")

# Database Connection
connection = sqlite3.connect("database/telemetry.db")

# Load Data
query = "SELECT * FROM robot_telemetry ORDER BY id DESC LIMIT 100"

df = pd.read_sql_query(query, connection)

connection.close()

# Check Data
if df.empty:
    st.warning("No telemetry data available.")
    st.stop()

# Latest Telemetry
latest = df.iloc[0]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Temperature",
    f"{latest['temperature']} °C"
)

col2.metric(
    "Battery",
    f"{latest['battery_level']} %"
)

col3.metric(
    "Motor Speed",
    f"{latest['motor_speed']} RPM"
)

col4.metric(
    "CPU Usage",
    f"{latest['cpu_usage']} %"
)

st.divider()

# Robot Status
st.subheader("Robot Status")

status = latest["status"]

if status == "ACTIVE":
    st.success(f"Robot Status: {status}")

elif status == "ERROR":
    st.error(f"Robot Status: {status}")

elif status == "CHARGING":
    st.warning(f"Robot Status: {status}")

else:
    st.info(f"Robot Status: {status}")

# Charts
st.subheader("Telemetry Analytics")

chart_col1, chart_col2 = st.columns(2)

# Temperature Chart
with chart_col1:

    fig_temp = px.line(
        df,
        x="timestamp",
        y="temperature",
        title="Temperature Trend"
    )

    st.plotly_chart(fig_temp, use_container_width=True)

# Battery Chart
with chart_col2:

    fig_battery = px.line(
        df,
        x="timestamp",
        y="battery_level",
        title="Battery Level Trend"
    )

    st.plotly_chart(fig_battery, use_container_width=True)

# Motor Speed Chart
fig_motor = px.line(
    df,
    x="timestamp",
    y="motor_speed",
    title="Motor Speed Analytics"
)

st.plotly_chart(fig_motor, use_container_width=True)

# Telemetry Table
st.subheader("Recent Telemetry Data")

st.dataframe(df)