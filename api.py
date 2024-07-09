import streamlit as st
import pandas as pd
from PIL import Image
import joblib
import os
import pickle


st.set_page_config(layout="wide")
custom_css = """
    <style>
        body {
            font-size: 18px !important;
            font-family: CenturyGothic, sans-serif !important;
            font-weight: bold !important;
        }
    </style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
# Title with image
st.sidebar.title("IAQ4EDU project")
img_path = "https://github.com/hugoapi/api2/raw/main/IAQ4EDU.png"
st.sidebar.image(img_path)



# In[2] webapp
# Title
#img = Image.open("IAQ4EDU.png")
#st. image(img)

# In[3] webapp

# Selectbox
Season = "Season"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Season}</span>", unsafe_allow_html=True)
selectboxexample = st.selectbox(label="Season", label_visibility='collapsed', options=("Spring", "Summer", "Winter"))

# Input bar 1
Classroom_volunme = "Classroom volunme"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Classroom_volunme}</span>", unsafe_allow_html=True)
volume = st.number_input(label="Classroom volunme", label_visibility='collapsed', min_value=0.00, format='%.2f')

# Input bar 2
N_students = "Number of students"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{N_students}</span>", unsafe_allow_html=True)
students = st.number_input(label="Number of students",label_visibility='collapsed', min_value=0, max_value=100, format='%g')

# Input bar 3
Occupancy_duration = "Occupancy duration"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Occupancy_duration}</span>", unsafe_allow_html=True)
occtime = st.number_input(label="Occupancy duration",label_visibility='collapsed', min_value=0, format='%g')

# Input bar 4
Area_window = "Opening area of windows"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Area_window}</span>", unsafe_allow_html=True)
openwindow = st.number_input(label="Opening area of windows",label_visibility='collapsed', min_value=0.00, format='%.2f')

# Input bar 5
Duration_window = "Window opening duration"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Duration_window}</span>", unsafe_allow_html=True)
windowtime = st.number_input(label="Window opening duration",label_visibility='collapsed', min_value=0, format='%g')

# Input bar 6
Area_door = "Opening area of door"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Area_door}</span>", unsafe_allow_html=True)
opendoor = st.number_input(label="Opening area of door",label_visibility='collapsed', min_value=0.00, format='%.2f')

# Input bar 7
Duration_door = "Door opening duration"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Duration_door}</span>", unsafe_allow_html=True)
doortime = st.number_input("Door opening duration", label_visibility='collapsed', min_value=0, format='%g')

# Text area
Comments = "Do you have any comments?"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Comments}</span>", unsafe_allow_html=True)
st.text_area("Do you have any comments?", label_visibility='collapsed')

# Fonction pour vérifier et charger le modèle
def load_model(model_path):
    try:
        if os.path.isfile(model_path):
            model = joblib.load(model_path)
            st.success(f"Modèle {model_path} chargé avec succès.")
            return model
        else:
            st.error(f"Le fichier {model_path} n'a pas été trouvé.")
            return None
    except Exception as e:
        st.error(f"Erreur lors du chargement du modèle: {str(e)}")
        return None

# Chemin du modèle
model_path = "model.pkl"

# Charger le modèle
model = load_model(model_path)

if model is not None:
    # Font personnalisée (optionnelle, pour le style de l'interface utilisateur)
    custom_css = """
        <style>
            body {
                font-size: 18px !important;
                font-family: CenturyGothic, sans-serif !important;
                font-weight: bold !important;
            }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


    # Bouton pour lancer la prédiction
    if st.button("Connaître votre IAQ"):
        # Préparer les données d'entrée
        X = pd.DataFrame([[volume, students, occtime, openwindow, windowtime, opendoor, doortime]], 
                         columns=["VOLUME", "TOTAL_STUDENTS", "OCCUPIED_TIME", "OPENING_SIZE_WINDOW",
                                  "OPENINNG_WINDOW_TIME", "OPENING_SIZE_DOOR", 
                                  "OPENING_DOOR_TIME"])

        try:
            # Obtenir la prédiction
            prediction = model.predict(X)[0]

            # Afficher la prédiction
            if prediction == 1:
                st.success("Votre niveau de qualité de l'air est : Bon")
            elif prediction == 2:
                st.warning("Votre niveau de qualité de l'air est : Acceptable")
            elif prediction == 3:
                st.error("Votre niveau de qualité de l'air est : Mauvais")
            else:
                st.error("Impossible de déterminer le niveau de qualité de l'air")
        except Exception as e:
            st.error(f"Erreur lors de la prédiction: {str(e)}")
else:
    st.error("Modèle non chargé. Veuillez vérifier le fichier modèle et réessayer.")
