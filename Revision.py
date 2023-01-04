# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import module
import streamlit as st
# Display Images
from PIL import Image
img = Image.open("Karina.png")
st.image(img, width=400)
