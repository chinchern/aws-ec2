
import streamlit as st

# Streamlit App
st.title("🚀 My First Streamlit App on AWS EC2")
st.write("Hello! This is a simple web app running on an EC2 instance.")

# Text input
user_input = st.text_input("Enter your name:", "")

# Button
if st.button("Greet Me"):
    st.write(f"👋 Hello, {user_input}!")

# Footer
st.write("---")
st.write("Deployed on AWS EC2 using Streamlit!")
