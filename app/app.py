import streamlit as st
from utils import style
from utils import login
st.set_page_config(layout="wide")

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Home"]

def login_page():

    st.header("Log in")

    if login.check_password():
        st.session_state.role = "Home"
        st.rerun()

def logout():
    st.session_state.role = None
    st.session_state["password_correct"] = "logged out"
    st.rerun()

role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", 
                   title="Settings", 
                   icon=":material/settings:")
search = st.Page("view/search.py", 
                    title="Busca de usuários", 
                    icon=":material/help:",
                    default=(role == "Home"),
)

# filter_devices = st.Page(
#     "view/api_device_filter_docs.py",
#     title="Log Insights Documents",
#     icon=":material/help:",
# )

request_pages = [search]
account_pages = [logout_page, settings ]

page_dict = {}
if st.session_state.role in ["Home"]:
    page_dict["Request"] = request_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login_page)])

pg.run()