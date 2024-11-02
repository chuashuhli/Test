import streamlit as st
from utility import check_password

#check if password is correct
if not check_password():
    st.stop()


st.title("Methodology")
st.write("""
This page outlines the methodology followed in generating this page.
The methodology involves the following key steps:
""")

st.header("1. User Query")

st.header("2. Identify Available Social Assistance")

st.header("3. Get Social Assistance Details")

st.header("4. Generate Response Based on Social Assistance Details")

st.header("5. LLM Response")

st.header("6. Location of Social Service Offices were converted to Latitude and Longitude to be added into the map")

st.write("This structured approach ensures that responses are tailored, accurate, and directly relevant to the user's social assistance needs.")