import streamlit as st

def hidden_menu_and_footer():
    hide_menu = '''
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    '''
    st.markdown(hide_menu, unsafe_allow_html=True)

def headerstyle():
    st.markdown(
    """
    <nav class="navbar fixed-top navbar-light bg-white" style="color: #ffffff; padding: 0.8rem 1rem;">
        <span class="navbar-brand mb-0 h1"></span>
    </nav>
    """, unsafe_allow_html=True
    )

def space(tamanho):
    if tamanho == 1:
        st.title('')
    if tamanho == 2:
        st.header('') 
    if tamanho == 3:
        st.write('') 

def sidebarwidth():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            width: 250px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 250px;
            margin-left: -500px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def font_google():
    st.markdown(
        """
        <style>
        @font-face {
            font-family: 'Roboto';
            font-style: normal;
            font-weight: 400;
            src: url(https://fonts.gstatic.com/s/tangerine/v12/IurY6Y5j_oScZZow4VOxCZZM.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
        html, body, [class*="css"] {
            font-family: 'Roboto';
            font-size: 48px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def up_bar():
    st.markdown(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" crossorigin="anonymous"></script>
    """, unsafe_allow_html=True
    )

def style_0():
    st.markdown(
    """
    <style>
    .st-bv { background-color: #f2f2f2; }
    a { color:rgb(0, 0, 0); text-align: left; font-size: 14px; font-family: sans-serif; }
    p { color:rgb(0, 0, 0); text-align: left; font-size: 14px; font-family: sans-serif; }
    .css-10trblm { position: relative; flex: 1 1 0%; margin-left: calc(3rem); color:rgb(56, 67, 191); font-family: sans-serif; font-weight: bold; }
    h3 { color:rgb56, 67, 191; text-align: left; font-size: 20px; font-family: sans-serif; }
    [data-testid="stMetricValue"] { font-size: 25px; }
    .css-po1uzv { position: fixed; top: 0px; left: 0px; right: 0px; height: 0.000rem; background: rgb(220, 224, 247); outline: none; z-index: 999990; display: block; }
    .css-11qlpl9 { position: fixed; top: 0px; left: 0px; right: 0px; height: 0.00rem; background: rgb(250, 250, 250); outline: none; z-index: 999990; display: block; }
    .css-hxt7ib { padding-top: 0rem; padding-left: 1rem; padding-right: 1rem; }
    .css-12oz5g7 { flex: 1 1 0%; width: 100%; padding: 0rem 1rem 10rem; max-width: 46rem; }
    .st-b7 { border-radius: 2px; border-color: black; }
    .main-svg { border-radius: 2.25rem; width: 100%; display: flex; flex-wrap: wrap; flex-grow: 1; align-items: stretch; }
    .plot-container.plotly { width: 100%; display: flex; flex-wrap: wrap; flex-grow: 1; align-items: stretch; }
    .stDataFrame { border-radius: 10px; background: rgb(255, 255, 255); background-color: white; color: white; font-weight: bold; }
    table, td { font-weight: 500; }
    .css-a58qmi-EmotionIconBase { vertical-align: middle; overflow: hidden; color: inherit; fill: currentcolor; display: inline-flex; font-size: 1.25rem; width: 1.25rem; height: 1.25rem; margin: 0px -1.5rem 0px 10px; }
    </style>
    """, unsafe_allow_html=True
    )

def style_menu():
    hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    reduce_header_height_style = """
    <style>
        div.block-container {padding-top:0rem;}
        #MainMenu {visibility: visible;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        footer:after {
            content:'Copyright Bix-tech 2023';
            visibility: visible;
            display: block;
            position: relative;
            padding: 0px;
            top: 0px;
        }
    </style>
    """
    st.markdown(reduce_header_height_style, unsafe_allow_html=True)









# import streamlit as st

# from dateutil.relativedelta import relativedelta
# from datetime import datetime

# #esconder botões do streamlit
# def hidden_menu_and_footer():
#     hide_menu = '''
#     <style>
#     #MainMenu {
#         visibility:hidden;
#     }

#     footer{
#         visibility:hidden;
#     }

#     </style>
#     '''
#     st.markdown(hide_menu, unsafe_allow_html=True)

# #linha no cabeçalho branca desing
# def headerstyle():
#     st.markdown(
#     f"""
#     <nav class="navbar fixed-top navbar-light bg-white" style="color: #ffffff; padding: 0.8rem 1rem;">
#         <span class="navbar-brand mb-0 h1" " >  </span>
#     </nav>
#     """, unsafe_allow_html=True
#     )


# #espaço entre plots
# def space(tamanho):
#     if tamanho == 1:
#         st.title('')
#     if tamanho == 2:
#         st.header('') 
#     if tamanho == 3:
#         st.write('') 

# def sidebarwidth():
#     st.markdown(
#         """
#         <style>
#         [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
#             width: 250px;
#         }
#         [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
#             width: 250px;
#             margin-left: -500px;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#         )    

