import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import env
import os
# Verbindung zur PostgreSQL-Datenbank herstellen
def get_data():
    database_url = st.secrets["database_url"]
    engine = create_engine(database_url)
    query = "SELECT * FROM stg_burger_mart.dim_date"
    df = pd.read_sql(query, engine)
    return df

# Titel des Dashboards
st.title('Mein Streamlit Dashboard')

# Daten abrufen und anzeigen
df = get_data()
st.write(df)