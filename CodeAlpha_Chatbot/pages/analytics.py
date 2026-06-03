import streamlit as st
import sqlite3
import pandas as pd

st.title("📊 Analytics")

conn = sqlite3.connect("chatbot.db")

try:

    df = pd.read_sql_query(
        "SELECT * FROM messages",
        conn
    )

    st.dataframe(df)

except:

    st.warning("No analytics available yet.")

conn.close()