import streamlit as st

def show_about():
    st.header("About Me")
    st.write("I am an experienced fullstack Python developer with JavaScript skills as well. I’m currently learning machine learning and automation around infrastructure as code.")

    st.image("https://raw.githubusercontent.com/elephantatech/elephantatech/2161e5cf288738f06ee0899cea8e1dc5c1798a72/IMG_0753.JPG", caption="Profile Picture")

    st.header("Social Connections")
    st.markdown(":baby_chick: [Twitter](https://twitter.com/elephantatech)")
    st.markdown(":office: [linkedin](https://www.linkedin.com/in/vivekmistry/)")
    st.markdown(":elephant: [more about me](https://about.me/vivekmistry)")


