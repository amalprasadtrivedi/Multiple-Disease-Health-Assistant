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
st.sidebar.markdown("### General Instructions:")
st.sidebar.markdown("1. Enter your health data in required column.")
st.sidebar.markdown("2. Click the 'Test Result' button.")
st.sidebar.markdown("3. View the health analysis results based on the provided data.")
st.sidebar.markdown("---")

# Sidebar navigation (Alternative to option_menu)
selected = st.sidebar.radio("Multiple Disease Prediction System", [
    'Diabetes Prediction',
    'Heart Disease Prediction',
    'Parkinsons Prediction'
])

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [float(x) if x.strip() else 0.0 for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    inputs = [st.text_input(label) for label in [
        'Age', 'Sex', 'Chest Pain types', 'Resting Blood Pressure', 'Serum Cholestoral in mg/dl', 'Fasting Blood Sugar > 120 mg/dl',
        'Resting Electrocardiographic results', 'Maximum Heart Rate achieved', 'Exercise Induced Angina', 'ST depression induced by exercise',
        'Slope of the peak exercise ST segment', 'Major vessels colored by flourosopy', 'Thal: 0 = normal; 1 = fixed defect; 2 = reversable defect'
    ]]
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [float(x) if x.strip() else 0.0 for x in inputs]
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
elif selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    inputs = [st.text_input(label) for label in [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ',
        'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA',
        'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]]
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [float(x) if x.strip() else 0.0 for x in inputs]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
    st.success(parkinsons_diagnosis)

st.sidebar.markdown(
    """
    <style>
        .full-width-button img {
            width: 100% !important;
        }
    </style>
    <a href="https://amalprasadtrivediportfolio.vercel.app/" target="_blank" class="full-width-button">
        <img src="https://img.shields.io/badge/Created%20by-Amal%20Prasad%20Trivedi-blue">
    </a>
    """,
    unsafe_allow_html=True
)
