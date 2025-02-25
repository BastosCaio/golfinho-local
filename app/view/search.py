import streamlit as st
import os
import json
import shutil
import logging
from utils.state_session_helpers import ss_verify
from utils.utils import get_full_json, get_photo_data_from_id
from PIL import Image
import io
import base64
import requests
import re
from dotenv import load_dotenv
import os
import sys
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from st_aggrid.shared import JsCode
import concurrent.futures
from deepface import DeepFace

import pandas as pd

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def process_base64_image(base64_string):
    """
    Process a base64 string into a format that can be displayed in AG-Grid
    
    Args:
        base64_string: The base64 encoded image string
    Returns:
        str: A data URL that can be used in an img src attribute
    """
    if not base64_string:
        return "https://via.placeholder.com/50"
    
    # If the string is a list with one element, get the first element
    if isinstance(base64_string, list) and len(base64_string) > 0:
        base64_string = base64_string[0]
    
    # Remove any existing data URL prefix
    if 'base64,' in base64_string:
        base64_string = base64_string.split('base64,')[1]
    
    # Create the complete data URL
    return f"data:image/jpeg;base64,{base64_string.strip()}"

def run_recognition():
    st.session_state['face'] = True
    # Add your code here

    pass


def delete_user_list(opt):
    # Add your code here

    if opt.selected_rows is not None and not opt.selected_rows.empty:
        for i in range (0,len(opt.selected_rows)):
            selected_device = opt.selected_rows.iloc[i]
            user_id = str(selected_device["UserID"])


            if os.path.exists(selected_device["LocalPath"]):
                shutil.rmtree(os.path.dirname(selected_device["LocalPath"]))

            st.write('Usuário: ' + user_id + ' deletado da base local.')
            
    else:
        st.write('Nenhum usuário foi selecionado, por favor selecione um usuário para deletar.')

    pass

def clean_selection(opt):
    st.write("Limpando seleção")
    # Add your code here


    opt.selected_rows.empty
    

