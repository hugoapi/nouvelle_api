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

page = st.sidebar.selectbox('fill in your informations:', ["Occupants's features and behaviors", 'Outdoor environmental parameters','Building and classroom characteristics'])

# Function to create an input field with a label
def create_input_field(label, min_value=0, format='%g'):
    st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{label}</span>", unsafe_allow_html=True)
    return st.number_input(label, label_visibility='collapsed', min_value=min_value, format=format)

def create_selectbox(label, options):
    st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{label}</span>", unsafe_allow_html=True)
    return st.selectbox(label, options, label_visibility='collapsed')

if page == "Occupants's features and behaviors" :
    st.title("Occupants's features and behaviors")

    # Student's age
    student_age = create_input_field("Student's age")
    
    # Mean clothing insulation value
    mean_clothing_insulation_value = create_input_field("Mean clothing insulation value", min_value=0.0)
    
    # Number of male students
    num_male_students = create_input_field("Number of male students")
    
    # Number of female students
    num_female_students = create_input_field("Number of female students")
    
    # Number of male adults
    num_male_adults = create_input_field("Number of male adults")
    
    # Number of female adults
    num_female_adults = create_input_field("Number of female adults")
    
    # Activity level
    activity_level = create_input_field("Activity level", min_value=0.0)
    
    # Activity duration
    activity_duration = create_input_field("Activity duration", min_value=0.0)
    
    # Opening area of windows
    opening_area_windows = create_input_field("Opening area of windows", min_value=0.0)
    
    # Opening area of doors
    opening_area_doors = create_input_field("Opening area of doors", min_value=0.0)
    
    # Opening duration of windows
    opening_duration_windows = create_input_field("Opening duration of windows", min_value=0.0)
    
    # Opening duration of doors
    opening_duration_doors = create_input_field("Opening duration of doors", min_value=0.0)
    
    # Ventilation strategy
    ventilation_strategy = "Ventilation strategy"
    st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{ventilation_strategy}</span>", unsafe_allow_html=True)
    ventilation_strategy = st.selectbox("Ventilation strategy", ["Natural", "Mechanical", "Hybrid"], label_visibility='collapsed')

    if st.button("Connaître votre IAQ"):
        # Préparer les données d'entrée
        X = pd.DataFrame([[volume, students, occtime, openwindow, windowtime, opendoor, doortime]], 
                         columns=["VOLUME", "TOTAL_STUDENTS", "OCCUPIED_TIME", "OPENING_SIZE_WINDOW",
                                  "OPENINNG_WINDOW_TIME", "OPENING_SIZE_DOOR", 
                                  "OPENING_DOOR_TIME"])

elif page == 'Building and classroom characteristics' :

    st.title('Building and classroom characteristics')
    # Climate zone
    climate_zone = create_selectbox("Climate zone", ["Tropical", "Dry", "Temperate", "Continental", "Polar"])
    
    # Geographic location
    geographic_location = create_input_field("Geographic location")
    
    # Educational level
    educational_level = create_selectbox("Educational level", ["Primary", "Secondary", "Higher Education"])
    
    # Construction year
    construction_year = create_input_field("Construction year")
    
    # Classroom floor
    classroom_floor = create_input_field("Classroom floor")
    
    # Classroom volume
    classroom_volume = create_input_field("Classroom volume", min_value=0.0)
    
    # Total window area
    total_window_area = create_input_field("Total window area", min_value=0.0)
    
    # Total door area
    total_door_area = create_input_field("Total door area", min_value=0.0)
    
    # Facade orientation
    facade_orientation = create_selectbox("Facade orientation", ["North", "East", "South", "West"])
    
    # Facade area
    facade_area = create_input_field("Facade area", min_value=0.0)
    
    # Facade thickness
    facade_thickness = create_input_field("Facade thickness", min_value=0.0)
    
    # Heating mode
    heating_mode = create_selectbox("Heating mode", ["None", "Central heating", "Radiators", "Underfloor heating", "Heat pump"])


elif page == 'Outdoor environmental parameters' :
    
    st.title('Outdoor environmental parameters')
    Season = "Season"
    st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Season}</span>", unsafe_allow_html=True)
    selectboxexample = st.selectbox(label="Season", label_visibility='collapsed', options=("Spring", "Summer", "Winter"))

    wind_speed = "wind speed"
    st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{wind_speed}</span>", unsafe_allow_html=True)
    wind_speed = st.number_input("wind speed", label_visibility='collapsed', min_value=0, format='%g')

    wind_direction = "wind direction"
    st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{wind_direction}</span>", unsafe_allow_html=True)
    selectboxexample = st.selectbox(label="wind direction", label_visibility='collapsed', options=("east", "west", "north","south"))

    air_temperature = "air temperature"
    st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{air_temperature}</span>", unsafe_allow_html=True)
    air_temperature = st.number_input("air temperature", label_visibility='collapsed', min_value=0, format='%g')

    relative_humidity = "relative humidity"
    st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{relative_humidity}</span>", unsafe_allow_html=True)
    relative_humidity = st.number_input("relative humidity", label_visibility='collapsed', min_value=0, format='%g')

    atmospherie_pressure = "atmospherie pressure"
    st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{atmospherie_pressure}</span>", unsafe_allow_html=True)
    atmospherie_pressure = st.number_input("atmospherie pressure", label_visibility='collapsed', min_value=0, format='%g')

    precipitation = "precipitation"
    st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{precipitation}</span>", unsafe_allow_html=True)
    precipitation = st.number_input("precipitation", label_visibility='collapsed', min_value=0, format='%g')

    solar_radiation = "solar radiation"
    st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{solar_radiation}</span>", unsafe_allow_html=True)
    solar_radiation = st.number_input("solar radiation", label_visibility='collapsed', min_value=0, format='%g')
    
    running_mean_temperature = "running_mean_temperature"
    st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{running_mean_temperature}</span>", unsafe_allow_html=True)
    running_mean_temperature = st.number_input("running mean temperature", label_visibility='collapsed', min_value=0, format='%g')
    













