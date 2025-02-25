mkdir -p ~/.streamlit/

mkdir -p ~/.streamlit/


echo "\
[theme]\n\
primaryColor = '#FF4B4B'\n\
backgroundColor = '#FFFFFF\n\
secondaryBackgroundColor = '#FFFFFF'\n\
textColor = '#31333F'\n\

[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

