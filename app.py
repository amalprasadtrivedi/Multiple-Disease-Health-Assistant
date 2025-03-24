import os
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Loading the saved models
diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('saved_models/parkinsons_model.sav', 'rb'))

# Sidebar
st.sidebar.title("S.O.P.H.I.E. Health Assistant")
st.sidebar.info("This is the Health Assistant module of the Series One Processor Hyper Intelligence Encryptor (S.O.P.H.I.E.). Please use it responsibly.")
st.sidebar.markdown("---")

# Sidebar navigation with Home Page
tabs = ["Home", "Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"]
selected = st.sidebar.radio("Multiple Disease Prediction System", tabs)

if selected == "Home":
    st.title("Welcome to S.O.P.H.I.E. Health Assistant")
    st.write("""
    **About the System:**
    This Health Assistant module is designed to predict the likelihood of three diseases based on user-provided health parameters using trained machine learning models.
    
    ### Available Health Predictions:
    1. **Diabetes Prediction**: Predicts the likelihood of diabetes using factors like glucose level, insulin, and BMI.
    2. **Heart Disease Prediction**: Analyzes heart health based on cholesterol, blood pressure, and other key indicators.
    3. **Parkinson's Prediction**: Detects signs of Parkinson’s disease using voice-based features like jitter and shimmer.
    
    Please navigate to the respective sections from the sidebar to perform a health analysis.
    """)

# Diabetes Prediction Page
elif selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    st.write("""
    **About Diabetes:**
    Diabetes is a chronic condition that affects how the body processes blood sugar (glucose). If left unmanaged, it can lead to severe complications.
    
    **Health Parameters:**
    - **Pregnancies**: Number of times pregnant
    - **Glucose**: Blood sugar level (70-130 mg/dL)
    - **Blood Pressure**: Systolic pressure (80-120 mmHg)
    - **BMI**: Body Mass Index (18.5-24.9 is normal)
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        Glucose = st.text_input('Glucose Level')
        BloodPressure = st.text_input('Blood Pressure')
    with col2:
        BMI = st.text_input('BMI')
        Insulin = st.text_input('Insulin Level')
        Age = st.text_input('Age')
    
    if st.button('Diabetes Test Result'):
        user_input = [float(x) if x.strip() else 0.0 for x in [Pregnancies, Glucose, BloodPressure, BMI, Insulin, Age]]
        prediction = diabetes_model.predict([user_input])
        st.success('Diabetic' if prediction[0] == 1 else 'Not Diabetic')

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    st.write("""
    **About Heart Disease:**
    Heart disease refers to conditions affecting the heart, such as coronary artery disease, heart attacks, and arrhythmias.
    
    **Health Parameters:**
    - **Age**: Age of the individual
    - **Cholesterol**: Serum cholesterol (below 200 mg/dL is desirable)
    - **Resting Blood Pressure**: Normal range (90-120 mmHg)
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        Age = st.text_input('Age')
        Cholesterol = st.text_input('Cholesterol Level')
        RestingBP = st.text_input('Resting Blood Pressure')
    with col2:
        MaxHR = st.text_input('Maximum Heart Rate')
        ExerciseAngina = st.text_input('Exercise Induced Angina (0/1)')
        MajorVessels = st.text_input('Major vessels colored by fluoroscopy')
    
    if st.button('Heart Disease Test Result'):
        user_input = [float(x) if x.strip() else 0.0 for x in [Age, Cholesterol, RestingBP, MaxHR, ExerciseAngina, MajorVessels]]
        prediction = heart_disease_model.predict([user_input])
        st.success('Heart Disease Detected' if prediction[0] == 1 else 'No Heart Disease')

# Parkinson's Prediction Page
elif selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    st.write("""
    **About Parkinson's Disease:**
    Parkinson's is a neurodegenerative disorder that affects movement. Symptoms include tremors, stiffness, and difficulty with balance.
    
    **Health Parameters:**
    - **MDVP Fo(Hz)**: Fundamental frequency of voice
    - **Jitter (%)**: Variation in voice frequency
    - **Shimmer (dB)**: Variation in voice amplitude
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
        Jitter_Percent = st.text_input('Jitter(%)')
    with col2:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
        HNR = st.text_input('Harmonic to Noise Ratio')
    
    if st.button("Parkinson's Test Result"):
        user_input = [float(x) if x.strip() else 0.0 for x in [MDVP_Fo, Jitter_Percent, MDVP_Shimmer, HNR]]
        prediction = parkinsons_model.predict([user_input])
        st.success("Parkinson's Detected" if prediction[0] == 1 else "No Parkinson's")

# Footer with creator info
st.sidebar.markdown(
    """
    <a href="https://amalprasadtrivediportfolio.vercel.app/" target="_blank">
        <img src="https://img.shields.io/badge/Created%20by-Amal%20Prasad%20Trivedi-blue">
    </a>
    """,
    unsafe_allow_html=True
)
