import streamlit as st
st.set_page_config(
    page_title="Event Counter",
    layout="centered"
)

st.title("Event Counter")
if "count" not in st.session_state:
    st.session_state.count = 0
fwd_button = st.button("Forward")
back_button = st.button("Back")
reset_button = st.button("reset")

if fwd_button:
    st.session_state.count = st.session_state.count + 1
elif back_button:
    st.session_state.count = st.session_state.count - 1
elif reset_button:
    st.session_state.count = 0
st.write(st.session_state.count)