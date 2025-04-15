import streamlit as st

# Title of the app
st.title("Double the Numbers")

# Input for numbers
numbers = st.text_input("Enter numbers separated by commas:")

# Process the input
if numbers:
    # Split the input string into a list of numbers
    number_list = [float(num) for num in numbers.split(",") if num.strip()]
    doubled_list = [num * 2 for num in number_list]
    
    # Display the result
    st.write(f"The doubled numbers are: {doubled_list}")
