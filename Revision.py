# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import module
import streamlit as st
# Display Images
from PIL import Image
img = Image.open("C:/Users/Appu/Desktop/Streamlit Test/Karina.png")
st.image(img, width=200)