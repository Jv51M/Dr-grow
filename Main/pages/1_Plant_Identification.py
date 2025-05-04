import streamlit as st
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model # type: ignore
import numpy as np
import cv2
import pandas as pd
import time

# Load the dataset
df = pd.read_excel(r"C:\Mini_Project\Main\Care dataset.xlsx")

# Load the model (do this once at startup)
model = load_model(r"C:\Mini_Project\Main\model_saved\2025-03-20-21-54-37\dr_grow_newdataset.keras")
class_names = ['Curry leaf', 'Neem', 'Potato', 'Pumpkin', 'Cucumber', 'Lemon', 'Tomato']

def preprocess_image(uploaded_file):
    # Read the file as bytes and convert to numpy array
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Resize and convert to grayscale
    img = cv2.resize(img, (256, 256))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.expand_dims(gray/255, 0)
    
    return img, gray

def identify_plant(uploaded_file):
    img, gray = preprocess_image(uploaded_file)
    
    ypred = model.predict(gray)
    ypred = np.argmax(ypred, axis=1)
    op = int(ypred.item())
    keyword = class_names[op]
    
    return keyword, img

def show_plant_care(keyword):
    st.title('Plant Care')
    
    matching_rows = df[df["PlantName"].astype(str) == keyword]

    if not matching_rows.empty:
        for _, row in matching_rows.iterrows():
            st.write(f"**Plant Name:** {row['PlantName']}")
            st.write(f"**Watering Frequency:** {row['WateringFrequency']}")
            st.write(f"**Sunlight Needs:** {row['SunlightNeeds']}")
            st.write(f"**Soil Type:** {row['SoilType']}")
            st.write(f"**Special Care:** {row['SpecialCare']}")
    else:
        st.error("No matching plant found.")

def main():
    st.set_page_config(page_title="Dr.Grow", page_icon="🌱")
    
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'main'
    if 'uploaded_file' not in st.session_state:
        st.session_state.uploaded_file = None
    if 'keyword' not in st.session_state:
        st.session_state.keyword = None
    if 'plant_image' not in st.session_state:
        st.session_state.plant_image = None
    
    # Main page
    if st.session_state.page == 'main':
        st.title("Dr.Grow")
        
        # File uploader
        uploaded_file = st.file_uploader("Upload an image of a plant leaf", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            st.session_state.uploaded_file = uploaded_file
            
            # Identify the plant
            with st.spinner('Identifying plant...'):
                try:
                    keyword, img = identify_plant(uploaded_file)
                    st.session_state.keyword = keyword
                    st.session_state.plant_image = img
                    time.sleep(2)  # Simulate processing time
                    st.session_state.page = 'identification'
                    st.rerun()
                except Exception as e:
                    st.error(f"Error processing image: {str(e)}")
    
    # Identification page
    elif st.session_state.page == 'identification':
        st.title('Leaf Classification')
        
        # Display the image and result
        st.image(st.session_state.plant_image, channels="BGR")
        st.success(f"Identified as: {st.session_state.keyword}")
        
        if st.button("Next"):
            st.session_state.page = 'care'
            st.rerun()
    
    # Plant care page
    elif st.session_state.page == 'care':
        show_plant_care(st.session_state.keyword)
        
        if st.button("Back to Main"):
            st.session_state.page = 'main'
            st.session_state.uploaded_file = None
            st.session_state.keyword = None
            st.session_state.plant_image = None
            st.rerun()

if __name__ == "__main__":
    main()