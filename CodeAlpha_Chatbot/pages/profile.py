import streamlit as st

st.title("👤 Profile")

if "user" in st.session_state:

    st.success(f"Logged in as: {st.session_state.user}")

    st.write("Account Type: User")

else:

    st.warning("Please login first.")