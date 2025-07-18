import streamlit as st
import pandas as pd
import pickle

# Load your trained model
model = pickle.load(open('rf_model.pkl', 'rb'))

st.title('Customer Churn Prediction')

# Inputs
gender = st.selectbox('Gender', ['Male', 'Female'])
partner = st.selectbox('Partner', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['Yes', 'No'])
phone_service = st.selectbox('Phone Service', ['Yes', 'No'])
multiple_lines = st.selectbox('Multiple Lines', ['Yes', 'No'])
internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
online_security = st.selectbox('Online Security', ['Yes', 'No'])
online_backup = st.selectbox('Online Backup', ['Yes', 'No'])
device_protection = st.selectbox('Device Protection', ['Yes', 'No'])
tech_support = st.selectbox('Tech Support', ['Yes', 'No'])
streaming_tv = st.selectbox('Streaming TV', ['Yes', 'No'])
streaming_movies = st.selectbox('Streaming Movies', ['Yes', 'No'])
contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
paperless_billing = st.selectbox('Paperless Billing', ['Yes', 'No'])
payment_method = st.selectbox(
    'Payment Method',
    ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
)
senior = st.selectbox('Senior Citizen', [0, 1])
tenure = st.slider('Tenure (months)', 0, 72, 1)
monthly_charges = st.number_input('Monthly Charges', 0.0, 500.0, step=1.0)
total_charges = st.number_input('Total Charges', 0.0, 10000.0, step=1.0)

# Encode binary
gender = 1 if gender == 'Male' else 0
partner = 1 if partner == 'Yes' else 0
dependents = 1 if dependents == 'Yes' else 0
phone_service = 1 if phone_service == 'Yes' else 0
multiple_lines = 1 if multiple_lines == 'Yes' else 0
online_security = 1 if online_security == 'Yes' else 0
online_backup = 1 if online_backup == 'Yes' else 0
device_protection = 1 if device_protection == 'Yes' else 0
tech_support = 1 if tech_support == 'Yes' else 0
streaming_tv = 1 if streaming_tv == 'Yes' else 0
streaming_movies = 1 if streaming_movies == 'Yes' else 0
paperless_billing = 1 if paperless_billing == 'Yes' else 0

# Encode multi-category
# IMPORTANT: These must match how you encoded them in training!

# InternetService
if internet_service == 'DSL':
    internet_service = 0
elif internet_service == 'Fiber optic':
    internet_service = 1
else:
    internet_service = 2

# Contract
if contract == 'Month-to-month':
    contract = 0
elif contract == 'One year':
    contract = 1
else:
    contract = 2

# PaymentMethod
if payment_method == 'Electronic check':
    payment_method = 0
elif payment_method == 'Mailed check':
    payment_method = 1
elif payment_method == 'Bank transfer (automatic)':
    payment_method = 2
else:
    payment_method = 3

# Final input DataFrame (exact same order!)
input_data = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [senior],
    'Partner': [partner],
    'Dependents': [dependents],
    'tenure': [tenure],
    'PhoneService': [phone_service],
    'MultipleLines': [multiple_lines],
    'InternetService': [internet_service],
    'OnlineSecurity': [online_security],
    'OnlineBackup': [online_backup],
    'DeviceProtection': [device_protection],
    'TechSupport': [tech_support],
    'StreamingTV': [streaming_tv],
    'StreamingMovies': [streaming_movies],
    'Contract': [contract],
    'PaperlessBilling': [paperless_billing],
    'PaymentMethod': [payment_method],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges]
}) 

# Predict
if st.button('Predict'):
    result = model.predict(input_data)
    st.write('Prediction: ', 'Churn' if result[0] == 1 else 'No Churn')