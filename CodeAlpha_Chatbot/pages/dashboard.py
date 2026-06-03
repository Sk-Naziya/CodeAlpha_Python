import streamlit as st
import sqlite3

st.title("🏠 Nexus AI Dashboard")

conn = sqlite3.connect("chatbot.db")
c = conn.cursor()

try:
    c.execute("SELECT COUNT(*) FROM users")
    users = c.fetchone()[0]
except:
    users = 0

try:
    c.execute("SELECT COUNT(*) FROM messages")
    messages = c.fetchone()[0]
except:
    messages = 0

try:
    c.execute("SELECT COUNT(*) FROM chats")
    chats = c.fetchone()[0]
except:
    chats = 0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Users", users)

with col2:
    st.metric("💬 Messages", messages)

with col3:
    st.metric("📂 Chats", chats)

st.divider()

st.subheader("🚀 Welcome to Nexus AI")

st.info("""
Features coming soon:

✅ Voice Assistant

✅ PDF Chat

✅ AI Image Studio

✅ User Memory

✅ Analytics

✅ Themes
""")

conn.close()