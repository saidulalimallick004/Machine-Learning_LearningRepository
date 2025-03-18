import streamlit as st
import pickle,joblib
from sklearn.linear_model import LinearRegression

import os
os.makedirs("resources", exist_ok=True)

MODEL_PATH="resources/HousePricePredictionModel.plk"
MAPPING_CITY_PATH="resources/Reverse_mapping.plk"
MODEL_DETAIL_PATH="resources/model_currectness_value.plk"


st.title('The House Price Prediction Model: ')

with open(MODEL_DETAIL_PATH,'rb') as x:
    detail=dict(pickle.load(x))

with st.expander("Click to see Model details"):
    st.write("Model Detail:")
    st.write("R2 Score:",detail['model_r2_score'])
    st.write("Mean Absolute Error Score:",detail['model_mae'])
    st.write("Mean Squere Error Score:",detail['model_mse'])


a=st.number_input("Enter Area(sq.ft.):",value=1500)
b=st.number_input("Enter No of Bedrooms:",value=4)
c=st.number_input("Enter No of Bathrooms:",value=3)



with open(MAPPING_CITY_PATH,'rb') as f:
    reverse_mapping=dict(pickle.load(f))
City_list1= list(reverse_mapping.keys())

d=st.selectbox(
    "Select City:",City_list1
)

city=d
d=reverse_mapping.get(d,None)
UserInput=[a,b,c,d] 



if st.button("Predict", type='secondary'):

    HousePricePredictionModel=joblib.load(MODEL_PATH)
    Pred_price=HousePricePredictionModel.predict([UserInput])

    


    st.write("---------------------------------------------------------------------")
    st.write(f"""
      Area: {UserInput[0]}\n
      No of Bedroom: {UserInput[1]}\n
      No of Bathroom: {UserInput[2]}\n
      City: {city}\n
    
      Price(INR) = Rs.{Pred_price[0]:.2f}
      -------------------------------------
""")
    

#RUN IN Terminal:
#      streamlit must needed 
##    "streamlit run HousePricePredictionStreamlit.py"