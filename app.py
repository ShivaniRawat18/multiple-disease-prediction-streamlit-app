import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                  layout="wide",
                  page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
st.title("Multiple Disease Prediction System")
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.subheader('Diabetes Prediction')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1, format="%d")
        
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0, step=1, format="%d")
    
    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0, step=1, format="%d")
    
    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0, step=1, format="%d")
    
    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0, step=1, format="%d")
    
    with col3:
        BMI = st.number_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.number_input('Age of the Person', min_value=0, step=1, format="%d")
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        # Example conversion with fallback or error handling
        
             

#        diab_prediction = diabetes_model.predict([[int(Pregnancies), int(Glucose), int(BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])


        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.subheader('Heart Disease Prediction')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', value=None)
        
    with col2:
        sex = st.number_input('Sex', value=None)
        
    with col3:
        cp = st.number_input('Chest Pain types', value=None)
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure', value=None)
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl', value=None)
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl', value=None)
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results', value=None)
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved', value=None)
        
    with col3:
        exang = st.number_input('Exercise Induced Angina', value=None)
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise', value=None)
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment', value=None)
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy', value=None)
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', value=None)
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        #heart_prediction = heart_disease_model.predict(int(age), int(sex), int(cp), float(trestbps), float(chol), int(fbs), int(restecg), float(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal))

        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
        st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.subheader("Parkinson's Disease Prediction")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', format="%.6f", value=None)
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', format="%.6f", value=None)
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', format="%.6f", value=None)
        
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)', format="%.6f", value=None)
        
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', format="%.6f", value=None)
        
    with col1:
        RAP = st.number_input('MDVP:RAP', format="%.6f", value=None)
        
    with col2:
        PPQ = st.number_input('MDVP:PPQ', format="%.6f", value=None)
        
    with col3:
        DDP = st.number_input('Jitter:DDP', format="%.6f", value=None)
        
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer', format="%.6f", value=None)
        
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', format="%.6f", value=None)
        
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3', format="%.6f", value=None)
        
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5', format="%.6f", value=None)
        
    with col3:
        APQ = st.number_input('MDVP:APQ', format="%.6f", value=None)
        
    with col4:
        DDA = st.number_input('Shimmer:DDA', format="%.6f", value=None)
        
    with col5:
        NHR = st.number_input('NHR', format="%.6f", value=None)
        
    with col1:
        HNR = st.number_input('HNR', format="%.6f", value=None)
        
    with col2:
        RPDE = st.number_input('RPDE', format="%.6f", value=None)
        
    with col3:
        DFA = st.number_input('DFA', format="%.6f", value=None)
        
    with col4:
        spread1 = st.number_input('spread1', format="%.6f", value=None)
        
    with col5:
        spread2 = st.number_input('spread2', format="%.6f", value=None)
        
    with col1:
        D2 = st.number_input('D2', format="%.6f", value=None)
        
    with col2:
        PPE = st.number_input('PPE', format="%.6f", value=None)

    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (float(parkinsons_prediction[0]) == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
        st.success(parkinsons_diagnosis)

def set_bg_from_url(url, opacity=1):
    
    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
            
     
    </footer>
"""
    st.markdown(footer, unsafe_allow_html=True)
    
    
    # Set background image using HTML and CSS
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image from URL
set_bg_from_url("https://media.licdn.com/dms/image/v2/D5622AQHIvcmdIx7OAA/feedshare-shrink_1280/B56ZX.BZLBGQAo-/0/1743723533545?e=2147483647&v=beta&t=5r3qSEgOGpvvmo5gTezUb8ggFkG1fnCASyUGxkGWHno", opacity=0.875)
