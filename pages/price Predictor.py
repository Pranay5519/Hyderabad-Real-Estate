import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn
import joblib
import category_encoders as ce

print(pd.__version__)
print(sklearn.__version__)
st.set_page_config(page_title="Viz Demo")

df= pd.read_csv("df_final.csv")
with open("pipeline.pkl",'rb') as file:
    model = pickle.load(file)



st.header('Enter your inputs')

# property_type
property_type = st.selectbox('Property Type',['flat','house'])

# sector
sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique().tolist())))

balcony =st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))
property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area'))

servant_room = float(st.selectbox('Servant Room',[0.0, 1.0]))
study_room = float(st.selectbox('Study Room',[0.0, 1.0]))
pooja_room = float(st.selectbox('Pooja Room',[0.0, 1.0]))

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnish_score'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_score'].unique().tolist()))
floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))


if st.button('Predict'):

    # form a dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area,study_room, servant_room, pooja_room,
             luxury_category,furnishing_type , floor_category]]

    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'study room', 'servant room',
       'pooja room', 'luxury_score', 'furnish_score', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)


    # predict
    price = np.expm1(model.predict(one_df))[0]
    print(price)
    low = price - 0.21
    high = price + 0.21


    # display
    st.text("The price of the flat is between {} Cr and {} Cr".format(round(low, 2), round(high, 2)))
