import streamlit as st  
import pandas as pd  
import numpy as np  

# Set a title for the app
st.title("🎉 Welcome to My First Streamlit App!")  

# Intro message
st.write("Hey there! 👋 This is a simple web app built using Streamlit. Let's explore some cool features together!")

# User input section
st.subheader("👤 Tell me about yourself")  
name = st.text_input("What's your name?")
if name:
    st.write(f"Nice to meet you, {name}! 😊 Hope you're having a great day!")

# Number slider
st.subheader("🎂 Age Selector")  
age = st.slider("How old are you?", 1, 100, 25)
st.write(f"Wow! You're {age} years young! 🎈")

# Button interaction
st.subheader("🚀 Try this button")  
if st.button("Click Me!"):
    st.success("You clicked the button! 🎉 Hope you're enjoying this demo!")

# Checkbox for fun
agree = st.checkbox("I think Streamlit is awesome!")
if agree:
    st.write("🔥 You're absolutely right! Streamlit makes life easier for developers.")

# Simple data visualization
st.subheader("📊 Random Chart")  
st.write("Here's a randomly generated chart just for fun!")  

data = pd.DataFrame(
    np.random.randn(20, 3),  
    columns=["A", "B", "C"]  
)
st.line_chart(data)

# Thank you message
st.write("Thanks for checking out my app! Have a great day! 🚀😃")
