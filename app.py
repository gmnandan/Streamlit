# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BgGqFHNgwfz4gk_jkJLKFHmkmUI6nP3H
"""

import streamlit as st

def largest_number(a, b, c):
    """Function to find the largest among 3 given numbers."""
    return max(a, b, c)

# Title of the web application
st.title("Find the largest number")

# User input for 3 numbers
a = st.number_input("Enter the first number", value=0)
b = st.number_input("Enter the second number", value=0)
c = st.number_input("Enter the third number", value=0)

# Button to find the largest number
if st.button("Find largest number"):
    largest_num = largest_number(a, b, c)
    st.success(f"The largest number is {largest_num}")