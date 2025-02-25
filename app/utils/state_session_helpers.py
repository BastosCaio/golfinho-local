import streamlit as st

def ss_verify(state:str, value:any=True):
    return state in st.session_state and st.session_state[state] == value

def ss_getvalue(state:str, return_if_empty:any=None):
    if state in st.session_state:
        return st.session_state[state]
    return return_if_empty