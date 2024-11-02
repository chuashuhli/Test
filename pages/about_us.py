import streamlit as st
from utility import check_password

#check if password is correct
if not check_password():
    st.stop()

st.set_page_config(
    page_title="About Us",
    page_icon="ℹ️",
)

st.title("About Us")

# Project Scope
st.header("Project Scope")
st.write("""
The goal of this application is to assist users in finding out more about the financial assistance available in Singapore. Comcare supports lower-income households with basic living expenses.
""")

# Objectives
st.header("Objectives")
st.write("""
- **Provide users with information on the financial assistance available**
- **Help users determine location of the nearest Social Service Office**
""")

# Data Sources
st.header("Data Sources")
st.write("""
- **Official Website**: [https://www.msf.gov.sg/what-we-do/comcare](https://www.msf.gov.sg/what-we-do/comcare)
""")

# Features
st.header("Features")

st.subheader("Virtual Assistant Care Bear🐻")
st.write("""
- **Provides a quick way to find out more about the financial assistance available in Singapore**
- **Allows users to check their eligibility**
""")

st.subheader("Social Service Agencies Location")
st.write("""
- **Provides users with details of where the social service centres are located to make applications easier**
""")

# Adding some additional styling and icons for better user experience
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
    }
    .stHeader {
        color: #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

st.write("For more information, please visit the [official website](https://www.msf.gov.sg/what-we-do/comcare).")