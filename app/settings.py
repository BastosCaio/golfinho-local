import streamlit as st
from forms.settings_menu import settings_form
from utils.config_handler import load_config, save_config

# Initialize config state if not present
if "settings" not in st.session_state:
    st.session_state["settings"] = load_config()

st.header("Settings")
st.write(f"You are logged in as {st.session_state.get('role', 'guest')}.")

# Show contact form
settings_form()




