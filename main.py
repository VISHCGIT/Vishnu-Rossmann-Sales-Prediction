import streamlit as st
import pandas as pd
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import  LabelEncoder
import xgboost as xgb
#from xgboost import XGBRegressor
import numpy as np
import re
st.header("Rossmann Sales Prediction App")
st.text_input("Enter your Name: ", key="name")
data = pd.read_csv("https://raw.githubusercontent.com/gurokeretcha/WishWeightPredictionApplication/master/Fish.csv")
#load label encoder
#encoder = LabelEncoder()
#encoder.classes_ = np.load('classes.npy',allow_pickle=True)

# load model
best_xgboost_model = xgb.XGBRegressor()
#best_xgboost_model.load_model("best_model.json")

if st.checkbox('Show Training Dataframe'):
    data

date1 = st.date_input("enter date:")
st.Write(date1.year)


collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]

numbers = st.text_input("PLease enter numbers")
st.write(collect_numbers(numbers))

fixed_numbers = st.multiselect("Please select numbers", [1, 2, 3, 4, 5])
st.write(fixed_numbers)

features = ["DayOfWeek","DayOfWeekName","MonthName","Customers","Promo","StateHoliday","SchoolHoliday","StoreType","Assortment","CompetitionDistance","CompetitionOpenSinceMonth","Promo2SinceWeek","PromoInterval"]
value = []
for i in range(len(features)):
    number = st.number_input("Enter the values for " +features[i])
    value.append(number)


"""if st.button('Make Prediction'):
    input_species = encoder.transform(np.expand_dims(inp_species, -1))
    inputs = np.expand_dims(
        [int(input_species), input_Length1, input_Length2, input_Length3, input_Height, input_Width], 0)
    prediction = best_xgboost_model.predict(inputs)
    print("final pred", np.squeeze(prediction, -1))
    st.write(f"Your fish weight is: {np.squeeze(prediction, -1):.2f}g")

    st.write(f"Thank you {st.session_state.name}! I hope you liked it.")
    st.write(f"If you want to see more advanced applications you can follow me on [medium](https://medium.com/@gkeretchashvili)")"""
