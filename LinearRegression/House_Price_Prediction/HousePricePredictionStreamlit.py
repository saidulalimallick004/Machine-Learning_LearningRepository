import streamlit as st
import pickle,joblib


st.title('The House Price Prediction Model: ')

a=st.number_input("Enter Area(sq.ft.):",value=1500)
b=st.number_input("Enter No of Bedrooms:",value=4)
c=st.number_input("Enter No of Bathrooms:",value=3)

with open('resources/Reverse_mapping.plk','rb') as f:
    reverse_mapping=dict(pickle.load(f))
City_list1= list(reverse_mapping.keys())

d=st.selectbox(
    "Select City:",City_list1
)
d=reverse_mapping.get(d,None)
UserInput=[a,b,c,d] 

if st.button("Predict", type='secondary'):
    HousePricePredictionModel=joblib.load('resources/HousePricePredictionModel.plk')
    Pred_price=HousePricePredictionModel.predict([UserInput])

    st.write("---------------------------------------------------------------------")
    st.write(f"""
      Area:{UserInput[0]}\n
      No of Bedroom:{UserInput[1]}\n
      No of Bathroom:{UserInput[2]}\n
      City:{UserInput[3]}\n
    
      Price(INR) = Rs.{Pred_price[0]:.2f}
      -------------------------------------
""")
    

#RUN IN Terminal:
#      streamlit must needed 
##    "streamlit run HousePricePredictionStreamlit.py"