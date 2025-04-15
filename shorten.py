import streamlit as st

# Title of the app
st.title("Shorten List of Items")

# Initialize a list to store user inputs
if 'data_list' not in st.session_state:
    st.session_state.data_list = []

# Input for new data
new_data = st.text_input("Enter new data:")

# Button to add data to the list
if st.button("Add to List"):
    if new_data:
        st.session_state.data_list.append(new_data)
        st.success(f"Added: {new_data}")

# Display the current list
st.write("Current List:")
st.write(st.session_state.data_list)

# Set max_value based on the length of the data_list
max_value = len(st.session_state.data_list) if st.session_state.data_list else 1

# Input for the number of items to display
num_items = st.number_input("Number of items to display:", min_value=1, max_value=max_value, value=1)

# Display the shortened list
if st.session_state.data_list:
    st.write("Shortened List:")
    st.write(st.session_state.data_list[:num_items])
else:
    st.write("The list is empty.")
