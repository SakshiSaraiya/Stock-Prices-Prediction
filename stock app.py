import streamlit as st
import joblib
import numpy as np

st.title("📈 Stock Price Predictor")

model = joblib.load('stock_model.pkl')

st.markdown("Enter stock indicators below:")

open_price = st.number_input("Open Price")
high_price = st.number_input("High Price")
low_price = st.number_input("Low Price")
volume = st.number_input("Volume", value=1000000, step=10000)

if st.button("Predict Next Day's Close"):
    features = np.array([[open_price, high_price, low_price, volume]])
    prediction = model.predict(features)[0]
    st.success(f"📊 Predicted Next Day Close: ₹{prediction:.2f}")
