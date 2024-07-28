import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from PIL import Image

# Verbindung zur PostgreSQL-Datenbank herstellen
def get_data(query):
    database_url = st.secrets["database_url"]
    engine = create_engine(database_url)
    df = pd.read_sql(query, engine)
    return df

# Titel des Dashboards
st.title('Burger Tasting Hamburg')

# Daten abrufen und anzeigen
query_rater = "SELECT * FROM stg_burger_seed_burger.seeds_dim_rater;"
df_rater = get_data(query_rater)

query_store = "SELECT * FROM stg_burger_seed_burger.seeds_dim_burgerstore;"
df_store = get_data(query_store)

# Tabellen nebeneinander anzeigen
col1, col2 = st.columns(2)

with col1:
    st.header("Rater")
    st.dataframe(df_rater)

with col2:
    st.header("Burger Store")
    st.dataframe(df_store)

# Instagram-Icon hinzufügen
instagram_url = "https://www.instagram.com/burgertastingofficial?igsh=MXBsMnRldmN3bG95NQ=="
instagram_image = "instagram_icon.png"  # Pfad zum Instagram-Icon-Bild

# Lade das Bild herunter und speichere es
image = Image.open(instagram_image)

# Bild anzeigen und als Link setzen
st.markdown(f'<a href="{instagram_url}" target="_blank"><img src="data:image/png;base64,{st.image(image)}" width="50" height="50"></a>', unsafe_allow_html=True)
