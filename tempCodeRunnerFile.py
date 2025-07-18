import streamlit as st
import pandas as pd
import pickle

# Load your saved Random Forest model
model = pickle.load(open('rf_model.pkl', 'rb'))

# Streamlit app title
st.title('Customer Churn Prediction')

st.write("""
This app predicts whether a customer will churn or not.
Please enter the customer details below:
""")

# Example inputs — replace with your dataset's real columns!
gender = st.selectbox('Gender', ['Male', 'Female'])
senior = st.selectbox('Senior Citizen', [0, 1])
partner = st.selectbox('Has Partner', ['Yes', 'No'])
dependents = st.selectbox('Has Dependents', ['Yes', 'No'])
tenure = st.slider('Tenure (months)', 0, 72, 1)
monthly_charges = st.number_input('Monthly Charges', 0.0, 500.0, step=1.0)

# Convert inputs to numeric if needed
partner = 1 if partner == 'Yes' else 0
dependents = 1 if dependents == 'Yes' else 0
gender = 1 if gender == 'Male' else 0

# Put inputs into a DataFrame (columns must match training data!)
input_data = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [senior],
    'Partner': [partner],
    'Dependents': [dependents],
    'tenure': [tenure],
    'MonthlyCharges': [monthly_charges]
})

# Predict button
if st.button('Predict Churn'):
    result = model.predict(input_data)
    st.write('Prediction:', 'Churn' if result[0] == 1 else 'No Churn')