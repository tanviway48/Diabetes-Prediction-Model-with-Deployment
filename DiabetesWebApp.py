import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open("diabetes_trained_model.sav", 'rb'))

# Define the function for prediction
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

# Define the main function
def main():
    # Adding background color and styling
    st.markdown("""
        <style>
        body {
            background-color: yellow;
        }
        .main {
            background-color: #EEDF7A;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        input {
            border: 30px solid #098098;
            border-radius: 5px;
            padding: 8px;
            width: 100%;
        }
        .stTextInput input {
            background-color: #e8f0fe;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 20px;
            padding: 10px;
            border-radius: 5px;
            font-weight:500;
            width: 100%;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .diagnosis-result {
            font-size: 24px;
            color: black;
            font-weight: bold;
            padding: 10px;
            background-color: #697565;
            border-radius: 10px;
            text-align: center;
            margin-top: 20px;
        }
        .custom-label {
            color: black;
            font-size: 20px;
            font-weight:bold;
            margin: 3px;
        }
        .hidden-label input {
            border: none;
        }
        </style>
        """, unsafe_allow_html=True)

    # Adding title 
    st.markdown(
        "<h1 style='text-align: center; color: #4CAF50;'>Diabetes Prediction System</h1>", 
        unsafe_allow_html=True
    )

    # Display image
    st.image("img.jpg", caption="Diabetes Prediction", use_column_width=True)

    # Input fields for the user 
    st.markdown("<p class='custom-label'>Number of Pregnancies</p>", unsafe_allow_html=True)
    Pregnancies = st.text_input("", key="Pregnancies", label_visibility="hidden")

    st.markdown("<p class='custom-label'>Glucose Level</p>", unsafe_allow_html=True)
    Glucose = st.text_input("", key="Glucose", label_visibility="hidden")

    st.markdown("<p class='custom-label'>BP Value</p>", unsafe_allow_html=True)
    BloodPressure = st.text_input("", key="BloodPressure", label_visibility="hidden")

    st.markdown("<p class='custom-label'>Skin Thickness Value</p>", unsafe_allow_html=True)
    SkinThickness = st.text_input("", key="SkinThickness", label_visibility="hidden")

    st.markdown("<p class='custom-label'>Insulin Level</p>", unsafe_allow_html=True)
    Insulin = st.text_input("", key="Insulin", label_visibility="hidden")

    st.markdown("<p class='custom-label'>BMI Value</p>", unsafe_allow_html=True)
    BMI = st.text_input("", key="BMI", label_visibility="hidden")

    st.markdown("<p class='custom-label'>Diabetes Pedigree Function Value</p>", unsafe_allow_html=True)
    DiabetesPedigreeFunction = st.text_input("", key="DiabetesPedigreeFunction", label_visibility="hidden")

    st.markdown("<p class='custom-label'>Enter Your Age</p>", unsafe_allow_html=True)
    Age = st.text_input("", key="Age", label_visibility="hidden")

    # Code for prediction
    diagnosis = ''

    # Button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

    # Displaying the result 
    st.markdown(f"<p class='diagnosis-result' style='text-align: center;'>{diagnosis}</p>", unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()


