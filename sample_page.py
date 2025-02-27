import streamlit as st  
import pandas as pd  
import numpy as np  
st.title("🎉Welcome to Streamlit App!")  
st.write("Hey there! 👋 This is a simple web app built using Streamlit ")
st.subheader("Tell me about yourself")  
name = st.text_input("What's your name?")
if name:
    st.write(f"Nice to meet you, {name}! 😊 Hope you're having a great day!")
st.subheader("🎂 Age Selector")  
age = st.slider("How old are you?", 1, 100, 25)
st.write(f"Wow! You're {age} years young! 🎈")
st.subheader("🚀 Try this button")  
if st.button("Click Me!"):
    st.success("You clicked the button! 🎉 Hope you're enjoying this demo!")
agree = st.checkbox("I think Streamlit is awesome!")
if agree:
    st.write("🔥 You're absolutely right! Streamlit makes life easier for developers.")
st.subheader("📊 Random Chart")  
st.write("Here's a randomly generated chart just for fun!")  

data = pd.DataFrame(
    np.random.randn(20, 3),  
    columns=["A", "B", "C"]  
)
st.line_chart(data)
st.write("Thanks for checking out my app! Have a great day! 🚀😃")
