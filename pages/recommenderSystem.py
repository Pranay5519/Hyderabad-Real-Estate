import streamlit as st
import ast
import numpy as np
import pandas as pd
import re
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder , MinMaxScaler,RobustScaler
df=pd.read_csv(r"C:\Users\HP\Desktop\datasets\flats campusX\hyderbad_sectors_cleaned_FS.csv")
del df['floorNum']
df['price'] = df['price'] * 10000000

print(df.isna().sum())
print(df['furnish_score'].isna().sum())

def categorize_furnish(score):
    if 0 <= score < 37:
        return "unfurnished"
    elif 37 <= score < 74:
        return "semifurnished"
    elif 74 <= score <= 111:
        return "furnished"
    else:
        return None


df['furnish_score'] = df['furnish_score'].apply(categorize_furnish)


def categorize_luxury(score):
    if 0 <= score < 85:
        return "Low"
    elif 85 <= score < 170:
        return "Medium"
    elif 170 <= score <= 300:
        return "High"
    else:
        return None


df['luxury_score'] = df['luxury_score'].apply(categorize_luxury)

df1 = df.copy()
print(df1.head())
property_type_or = OrdinalEncoder()
sector_or = OrdinalEncoder()
agePossession_or = OrdinalEncoder()
facing_or = OrdinalEncoder()
floor_category_or = OrdinalEncoder()
furnish_score_or = OrdinalEncoder()
luxury_score_or = OrdinalEncoder()
balcony_or = OrdinalEncoder()


df['property_type'] = property_type_or.fit_transform(df[['property_type']])
df['sector'] = sector_or.fit_transform(df[['sector']])
df['balcony'] = balcony_or.fit_transform(df[['balcony']])
df['facing'] = facing_or.fit_transform(df[['facing']])
df['floor_category']  =floor_category_or.fit_transform(df[['floor_category']])
df['luxury_score'] = luxury_score_or.fit_transform(df[['luxury_score']])
df['furnish_score'] = furnish_score_or.fit_transform(df[['furnish_score']])
df['agePossession']  = agePossession_or.fit_transform(df[['agePossession']])



st.title("Recommender Systems")

property_type = st.selectbox('Property Type',['flat','house'])

# sector
sector = st.selectbox('Sector',sorted(df1['sector'].unique().tolist()))

bedrooms = float(st.selectbox('Number of Bedroom',sorted(df1['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('Number of Bathrooms',sorted(df1['bathroom'].unique().tolist())))

balcony =st.selectbox('Balconies',sorted(df1['balcony'].unique().tolist()))
property_age = st.selectbox('Property Age',sorted(df1['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area'))

servant_room = float(st.selectbox('Servant Room',[0.0, 1.0]))
study_room = float(st.selectbox('Study Room',[0.0, 1.0]))
pooja_room = float(st.selectbox('Pooja Room',[0.0, 1.0]))

furnish_scores = df1['furnish_score'].unique().tolist()
furnish_scores = [score for score in furnish_scores if score is not None]  # Filter out None values
furnishing_type = st.selectbox('Furnishing Type', sorted(furnish_scores))

luxury_category = st.selectbox('Luxury Category',sorted(df1['luxury_score'].unique().tolist()))
floor_category = st.selectbox('Floor Category',sorted(df1['floor_category'].unique().tolist()))
facing = st.selectbox("facing" , sorted(df1['facing'].unique().tolist()))
price = float(st.number_input('Price in lacs') )

print(sector , bedrooms , bathroom , balcony , built_up_area , property_age , pooja_room , furnishing_type , luxury_category , floor_category)



if st.button('Recommend'):

    # form a dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony,facing, property_age
                , built_up_area,study_room, servant_room, pooja_room,
             luxury_category,furnishing_type , floor_category,price]]

    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'facing', 'agePossession', 'built_up_area', 'study room', 'servant room',
               'pooja room', 'luxury_score', 'furnish_score', 'floor_category',
               'price']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)
    one_df['property_type'] = property_type_or.transform(one_df[['property_type']])
    one_df['sector'] = sector_or.transform(one_df[['sector']])
    one_df['balcony'] = balcony_or.transform(one_df[['balcony']])
    one_df['facing'] = facing_or.transform(one_df[['facing']])
    one_df['floor_category'] = floor_category_or.transform(one_df[['floor_category']])
    one_df['luxury_score'] = luxury_score_or.transform(one_df[['luxury_score']])
    one_df['furnish_score'] = furnish_score_or.transform(one_df[['furnish_score']])
    one_df['agePossession'] = agePossession_or.transform(one_df[['agePossession']])
    sector = sector_or.transform([[sector]])[0][0]
    cosine_sim = cosine_similarity(df[df['sector'] == sector], one_df)
    similar_rows_indices = cosine_sim[:, 0].argsort()[:-6:-1]

    st.dataframe(df1[df1['sector']=='tellapur'].iloc[similar_rows_indices])
