Real-Time-Weather-Dashboard
----
**Summary**
Creates a dashboard from data pulled of Openweather API, processes and stores the data in a local PostgresSQL database, and visualize the data using Streamlit Dashboard.

**Project Architecture**
Openweathermap API => Kafka -> Kafka Consumer -> PostgresSQL -> Streamlit Dashboard

    Data Ingestion:

        OpenWeatherMap API (free tier for real-time weather data).

        Apache Kafka (local setup with Docker).

    Data Processing:

        Python (for data transformation and analysis).

    Storage:

        PostgreSQL (local setup with Docker).

    Visualization:

        Streamlit (free and open-source dashboard).

    Orchestration:

        Docker Compose (to run Kafka, PostgreSQL, and the dashboard locally).
