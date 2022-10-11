import streamlit as st
import numpy as np
import predictor
from PIL import Image
import warnings
from predictor import predict_class
warnings.filterwarnings('ignore')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.image('header.png')

placeholder = st.empty()
with placeholder.form("Input"):
  st.markdown("Titanic Survival Prediction")
  x00 = st.number_input(
    label='Enter Ticket class [1 = 1st, 2 = 2nd, 3 = 3rd] :',
    step=1.,
    format='%.2f'
    )
  
  x01 = st.number_input(
    label="Enter Sex ['male':0 , 'female':1 ] :",
    step=1.,format='%.4f'
    )

  x02 = st.number_input(label='Enter Age :',
    step=1.,
    format='%.2f'
    )

  x03 = st.number_input(
    label='Enter number of siblings / spouses aboard the Titanic :',
    step=1.,
    format='%.2f'
    )

  x04 = st.number_input(
    label='Enter number of parents / children aboard the Titanic :',
    step=1.,
    format='%.2f'
    )

  x05 = st.number_input(
    label='Enter Passenger fare:',
    step=1.,
    format='%.2f'
    )

  x06 = st.number_input(
    label='Enter Port of Embarkation :',
    step=1.,
    format='%.2f'
    )
  values_list = [x00,x01,x02,x03,x04,x05,x06]
  submit =  st.form_submit_button("submit")

if submit and None not in values_list:
  input_data = values_list
  st.markdown(f"### {predict_class(input_data)}")
else:
  st.markdown("### TEST ENTRIES ARE EMPTY OR CONTAIN INCORRECT VALUES")

st.image('footer.png')