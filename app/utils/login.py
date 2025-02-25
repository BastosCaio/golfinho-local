import streamlit as st
import os

def check_password():
    """Returns `True` if the user had the correct password."""


    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False
    
    col1, col2, col3,= st.columns([1,1,1])

    col7, col8, col9 = st.columns([1,1,1])

    if "password_correct" not in st.session_state:
        logo_path = "assets/images/logo_site.svg"
        # col1.image(logo_path, width=100)
        col1.header(":dolphin:")
        col2.subheader("Golfinho Controle de Usuários")
        input_label = "Enter your password"
        col8.text_input(
            input_label, type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        col8.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        col8.error("😕 Incorrect password")
        return False
    elif st.session_state["password_correct"] == "logged out":
        # Password not correct, show input + error.
        col8.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        col8.warning("You are logged out")
        return False
    else:
        # Password correct.
        return True