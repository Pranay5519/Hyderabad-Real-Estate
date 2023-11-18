from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor,GradientBoostingRegressor,AdaBoostRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
from sklearn.metrics import mean_absolute_error
import warnings
import pickle
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd



with open(r"C:\Users\HP\Desktop\datasets\99acres\pipeline.pkl",'rb') as file:
    model = pickle.load(file)


data = [['flat', 'kokapet', 3.0, 3.0, '1', 'New Property', 1945.0, 0.0, 0.0,
       0.0, 'High', 'unfurnished', 'Mid Floor']]
columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'study room', 'servant room',
       'pooja room', 'luxury_score', 'furnish_score', 'floor_category']

# Convert to DataFrame
one_df = pd.DataFrame(data, columns=columns)
print(np.expm1(model.predict(one_df))[0])