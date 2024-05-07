import streamlit as st
import pandas as pd
from send_email import send_email

# Build the topics list
csvfile = 'topics.csv'
df = pd.read_csv(csvfile)

topics = []
for index, row in df.iterrows():
    topic = row['topic']
    topics.append(topic)

# Display the page
st.set_page_config(layout="wide")

with st.form(key='Contact Us'):
    user_email = st.text_input("Your email address")

    user_topic = st.selectbox("What topic do you want to discuss?", options=topics, placeholder=topics[0])

    user_message = st.text_area("Text")

    submit = st.form_submit_button()

    if submit:
        if not user_email:
            st.write("Please enter your email address")
        elif not user_topic:
            st.write("Please select a topic")
        elif not user_message:
            st.write("Please enter your message")
        else:
            # Note: Subject must be 1st line of message AND must be followed by a CR
            eml_message = f"""\
Subject: {user_topic}  [from: {user_email}]

{user_message}
From: {user_email}
"""
            send_email(eml_message)

            st.success('Email sent successfully!', icon="✅")
