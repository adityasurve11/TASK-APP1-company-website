import streamlit as st
from sendEMAIL import sendEMAIL
import pandas

df = pandas.read_csv("topics.csv")

st.header("Contact US")

with st.form(key="email_form"):
    user_email = st.text_input("Your email Address")
    option = st.selectbox(
        'What topic do you want to discuss?',
        df["topic"])
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
topic {option}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        sendEMAIL(message)
        st.info("Your email was sent successfullyyyy")