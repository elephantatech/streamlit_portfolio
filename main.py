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

# Add CSS to make buttons the same width
st.markdown(
    """
    <style>
    .sidebar .stButton button {
        width: 100%;
        display: block;
        margin: 5px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create buttons for navigation
if st.sidebar.button("About", use_container_width=True):
    set_page("About")
if st.sidebar.button("Contact", use_container_width=True):
    set_page("Contact")
if st.sidebar.button("Portfolio", use_container_width=True):
    set_page("Portfolio")

# Display the selected page
if st.session_state.page == 'About':
    show_about()
elif st.session_state.page == 'Contact':
    show_contact()
elif st.session_state.page == 'Portfolio':
    show_portfolio()
