import streamlit as st

st.title("Streamlit is amazing!")


# streamlit hello
# cd C:\Users\alatief\Day3
# ls
# streamlit run app.py
"""
NEVER USE SPACES IN FILENAMES
NEVER USE SPACES IN FOLDERNAMES
"""


st.write("This is my web app..")



number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")

