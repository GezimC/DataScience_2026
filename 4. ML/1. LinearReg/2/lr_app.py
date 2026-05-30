import joblib as jl
import streamlit as sl


model = jl.load('lr_model.pkl')


x1 = sl.number_input('Avg. Session Length')
x2 = sl.number_input('Time on App')
x3 = sl.number_input('Time on Website')
x4 = sl.number_input('Length of Membership')


if sl.button('Predict'):
    predicted = model.predict([[x1,x2,x3,x4]])
    sl.success(predicted)