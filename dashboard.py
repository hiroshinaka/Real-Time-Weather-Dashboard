import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL Connection using SQLAlchemy
engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/postgres")

st.title("Real-Time Weather Dashboard")

# Function to fetch data
@st.cache_data(ttl=5)  # Cache for 5 seconds
def get_weather_data():
    return pd.read_sql("SELECT * FROM weather ORDER BY timestamp DESC LIMIT 10", engine)

# Display data
st.write("Latest Weather Data:")
df = get_weather_data()
st.write(df)

# Add refresh button
if st.button("Refresh"):
    st.rerun()
