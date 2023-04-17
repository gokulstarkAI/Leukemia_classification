# Importing
import streamlit as st
import tensorflow as tf

# Loading the model
model = tf.keras.models.load_model("/Users/gokul/Desktop/pythonProject/models/ALL_VGG16.h5")


# Function to make prediction on model
def predict(image):
    img = tf.keras.preprocessing.image.load_img(image, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Add batch dimension
    predictions = model.predict(img_array)
    if predictions[0][0] == 1.0:
        return "Benign", """A "Benign" condition refers to a growth or tumor that is not cancerous and does not 
        have the ability to spread to other parts of the body. Benign tumors are usually slow-growing and may not 
        cause any symptoms or health problems. However, they can become a concern if they grow and put pressure on 
        nearby tissues or organs, or if they affect the functioning of these structures."""
    elif predictions[0][1] == 1.0:
        return "Early", """This refers to cancer that is detected at an early stage, before it has spread to other 
        parts of the body. Early detection of cancer can improve treatment outcomes and increase the chances of a full 
        recovery."""
    elif predictions[0][2] == 1.0:
        return "Precancerous", """Precancerous conditions, also known as premalignant conditions, are abnormal cell 
        growths that have the potential to become cancerous. However, not all precancerous conditions will develop 
        into cancer."""
    elif predictions[0][3] == 1.0:
        return "Prognosis", """This refers to the likely outcome of a disease or condition. In the case of cancer, 
        prognosis may be influenced by a variety of factors, including the type and stage of cancer, 
        the patient's age and overall health, and the effectiveness of available treatments. A positive prognosis 
        suggests a favorable outcome, while a negative prognosis suggests a poorer outcome."""
    else:
        return "Unknown", ""


# Setting up streamlit webapp
st.set_page_config(
    page_title="Leukemia Image Classification",
    page_icon="🩸",
    layout="centered",
    initial_sidebar_state="expanded"
)
st.title("Leukemia Image Classification")
st.write("Let's diagnose your blood cells🩸! Upload an image below.")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "bmp", "png"])
# Make a prediction when the user clicks the 'Classify' button
if st.button('Classify 🔬'):
    # Check if an image has been uploaded
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image.')
        label, description = predict(uploaded_file)
        st.write(f"Diagnosis: **{label}**")
        st.write(description)
# st.write("This is a research tool not for actual diagnosis.")
# [theme]
# primaryColor="#c3efcd"
# backgroundColor="#f8f9fa"
# secondaryBackgroundColor="#d4edda"
# textColor="#212529"
# font="monospace"
