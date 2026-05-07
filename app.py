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
    st.title("🏠 Welcome to S.O.P.H.I.E. Health Assistant")

    st.markdown(
        """
        ## 🌟 About the Health Assistant
        Welcome to **S.O.P.H.I.E. Health Assistant**, an advanced AI-powered healthcare tool designed to provide preliminary health assessments.
        Our system leverages **Machine Learning** models to predict the likelihood of three major diseases:
    
        - 🩸 **Diabetes Prediction**
        - ❤️ **Heart Disease Prediction**
        - 🧠 **Parkinson's Disease Prediction**
    
        This tool is developed as a part of the **Series One Processor Hyper Intelligence Encryptor (S.O.P.H.I.E.)**, ensuring accuracy, reliability, and ease of use.
        """
    )

    st.markdown(
        """
        ## 🔬 How It Works?
        1. **Select a disease prediction model** from the left sidebar.
        2. **Enter the required health parameters** in the provided input fields.
        3. **Click the 'Test Result' button** to get a preliminary analysis based on machine learning predictions.
        4. **Interpret the results** and consult a healthcare professional for further diagnosis.
        """
    )

# Diabetes Prediction Page
elif selected == 'Diabetes Prediction':
    # Title and Introduction
    st.title("🩺 Diabetes Prediction using Machine Learning")
    st.markdown("""
    ### Understanding Diabetes
    Diabetes is a chronic health condition that affects how your body turns food into energy. It occurs when your body either doesn't produce enough insulin or can't effectively use the insulin it produces.
    There are two main types of diabetes:
    - **Type 1 Diabetes:** The body stops producing insulin.
    - **Type 2 Diabetes:** The body becomes resistant to insulin.

    With early diagnosis and proper management, diabetes can be controlled, reducing risks of severe health complications like heart disease, kidney failure, and nerve damage.

    ### Input Parameters and Their Importance
    This prediction system takes the following inputs to assess the likelihood of diabetes:

    1. **Pregnancies 🤰** - Number of times a woman has been pregnant.
       - Range: 0 - 17
    2. **Glucose Level 🩸** - Blood sugar concentration.
       - Normal: 70-99 mg/dL
       - Prediabetes: 100-125 mg/dL
       - Diabetes: 126+ mg/dL
    3. **Blood Pressure 💓** - Pressure of circulating blood against vessel walls.
       - Normal: <120/80 mmHg
       - Hypertension: >130/80 mmHg
    4. **Skin Thickness 📏** - Measures subcutaneous fat using a caliper.
       - Normal: 10-50 mm
    5. **Insulin Level 💉** - Insulin in the blood.
       - Normal: 16-166 µIU/mL
    6. **BMI (Body Mass Index) ⚖️** - Weight in relation to height.
       - Normal: 18.5 - 24.9
       - Overweight: 25 - 29.9
       - Obese: 30+
    7. **Diabetes Pedigree Function 🧬** - Indicates genetic risk based on family history.
       - Higher values indicate a greater likelihood of diabetes.
    8. **Age 🎂** - Age of the individual.
       - Higher age increases diabetes risk.
    
    ---
    
    ### Enter Your Health Data
    """)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('🤰 Number of Pregnancies')
        SkinThickness = st.text_input('📏 Skin Thickness value (mm)')
        DiabetesPedigreeFunction = st.text_input('🧬 Diabetes Pedigree Function')
    with col2:
        Glucose = st.text_input('🩸 Glucose Level (mg/dL)')
        Insulin = st.text_input('💉 Insulin Level (µIU/mL)')
        Age = st.text_input('🎂 Age of the Person')
    with col3:
        BloodPressure = st.text_input('💓 Blood Pressure (mmHg)')
        BMI = st.text_input('⚖️ BMI value')

    # Prediction and Result
    diab_diagnosis = ''
    if st.button('🧪 Diabetes Test Result'):
        user_input = [float(x) if x.strip() else 0.0 for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = '✅ The person is NOT diabetic' if diab_prediction[0] == 0 else '⚠️ The person IS diabetic'
        st.success(diab_diagnosis)

    st.markdown("""
    ### Understanding the Result
    - If the result indicates **'The person is NOT diabetic'**, it suggests that your provided health parameters are within a normal range.
    - If the result indicates **'The person IS diabetic'**, you should consult a healthcare professional for further testing and lifestyle modifications.
    
    ### Preventive Measures 🏃‍♂️🥗
    - Maintain a **healthy diet** with fiber-rich foods.
    - Exercise **regularly** to control blood sugar.
    - Monitor **blood glucose levels** frequently.
    - Avoid excessive **sugar and processed food** intake.
    - Manage **stress** and maintain a good sleep cycle.

    🩺 **Early detection can prevent complications. Stay informed and take care of your health!**
    """)

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    # Heart Disease Prediction Page
    st.title('❤️ Heart Disease Prediction using Machine Learning')
    st.markdown("""
    ### Introduction
    Heart disease refers to a range of conditions that affect the heart, including blood vessel diseases, heart rhythm problems, and congenital heart defects. It is one of the leading causes of death worldwide, making early detection crucial. This AI-powered tool assists in predicting heart disease risks based on user-input health parameters.

    #### How It Works:
    - Enter your health parameters.
    - Click the 'Test Result' button.
    - View the prediction results.
    
    ---
    ### Parameters and Their Ranges
    Below are the 13 parameters used to predict heart disease:
    
    1. **Age (years)**: The person's age (e.g., 29-77).
    2. **Sex (0 = Female, 1 = Male)**: Biological sex of the individual.
    3. **Chest Pain Type (0-3)**: The type of chest pain experienced:
       - 0: Typical Angina (predictable pain on exertion)
       - 1: Atypical Angina (unpredictable pain)
       - 2: Non-anginal pain (not related to the heart)
       - 3: Asymptomatic (no pain)
    4. **Resting Blood Pressure (mmHg)**: The resting blood pressure level (94-200 mmHg).
    5. **Serum Cholesterol (mg/dl)**: The cholesterol level in the blood (126-564 mg/dl).
    6. **Fasting Blood Sugar (> 120 mg/dl, 0 = No, 1 = Yes)**: Indicates whether fasting blood sugar is higher than 120 mg/dl.
    7. **Resting Electrocardiographic Results (0-2)**: Evaluates heart's electrical activity:
       - 0: Normal
       - 1: ST-T wave abnormality
       - 2: Left ventricular hypertrophy
    8. **Maximum Heart Rate Achieved (bpm)**: Maximum heart rate during stress test (71-202 bpm).
    9. **Exercise Induced Angina (0 = No, 1 = Yes)**: Indicates whether chest pain is triggered by physical exertion.
    10. **Oldpeak (ST Depression)**: ST segment depression induced by exercise relative to rest (0-6.2).
    11. **Slope of Peak Exercise ST Segment (0-2)**: Measures the slope of the ST segment:
       - 0: Upsloping
       - 1: Flat
       - 2: Downsloping
    12. **Number of Major Vessels Colored by Fluoroscopy (0-4)**: The number of blood vessels (0-4) detected by fluoroscopy.
    13. **Thalassemia (0-3)**: A blood disorder classification:
       - 0: Normal
       - 1: Fixed defect (permanent damage)
       - 2: Reversible defect (risk present but reversible)

    ---
    ### Input Your Health Data
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('📅 Age', placeholder='Enter your age')
        Sex = st.selectbox('⚥ Sex', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
        ChestPain = st.selectbox('💔 Chest Pain Type', options=[0, 1, 2, 3], 
                                 format_func=lambda x: ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'][x])
        RestingBP = st.text_input('🩸 Resting Blood Pressure (mmHg)', placeholder='Enter your BP value')
        Thal = st.selectbox('🧬 Thalassemia Type', options=[0, 1, 2, 3], 
                            format_func=lambda x: ['Normal', 'Fixed Defect', 'Reversible Defect', 'Unknown'][x])

    with col2:
        Cholesterol = st.text_input('🥩 Serum Cholesterol (mg/dl)', placeholder='Enter cholesterol level')
        FastingBS = st.selectbox('🧪 Fasting Blood Sugar > 120 mg/dl', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
        RestECG = st.selectbox('📉 Resting ECG Results', options=[0, 1, 2], 
                               format_func=lambda x: ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'][x])
        MaxHR = st.text_input('❤️ Maximum Heart Rate Achieved (bpm)', placeholder='Enter max HR')

    with col3:
        ExerciseAngina = st.selectbox('🏃‍♂️ Exercise Induced Angina', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
        Oldpeak = st.text_input('📉 Oldpeak (ST Depression)', placeholder='Enter Oldpeak value')
        Slope = st.selectbox('📈 Slope of Peak ST Segment', options=[0, 1, 2], 
                             format_func=lambda x: ['Upsloping', 'Flat', 'Downsloping'][x])
        MajorVessels = st.text_input('🩸 Major Vessels Colored by Fluoroscopy (0-4)', placeholder='Enter number of vessels')

    heart_diagnosis = ''
    if st.button('🔍 Heart Disease Test Result'):
        user_input = [float(Age), int(Sex), int(ChestPain), float(RestingBP), float(Cholesterol), int(FastingBS), 
                      int(RestECG), float(MaxHR), int(ExerciseAngina), float(Oldpeak), int(Slope), float(MajorVessels), int(Thal)]
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = '🚨 The person is at risk of heart disease!' if heart_prediction[0] == 1 else '✅ No heart disease detected!'
        st.success(heart_diagnosis)

    st.markdown("""
    ---
    ### Precautions & Recommendations
    If you are at risk of heart disease, consider the following:
    - **Healthy Diet**: Eat fruits, vegetables, and low-fat foods.
    - **Regular Exercise**: Engage in at least 30 minutes of moderate exercise daily.
    - **Routine Check-ups**: Visit a cardiologist for regular monitoring.
    - **Avoid Smoking & Alcohol**: These habits increase cardiovascular risk.
    - **Manage Stress**: Practice relaxation techniques like meditation and deep breathing.

    💙 Stay heart-healthy and prioritize your well-being!
    """)

# Parkinson's Prediction Page
elif selected == "Parkinson's Prediction":
    # Title and Introduction
    st.title("🧠 Parkinson's Disease Prediction using Machine Learning")
    st.markdown("""
    ## Understanding Parkinson’s Disease
    
    Parkinson’s disease is a progressive neurological disorder that affects movement. It occurs due to the loss of dopamine-producing neurons in the brain, leading to tremors, stiffness, and difficulty with balance and coordination. Early detection can help in managing symptoms effectively.
    
    This prediction model uses machine learning algorithms to analyze various voice and movement-related parameters to determine the likelihood of Parkinson’s disease.
    
    ## Parameters Considered for Prediction
    Each of the following parameters is derived from voice recordings and movement analysis, helping in detecting subtle changes associated with Parkinson’s disease.
    """)
    
    st.markdown("---")

    # Explanation of Parameters
    st.subheader("📌 Understanding the Parameters")
    st.markdown("""
    - **MDVP Fo, Fhi, Flo (Hz):** These measure the fundamental frequency of the voice, which tends to be unstable in Parkinson’s patients.
    - **Jitter (%) and Jitter (Abs):** Jitter quantifies variations in voice frequency. Increased jitter values indicate a higher probability of Parkinson’s disease.
    - **Shimmer & Shimmer dB:** These parameters reflect amplitude variations in speech, which may indicate vocal instability.
    - **NHR & HNR:** Noise-to-Harmonics Ratio (NHR) measures the proportion of noise in the voice, while HNR measures the harmonic strength relative to noise.
    - **RPDE & DFA:** RPDE evaluates the predictability of voice signals, and DFA assesses the complexity of speech patterns.
    - **Spread 1 & Spread 2:** These parameters indicate variations in speech waveforms.
    - **D2 & PPE:** D2 measures the complexity of voice modulation, and PPE evaluates entropy levels in speech frequency.

    Each of these parameters plays a crucial role in identifying vocal impairments associated with Parkinson’s disease.
    """)

    st.markdown("---")

    # Input Fields for Prediction
    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo = st.text_input("🔊 MDVP: Fundamental Frequency (Fo) in Hz", placeholder="Enter value (range: 88-260 Hz)")
        MDVP_Fhi = st.text_input("🔊 MDVP: Highest Frequency (Fhi) in Hz", placeholder="Enter value (range: 100-592 Hz)")
        MDVP_Flo = st.text_input("🔊 MDVP: Lowest Frequency (Flo) in Hz", placeholder="Enter value (range: 65-239 Hz)")
        MDVP_Jitter_Percent = st.text_input("📈 MDVP: Jitter (%)", placeholder="Enter value (range: 0.001-0.03%)")
        MDVP_Jitter_Abs = st.text_input("📉 MDVP: Jitter (Abs)", placeholder="Enter value (range: 0.00001-0.0002)")
        Jitter_DDP = st.text_input("📊 Jitter: DDP", placeholder="Enter value (range: 0.0001-0.02)")
        MDVP_Shimmer = st.text_input("🔎 MDVP: Shimmer", placeholder="Enter value (range: 0.01-0.1)")
        MDVP_Shimmer_dB = st.text_input("🔎 MDVP: Shimmer (dB)", placeholder="Enter value (range: 0.1-3.0 dB)")

    with col2:
        Shimmer_APQ3 = st.text_input("📌 Shimmer: APQ3", placeholder="Enter value (range: 0.01-0.08)")
        Shimmer_APQ5 = st.text_input("📌 Shimmer: APQ5", placeholder="Enter value (range: 0.01-0.1)")
        MDVP_APQ = st.text_input("📌 MDVP: APQ", placeholder="Enter value (range: 0.01-0.1)")
        Shimmer_DDA = st.text_input("📌 Shimmer: DDA", placeholder="Enter value (range: 0.01-0.08)")
        NHR = st.text_input("🔄 Noise-to-Harmonics Ratio (NHR)", placeholder="Enter value (range: 0.01-0.3)")
        HNR = st.text_input("🔄 Harmonics-to-Noise Ratio (HNR)", placeholder="Enter value (range: 8-35 dB)")
        RPDE = st.text_input("📡 Recurrence Period Density Entropy (RPDE)", placeholder="Enter value (range: 0.2-0.6)")
        DFA = st.text_input("📡 Detrended Fluctuation Analysis (DFA)", placeholder="Enter value (range: 0.5-0.9)")

    with col3:
        spread1 = st.text_input("📉 Spread 1", placeholder="Enter value (range: -8 to -2)")
        spread2 = st.text_input("📉 Spread 2", placeholder="Enter value (range: 0.01-0.5)")
        D2 = st.text_input("🔍 Correlation Dimension (D2)", placeholder="Enter value (range: 1-3)")
        PPE = st.text_input("📌 Pitch Period Entropy (PPE)", placeholder="Enter value (range: 0.02-0.5)")

    st.markdown("---")

    # Prediction Button
    parkinsons_diagnosis = ""
    if st.button("🧠 Predict Parkinson's Disease"):
        user_input = [float(x) if x.strip() else 0.0 for x in [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter_Percent, MDVP_Jitter_Abs, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        parkinsons_diagnosis = "🔴 The person has Parkinson's disease." if parkinsons_prediction[0] == 1 else "🟢 The person does not have Parkinson's disease."
        st.success(parkinsons_diagnosis)

st.markdown("---")

st.markdown("""
### ⚠️ Disclaimer
This prediction model is not a substitute for professional medical advice. Please consult a healthcare provider for an accurate diagnosis and treatment.
""")

# Footer with creator info
st.sidebar.markdown(
    """
    <style>
        .sidebar-button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
        }
        .sidebar-button img {
            width: 100%;
            max-width: 250px; /* Adjust max-width as needed */
        }
    </style>
    <div class="sidebar-button-container">
        <a href="https://amalprasadtrivediportfolio.vercel.app/" target="_blank" class="sidebar-button">
            <img src="https://img.shields.io/badge/Created%20by-AMAL%20PRASAD%20TRIVEDI-blue">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
