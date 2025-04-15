import streamlit as st

# Title of the app
st.title("Flowing Data Structure Example")

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

# Button to clear the list
if st.button("Clear List"):
    st.session_state.data_list.clear()
    st.success("List cleared!")