def show_page(params):
    page_width = 0.6
    _, content, __ = st.columns(((1-page_width)/2, page_width, (1-page_width)/2))

    st.session_state['Face'] = False

    with content:
        st.title("Busca de usuários")

        users = json.loads(get_full_json())

        user_name = content.text_input("Digite o nome do usuário", key="user_name")

        if user_name:
            users = {k: v for k, v in users.items() if user_name.lower() in v.get("CardName", "").lower()}


        st.subheader("Usuários")
        st.write("Selecione um usuário para ver a foto.")


        df = pd.DataFrame.from_dict(users,orient='index')


        PHOTO_DATA_FILE = "photo_data.json"


        # Load existing photo data from JSON file
        def load_photo_data():
            if os.path.exists(PHOTO_DATA_FILE):
                with open(PHOTO_DATA_FILE, "r") as f:
                    return json.load(f)
            return {}

        # Save updated photo data to JSON file
        def save_photo_data(photo_data):
            with open(PHOTO_DATA_FILE, "w") as f:
                json.dump(photo_data, f)

        # # Function to fetch photo data
        # def fetch_photo(user_id):
        #     return get_photo_data_from_id(user_id) or None
        
        # Function to fetch photo data
        def fetch_photo(user_id):
            photo = get_photo_data_from_id(user_id) or None
            return photo
        
        if "photo_data" not in st.session_state:
            st.session_state.photo_data = load_photo_data()
        
        if "face" not in st.session_state:
            st.session_state.face = False

        missing_users = [uid for uid in df["UserID"].astype(str) if uid not in st.session_state.photo_data]


        new_data = {}

        if missing_users:
            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                results = executor.map(fetch_photo, missing_users)
                for user_id, photo in zip(missing_users, results):
                    new_data[user_id] = photo  # Store result locally
                    save_photo_data({**st.session_state.photo_data, **new_data})  # Save incrementally

        st.session_state.photo_data.update(new_data)

        # Add PhotoData column to DataFrame
        df["PhotoData"] = df["UserID"].astype(str).map(st.session_state.photo_data)       

        df["PhotoData64"] = df["PhotoData"].apply(lambda x: base64.b64decode(x[0]) if x else None)


        # Process PhotoData column
        df["PhotoData64"] = df["PhotoData"].apply(
            lambda x: process_base64_image(x) if x else "https://via.placeholder.com/50"
        )

        column_names = ["PhotoData64","UserID", "CardName"]

        df_display = df[column_names]

        # Configure AG-Grid
        grid_builder = GridOptionsBuilder.from_dataframe(df_display, editable=True)
        
        # Image cell renderer
        cell_renderer = JsCode("""
            class ImageCellRenderer {
                init(params) {
                    this.eGui = document.createElement('img');
                    this.eGui.src = params.value || "https://via.placeholder.com/50";
                    this.eGui.width = 150;
                    this.eGui.height = 150;
                    this.eGui.style.borderRadius = "5px";
                    this.eGui.style.objectFit = "cover";
                    this.eGui.onerror = function() {
                        this.src = "https://via.placeholder.com/50";
                    };
                }
                getGui() {
                    return this.eGui;
                }
            }
        """)
        

        # Configure the PhotoData64 column
        grid_builder.configure_column(
            "PhotoData64",
            headerName="Photo",
            # width=200,
            cellRenderer=cell_renderer
        )
        
        # Configure grid options
        grid_builder.configure_grid_options(rowHeight=150)
        grid_builder.configure_selection('single', use_checkbox=True)
        
        grid_options = grid_builder.build()

        # Display the grid
        opt = AgGrid(
            df_display,
            gridOptions=grid_options,
            updateMode=GridUpdateMode.VALUE_CHANGED,
            allow_unsafe_jscode=True,
            key='grid2'
        )


        if opt.selected_rows is not None and not opt.selected_rows.empty:
            selected_device = opt.selected_rows.iloc[0]
            user_id = str(selected_device["UserID"])

            if not user_id:
                st.error("Erro ao carregar o ID do usuário")
            else :
                # user = users[user_id]
                user = df[df['UserID'] == user_id]
                st.write(user)
                st.subheader(f"Usuário {user_id}")
                st.write(f"Nome: {user['CardName'].iloc[0]}")

                photo_data = get_photo_data_from_id(user_id)
                if not photo_data:
                    st.error("Erro ao carregar a foto")
                else:
                    for i, photo in enumerate(photo_data):
                        try:
                            decoded_data = base64.b64decode(photo)
                            image = Image.open(io.BytesIO(decoded_data))
                            st.image(image, caption=f"Foto {i}")
                        except Exception as e:
                            st.error(f"Failed to decode photo data for image {i}: {e}")
                            continue


        # page_width = 0.6
        # _, content, __ = st.columns(((1-page_width)/2, page_width, (1-page_width)/2))

        buttons_width = 0.2       
        _, button1,button2, __ = st.columns((0.3, buttons_width, buttons_width, 0.3))

        button1.button("Avaliar na base", on_click=lambda: run_recognition())

        if st.session_state['face'] == True:
  
            st.write("Avaliando na base - Pode levar alguns minutos. Por favor aguarde")
            
            
            img_folder = 'photos/face_photos_user_'+user['UserID'][0]+'/'
            try:
                filename = next(os.walk(img_folder), (None, None, []))[2][0]
            
                img_path = img_folder + filename


                dfs = DeepFace.find(
                    img_path = img_path,
                    db_path = 'photos',
                    model_name = "Facenet",
                    threshold = 4.4
                )
                df2 = pd.DataFrame(dfs[0])


                df2 = df2[:5]
                df2['PhotoData'] = ""
                df2["PhotoData64"] = ""
                df2["UserID"] = ""

                df2['LocalPath'] = df2['identity']
                st.write('Imagem do Usuário Selecionado.')
                st.image(df2['LocalPath'].loc[0])

                for i in range (len(df2['LocalPath'])):

                    user_id = re.search('user_(.*)/', df2['LocalPath'].loc[i])
                    df2["UserID"].loc[i] = user_id.group(1)
                    
                    with open(df2['LocalPath'].loc[i], "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read())
                        df2['PhotoData'].loc[i] = str(encoded_string)
                    
                    
                

                df2["PhotoData"] = df2["UserID"].astype(str).map(st.session_state.photo_data)

                df2["PhotoData64"] = df2["PhotoData"].apply(
                    lambda x: process_base64_image(x) if x else "https://via.placeholder.com/50"
                )

                column_names = ["UserID","PhotoData64","LocalPath"]
                df_display2 = df2[column_names]

                st.write('Dentre os usuários similares segundo o sistema, selecione os que deseja apagar.')
                

                grid_builder = GridOptionsBuilder.from_dataframe(df_display2, editable=True)

                cell_renderer = JsCode("""
                class ImageCellRenderer {
                    init(params) {
                        this.eGui = document.createElement('img');
                        this.eGui.src = params.value || "https://via.placeholder.com/50";
                        this.eGui.width = 150;
                        this.eGui.height = 150;
                        this.eGui.style.borderRadius = "5px";
                        this.eGui.style.objectFit = "cover";
                        this.eGui.onerror = function() {
                            this.src = "https://via.placeholder.com/50";
                        };
                    }
                    getGui() {
                        return this.eGui;
                    }
                }
            """)
                
            
                grid_builder.configure_column(
                    "PhotoData64",
                    headerName="Photo",
                    width=200,
                    cellRenderer=cell_renderer
                )

                
                grid_builder.configure_grid_options(rowHeight=150)
                grid_builder.configure_selection('multiple', use_checkbox=True)
                grid_options = grid_builder.build()
                
                # Display the grid
                opt = AgGrid(
                    df_display2,
                    gridOptions=grid_options,
                    updateMode=GridUpdateMode.VALUE_CHANGED,
                    allow_unsafe_jscode=True,
                    key='grid3'
                )

                _, button3,button4, __ = st.columns((0.3, buttons_width, buttons_width, 0.3))

                button3.button("Deletar" , on_click=lambda: delete_user_list(opt))

            except:
                st.write('O usuário que você selecionou não existe na base local.')
                st.session_state['face'] == False
            
            # delete_user_name = content.text_input("Digite o nome do usuário a ser deletado", key="delete_user_name")

        



        # user_id = content.text_input("Digite o ID do usuário", key="user_id")
        # if not user_id:
        #     return
        
        # if not user_id.isdigit():
        #     content.error("O ID do usuário deve ser um número")
        #     return
        
        # user_id = int(user_id)
        # if user_id not in users:
        #     content.error("Usuário não encontrado")
        #     return
        
        # user = users[user_id]
        # content.subheader(f"Usuário {user_id}")
        # content.write(f"Nome: {user.get('Name', 'N/A')}")

        # photo_data = get_photo_data_from_id(user_id)
        # if not photo_data:
        #     content.error("Erro ao carregar a foto")
        #     return
        

        

show_page({})
