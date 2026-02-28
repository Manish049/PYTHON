import streamlit as st

# Task 1: Basic Streamlit App
st.title("Welcome to Streamlit!")

name = st.text_input("Enter your name:")

greet = st.button("Greet Me")

if greet:
    if name.strip():
        st.write(f"Hello, {name}!")
    else:
        st.write("Hello, !")
