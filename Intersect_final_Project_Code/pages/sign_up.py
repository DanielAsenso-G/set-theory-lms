import streamlit as st
import time
from Intersect_app import *

st.title("Sign UP!")

# Initialize session state for sign-up
if "signed_up" not in st.session_state:
    st.session_state.signed_up = False

# Use a unique page identifier to avoid duplicate keys
page_id = "sign_up"

# Sign-up form
if not st.session_state.signed_up:
    st.subheader("Sign Up")
    username = st.text_input("New Username", key=f"{page_id}_username")
    password = st.text_input("New Password", type="password", key=f"{page_id}_password")
    
    if st.button("Sign Up"):
        # Indicate successful sign-up and store session state
        st.session_state.signed_up = True
        st.success("Account created successfully! Please wait...")
        time.sleep(2)
        
        # Redirect to homepage.py after sign-up
        st.page_link(home_page) 

# If already signed up, display a message or redirect to the homepage immediately
else:
    st.success("You are already signed up!")
    st.page_link(home_page)
