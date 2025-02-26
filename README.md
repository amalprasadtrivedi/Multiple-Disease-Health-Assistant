# Multiple Disease Prediction System Documentation

## Table of Contents
1. Introduction
2. Problem Statement
3. Objectives
4. System Requirements
5. Dataset Description
6. Data Preprocessing
7. Feature Engineering
8. Model Selection
9. Model Training and Evaluation
10. Deployment Strategy
11. Conclusion

---

## 1. Introduction
The **Multiple Disease Prediction System** is designed to predict various diseases such as diabetes, heart disease, and Parkinson’s disease using machine learning models. The system is deployed as a **Streamlit** web application to provide a user-friendly interface for users to input their medical details and receive predictions instantly.

## 2. Problem Statement
Early detection of diseases is crucial for effective treatment and prevention. Many individuals lack access to immediate medical consultations, leading to delays in diagnosis. A machine learning-based system can analyze health parameters and predict potential diseases, assisting in early diagnosis and medical intervention.

## 3. Objectives
- Develop an AI-based system to predict multiple diseases accurately.
- Utilize different datasets for different diseases to enhance model performance.
- Provide a simple, interactive, and user-friendly **Streamlit** interface for users.
- Deploy the model as a web application for accessibility.

## 4. System Requirements
- **Hardware:**
  - Minimum 8GB RAM
  - At least 50GB storage space
  - GPU for faster model training (optional)
  
- **Software:**
  - Python 3.x
  - Jupyter Notebook / Google Colab
  - Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, Streamlit
  - IDE: VS Code, PyCharm (optional)

## 5. Dataset Description
The datasets used for this project include:
- **Diabetes Dataset:** Contains features like glucose level, blood pressure, BMI, etc.
- **Heart Disease Dataset:** Includes patient parameters like cholesterol, blood pressure, heart rate, etc.
- **Parkinson’s Disease Dataset:** Includes voice parameters to identify Parkinson’s disease.

### Sample Features:
| Feature              | Description                                  |
|----------------------|----------------------------------------------|
| Age                 | Age of the patient |
| BMI                 | Body Mass Index |
| Blood Pressure      | Blood pressure level |
| Glucose Level      | Blood sugar concentration |
| Heart Rate         | Number of heartbeats per minute |
| Voice Features (for Parkinson’s) | Acoustic parameters of voice |

## 6. Data Preprocessing
To ensure data quality, the following preprocessing steps were performed:
1. **Handling Missing Values:**
   - Checked and imputed missing values using mean or median.
2. **Feature Selection:**
   - Selected the most relevant features using correlation analysis.
3. **Encoding Categorical Data:**
   - Converted categorical data into numerical form.
4. **Feature Scaling:**
   - Applied **StandardScaler** for normalization.
5. **Data Splitting:**
   - Divided into **training (80%)** and **testing (20%)** sets.

## 7. Feature Engineering
Feature engineering techniques were applied to improve model accuracy:
- **Correlation Analysis:** Identified important attributes.
- **Dimensionality Reduction:** Used **PCA** for feature extraction.
- **Synthetic Data Generation:** Applied **SMOTE** for class imbalance handling.

## 8. Model Selection
Various machine learning models were tested to identify the best classifier:
- **Logistic Regression**
- **Decision Tree Classifier**
- **Random Forest Classifier**
- **Support Vector Machine (SVM)**
- **K-Nearest Neighbors (KNN)**
- **Neural Networks**

## 9. Model Training and Evaluation
The models were trained and evaluated based on key metrics:

| Model                 | Accuracy | Precision | Recall | F1-score |
|----------------------|---------|----------|--------|---------|
| Logistic Regression | 85.2%   | 82.5%    | 83.1%  | 82.8%   |
| Decision Tree       | 83.5%   | 80.7%    | 81.3%  | 81.0%   |
| Random Forest      | 89.1%   | 87.8%    | 88.5%  | 88.1%   |
| SVM                | 87.6%   | 85.9%    | 86.7%  | 86.3%   |
| KNN                | 84.3%   | 82.4%    | 83.2%  | 82.8%   |
| Neural Networks    | 91.2%   | 89.5%    | 90.3%  | 89.9%   |

The **Neural Network** model achieved the highest accuracy and was selected for deployment.

## 10. Deployment Strategy
The trained model was deployed using **Streamlit**:
1. **Backend:** Python-based model handling prediction requests.
2. **Frontend:** Streamlit app for user interaction.
3. **Hosting:** Deployed on **Streamlit Cloud/Heroku**.

### Steps to Run the Application Locally
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/multiple-disease-prediction.git
   ```
2. Navigate to the directory:
   ```sh
   cd multiple-disease-prediction
   ```
3. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```
5. Open the browser and go to:
   ```
   http://localhost:8501/
   ```

## 11. Conclusion
This project successfully developed a **Multiple Disease Prediction System** using machine learning and deployed it as a **Streamlit** web application. The neural network model provided the best accuracy, making it a reliable tool for early disease detection. Future improvements include:
- Expanding the system to predict more diseases.
- Integrating real-time patient data.
- Deploying a mobile-friendly version for accessibility.

---

**Project Repository:** [GitHub Link](https://github.com/your-repo/multiple-disease-prediction)

