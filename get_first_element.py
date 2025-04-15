import streamlit as st

# Title of the app
st.title("Get First Element from List")

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

# Display the first element if the list is not empty
if st.session_state.data_list:
    st.write("First Element:", st.session_state.data_list[0])
else:
    st.write("The list is empty.")
