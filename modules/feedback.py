import streamlit as st

def show_result(success):
    if success:
        st.success("✅ Email sent successfully!")
    else:
        st.error("❌ Failed to send email.")