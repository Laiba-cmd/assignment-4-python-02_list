import streamlit as st
import numpy as np
import cv2

# Title of the app
st.title("Erase Canvas")

# Create a canvas
canvas_size = (400, 400)
canvas = np.zeros((canvas_size[0], canvas_size[1], 3), dtype=np.uint8)

# Draw on the canvas
if st.button("Draw"):
    # Simulate drawing by adding random colors
    for i in range(100):
        x, y = np.random.randint(0, canvas_size[0]), np.random.randint(0, canvas_size[1])
        cv2.circle(canvas, (x, y), 5, (255, 0, 0), -1)

# Display the canvas
st.image(canvas, channels="RGB")

# Button to erase the canvas
if st.button("Erase"):
    canvas = np.zeros((canvas_size[0], canvas_size[1], 3), dtype=np.uint8)

# Display the cleared canvas
st.image(canvas, channels="RGB")
