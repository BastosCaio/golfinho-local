import streamlit as st
import re
from utils.config_handler import load_config, save_config

def settings_form():
    with st.form("settings_form"):
        st.header("DvM Connection")

        if "settings" not in st.session_state:
            st.session_state["settings"] = load_config()

        # Initialize inputs with values from the 'settings' state
        base_url = st.text_input("Base URL", 
                                 value=st.session_state["settings"].get("base_url", "gdm.local"))
        client_id = st.text_input("Client ID", 
                                  value=st.session_state["settings"].get("clientId", ""))
        secret_id = st.text_input("Secret ID", 
                                  value=st.session_state["settings"].get("clientSecret", ""))

        st.subheader("Model Prompt Instructions")
        prompt_inst = st.text_area("Prompt Instructions", 
                                   value=st.session_state["settings"].get("prompt", ""))
        
        # Add LLM model selection
        # model_options = ['Choose a model', 'llama3:8b', 'gemma2:2b', 'phi3:3.8b']
        MODEL_OPTIONS = st.session_state["settings"].get("model_options", ["Choose a model"])

        selected_model = st.selectbox(
            'Select a model to use',
            MODEL_OPTIONS,
            index=MODEL_OPTIONS.index(st.session_state["settings"].get("model", "Choose a model"))
        )

        # Form submit button
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Update session state with form inputs
            st.session_state["settings"]["base_url"] = base_url
            st.session_state["settings"]["clientId"] = client_id
            st.session_state["settings"]["clientSecret"] = secret_id
            st.session_state["settings"]["prompt"] = prompt_inst
            st.session_state["settings"]["model"] = selected_model  # Save the model selection

            st.success("Settings updated in memory. Don't forget to save!")


    # Add a Save button for explicit saving
    if st.button("Save Settings"):
        save_config(st.session_state["settings"])
        st.success("Settings saved successfully!")
        st.rerun(scope="app")