# def font_google():
#     st.markdown(
#             """
#             <style>
#     @font-face {
#     font-family: 'Roboto';
#     font-style: normal;
#     font-weight: 400;
#     src: url(https://fonts.gstatic.com/s/tangerine/v12/IurY6Y5j_oScZZow4VOxCZZM.woff2) format('woff2');
#     unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
#     }

#         html, body, [class*="css"]  {
#         font-family: 'Roboto';
#         font-size: 48px;
#         }
#         </style>

#         """,
#             unsafe_allow_html=True,
#         )

# def up_bar():
#     st.markdown(
#     """
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
#     """,unsafe_allow_html=True
#         )  



# #general style css
# def style_0():
#     st.markdown(
#     """
    

#     <style>

#     .st-bv {
#     background-color: #f2f2f2;
#     }
    
#     a{
#     color:rgb(0, 0, 0);
#     text-align: left;
#     font-size: 14px;
#     font-family: sans-serif;
    
#     }

#     p{
#     color:rgb(0, 0, 0);
#     text-align: left;
#     font-size: 14px;
#     font-family: sans-serif;
#     }

#     /* st.header */
#     .css-10trblm {
#     position: relative;
#     flex: 1 1 0%;
#     margin-left: calc(3rem);
#     color:rgb(56, 67, 191);
#     font-family: sans-serif;
#     font-weight: bold;
#     }

#     h3{
#     color:rgb56, 67, 191;
#     text-align: left;
#     font-size: 20px;
#     font-family: sans-serif;
#     }


#     /* Fonte st.metric */
#     [data-testid="stMetricValue"] {
#         font-size: 25px;
#     }  


#     /* Topo da página para cor de BK #f0eeee  */
#     .css-po1uzv {
#     position: fixed;
#     top: 0px;
#     left: 0px;
#     right: 0px;
#     height: 0.000rem;
#     /* background: rgb(240, 238, 238); */
#     background: rgb(220, 224, 247);
#     outline: none;
#     z-index: 999990;
#     display: block;
#     }

#     /* Topo da página para cor de BK #fafafa  */
#     .css-11qlpl9 {
#     position: fixed;
#     top: 0px;
#     left: 0px;
#     right: 0px;
#     height: 0.00rem;
#     background: rgb(250, 250, 250);
#     outline: none;
#     z-index: 999990;
#     display: block;
# }

#     .css-hxt7ib {
#     padding-top: 0rem;
#     padding-left: 1rem;
#     padding-right: 1rem;
#     }

#     .css-12oz5g7 {
#     flex: 1 1 0%;
#     width: 100%;
#     padding: 0rem 1rem 10rem;
#     max-width: 46rem;
#     }

#     .st-b7 { 
#         /* width: 600px; */
#         border-radius: 2px;
#         border-color: black;
#     }

#     .main-svg{
#         border-radius: 2.25rem;
#         width: 100%;
#         display: flex;
#         flex-wrap: wrap;
#         -webkit-box-flex: 1;
#         flex-grow: 1;
#         -webkit-box-align: stretch;  
#         align-items: stretch;
#     }

#     .plot-container.plotly{
#         width: 100%;
#         display: flex;
#         flex-wrap: wrap;
#         -webkit-box-flex: 1;
#         flex-grow: 1;
#         -webkit-box-align: stretch;  
#         align-items: stretch;

#     }

#     .stDataFrame {
#         border-radius: 10px;
#         background: rgb(255, 255, 255);
#         background-color: white;
#         color: white;   
#         font-weight: bold;
#     }

#     table, td { font-weight: 500;}

    

#     .css-a58qmi-EmotionIconBase {
#         vertical-align: middle;
#         overflow: hidden;
#         color: inherit;
#         fill: currentcolor;
#         display: inline-flex;
#         font-size: 1.25rem;
#         width: 1.25rem;
#         height: 1.25rem;
#         margin: 0px -1.5rem 0px 10px;
#         /* margin: 0px -9.875rem 0px 145px; */
#     }
#     <style>
#     """, unsafe_allow_html=True
#     )

#     # div[data-testid="stVerticalBlock"] > div:first-of-type {
#     # background-color: white;
#     # }

#     # table, th, td { font-size: 14px; }

# def style_menu():
#     hide_streamlit_style = """
#     <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibllity: hidden;}
#     </style>
#     """
#     st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
#     reduce_header_height_style = """
#         <style>
#             div.block-container {padding-top:0rem;}
#             #MainMenu {visibility: visible;}
#             header {visibility: hidden;}
#             footer {visibility: hidden;}
#             footer:after {
#                 content:'Copyright Bix-tech 2023'; 
#                 visibility: visible;
#                 display: block;
#                 position: relative;
#                 #background-color: red;
#                 padding: 0px;
#                 top: 0px;
#             }
#         </style>
#         """
#     #st.markdown(reduce_header_height_style, unsafe_allow_html=True)
