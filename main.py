import streamlit as st
from app.about import show_about
from app.contact import show_contact
from app.portfolio import show_portfolio

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'About'

def set_page(page):
    st.session_state.page = page

st.title("Vivek Mistry's Portfolio")

st.sidebar.title("Navigation")

# Create buttons for navigation
st.sidebar.button("About", on_click=set_page, args=("About",))
st.sidebar.button("Contact", on_click=set_page, args=("Contact",))
st.sidebar.button("Portfolio", on_click=set_page, args=("Portfolio",))

# Display the selected page
if st.session_state.page == 'About':
    show_about()
elif st.session_state.page == 'Contact':
    show_contact()
elif st.session_state.page == 'Portfolio':
    show_portfolio()