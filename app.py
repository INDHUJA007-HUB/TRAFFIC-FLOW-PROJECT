import streamlit as st
import pandas as pd
import pydeck as pdk
import altair as alt
from fetch_data import get_traffic_data
from upload_to_gcp import upload_file_to_gcp
from config import BUCKET_NAME

st.set_page_config(layout="wide")
st.title("🚦 Real-Time Traffic Flow Visualization")

# Fetch traffic data and upload to GCP
df = get_traffic_data()
upload_file_to_gcp(BUCKET_NAME, "traffic_data.csv", "latest_traffic_data.csv")

# Heatmap
st.subheader("📍 Heatmap of Traffic Density")
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=40.71, longitude=-74.00, zoom=11, pitch=50),
    layers=[pdk.Layer(
        "HeatmapLayer",
        data=df,
        get_position="[longitude, latitude]",
        get_weight="vehicle_count",
        radiusPixels=60,
    )]
))

# Line Plot
st.subheader("📈 Traffic Volume Over Time")
line_chart = alt.Chart(df).mark_line().encode(
    x='timestamp:T',
    y='vehicle_count:Q'
)
st.altair_chart(line_chart, use_container_width=True)

# Scatter Plot
st.subheader("⚫ Speed vs. Time")
scatter_chart = alt.Chart(df).mark_circle(size=60).encode(
    x='timestamp:T',
    y='speed:Q',
    tooltip=['latitude', 'longitude', 'speed']
)
st.altair_chart(scatter_chart, use_container_width=True)
