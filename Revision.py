# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Video Upload
import streamlit as st
video_file = open('Video.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
