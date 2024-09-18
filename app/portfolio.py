import streamlit as st

def show_portfolio():
    st.header("Portfolio")


    old_projects = [
        {
            "title": "Making APIs work for you",
            "description": "Webinar series I delivered for BlueCat Networks while I worked there.",
            "url": "https://github.com/bluecatlabs/making-apis-work-for-you/"
        },
        {
            "title": "ML Learnings",
            "description": "ML Learning I had during great Learning course for MIT Applied Data Science course.",
            "url": "https://github.com/elephantatech/ML_Learnings"
        },
        {
            "title": "Decode url chrome extension",
            "description": "My chrome extension I use when troubleshooting the url during development on chrome like browsers.",
            "url": "https://github.com/elephantatech/url-decorder-extension"
        }
    ]

    current_projects = [
        {
            "title": "ticketmaster",
            "description": "FastAPI REST API that allows for simple ticket system with Redis database.",
            "url": "https://elephantatech.github.io/ticketmaster/"
        },
        {
            "title": "booksapp",
            "description": "Flask REST API web app with MySQL backend for simple CRUD app with API.",
            "url": "https://github.com/elephantatech/bookapp"
        },
        {
            "title": "fast-tools",
            "description": "FastAPI REST service demonstrating backend service with database connectivity built with FastAPI, SQLAlchemy, Alembic.",
            "url": "https://github.com/elephantatech/fast-tools"
        },
        {
            "title": "Python Google DNS lookup",
            "description": "Simple script to demonstrate how to use dns.google.com REST API to query DNS records.",
            "url": "https://github.com/elephantatech/GoogleDNSLookup"
        },
        {
            "title": "dcataloger",
            "description": "Library application built with Django with UI and API. Presently still developing it.",
            "url": "https://github.com/elephantatech/dcatalog"
        },
        {
            "title": "django docker boilerplate template",
            "description": "Boilerplate template to get started local development with Django and PostgreSQL on Docker.",
            "url": "https://github.com/elephantatech/django-docker-template"
        },
        {
            "title": "bashtoolbox",
            "description": "My reference bash scripts and Linux bash command references with cheatsheets.",
            "url": "https://github.com/elephantatech/bashtoolbox"
        }
    ]

    st.subheader("Older Projects", divider=True)
    old_cols = st.columns(3)  # Create 3 columns for the grid layout

    for i, project in enumerate(old_projects):
        with old_cols[i % 3]:
            st.markdown(f"[**{project['title']}**]({project['url']})")
            st.write(project["description"])
    
    st.subheader("Active Projects", divider=True)
    curr_cols = st.columns(3)  # Create 3 columns for the grid layout

    for i, project in enumerate(current_projects):
        with curr_cols[i % 3]:
            st.markdown(f"[**{project['title']}**]({project['url']})")
            st.write(project["description"])
