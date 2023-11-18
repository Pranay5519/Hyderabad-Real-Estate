import streamlit as st

st.set_page_config(
    page_title="Hyderabad Real Estate Analytics App",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")
import streamlit as st

# Title
st.title("Real Estate Data Analysis with 99acres Data")

# Introduction
st.markdown("In this project, we collected data from the 99acres website, consisting of information on flats and independent houses. The data was initially divided into two files, which were cleaned individually to remove any inconsistencies or inaccuracies. Subsequently, the two datasets were merged, and feature engineering techniques were applied to enhance the quality and relevance of the data.")

st.markdown("An exploratory data analysis (EDA) was performed, encompassing both univariate and bivariate analyses to gain insights into the data's distribution and relationships. Outliers were identified and dealt with appropriately, while missing values were addressed through imputation or removal, as needed.")

st.markdown("In the final stage, model selection was carried out, using a pipeline considering various machine learning algorithms and evaluating their performance to find the most suitable model for the given dataset. This comprehensive analysis is crucial for making informed decisions and extracting valuable insights from the real estate data collected from 99acres.")

# Icons
st.markdown(":mortar_board: **Streamlit Web Application**: Developed a comprehensive Streamlit web application that combines multiple functionalities in one platform:")
st.markdown(":heavy_check_mark: **Price Predictor**: Integrated a machine learning model into the application, allowing users to input property details and receive instant price predictions.")
st.markdown(":bar_chart: **Analytics Section**: Included a dedicated section within the application where users can explore various visualizations like scatter plots, maps, and other charts, providing insights into the real estate market.")
st.markdown(":bulb: **Recommendation System**: Added a recommendation feature that offers personalized flat recommendations based on user preferences, enhancing the user's property search experience.")

st.markdown("This all-in-one Streamlit application provides users with a one-stop solution for real estate data analysis, price estimation, data visualization, and property recommendations, making it a powerful tool for informed decision-making in the housing market.")

st.sidebar.success("Select a demo above.")