import streamlit as st
import pandas as pd
import numpy as np

# Title for the app
st.title("Basic Streamlit App")

# Adding text input
name = st.text_input("Enter your name", "Type here...")
st.write(f"Hello, {name}!")

# Slider for user to select a number
number = st.slider("Pick a number", 0, 100, 25)
st.write(f"You selected: {number}")

# Data display with a simple line chart
st.write("Random data line chart")
data = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])
st.line_chart(data)