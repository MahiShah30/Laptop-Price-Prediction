import streamlit as st
import pickle
import pandas as pd
import numpy as np

try:
    with open('laptop_price_predictor_final.pkl', 'rb') as f:
        pipeline = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Make sure 'laptop_price_predictor_final.pkl' is in the same directory.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()

CURRENCY_RATES = {
    "India (INR)": {"rate": 90.0, "symbol": "₹"},
    "America (USD)": {"rate": 1.1, "symbol": "$"},
    "France (EUR)": {"rate": 1.0, "symbol": "€"}
}

st.title("💻 Laptop Price Prediction")
st.header("Fill in the details below to predict the price of a laptop")

country = st.selectbox("Select your country for price conversion:", list(CURRENCY_RATES.keys()))

col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox('Brand', ['Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'MSI', 'Apple', 'Other'])
    ram = st.selectbox('RAM (in GB)', [4, 8, 12, 16, 32, 64])
    storage = st.number_input('Storage (in GB)', min_value=128, max_value=4000, value=512, step=128)
    storage_type = st.selectbox('Storage Type', ['SSD', 'HDD', 'eMMC'])
    status = st.selectbox('Status', ['New', 'Refurbished'])

with col2:
    screen = st.number_input('Screen Size (in inches)', min_value=11.0, max_value=18.0, value=15.6, step=0.1)
    touch = st.selectbox('Touchscreen', ['No', 'Yes'])
    cpu_brand = st.selectbox('CPU Brand', [
        'Intel Core i7', 'Intel Core i5', 'Intel Core i3', 'Other Intel CPU',
        'AMD Ryzen 7', 'AMD Ryzen 5', 'AMD Ryzen 9', 'AMD Ryzen 3', 'Other AMD CPU',
        'Apple CPU', 'Other'
    ])
    gpu_brand = st.selectbox('GPU Brand', [
        'NVIDIA', 'Intel', 'AMD', 'None', 'ARM', 'Qualcomm'
    ])

if st.button('Predict Price'):
    try:
        selected_currency_info = CURRENCY_RATES[country]
        exchange_rate = selected_currency_info["rate"]
        currency_symbol = selected_currency_info["symbol"]

        touch_binary = 1 if touch == 'Yes' else 0

        input_data = pd.DataFrame([[
            status, brand, ram, storage, storage_type, screen, touch_binary, cpu_brand, gpu_brand
        ]], columns=[
            'Status', 'Brand', 'RAM', 'Storage', 'Storage type', 'Screen', 'Touch', 'Cpu_Brand', 'Gpu_Brand'
        ])

        prediction_log = pipeline.predict(input_data)
        predicted_price_eur = np.exp(prediction_log[0])

        converted_price = predicted_price_eur * exchange_rate

        st.success(f"The predicted price of the laptop is: {currency_symbol}{converted_price:,.2f}")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")