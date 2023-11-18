import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import ast
#-----------------------------------------
def feature_text_func(sector_name):
    main  = []
    for item in word_df[word_df['sector']==sector_name]['features'].dropna().apply(ast.literal_eval):
        main.extend(item)
    return " ".join(main)
#----------------------------------------------

word_df = pd.read_csv(r"C:\Users\HP\Desktop\datasets\flats campusX\hyderabad_properties_outliers_treated.csv")
# AVG PRICE PER SQFT PLOT
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title="Plotting Demo")

st.title('Analytics')
st.subheader("Average Price per Sqft")
new_df = pd.read_csv(r'C:\Users\HP\Desktop\datasets\flats campusX\data_for_viz.csv')
group_df = new_df.groupby('sector').mean()[['price','pricepersqft','built_up_area','latitude','longitude']]
group_df.dropna(inplace= True)

fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="pricepersqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1400,height=800,hover_name=group_df.index)

st.plotly_chart(fig , use_container_width=True)

# Nearest Locations PLot
st.header("Nearest Locations")

placeslatlong = pd.read_csv(r'C:\Users\HP\Desktop\datasets\flats campusX\hyderbad_places_latlong.csv')

group_df1 = group_df.reset_index(drop=False)


sectorname = st.selectbox('Sector',sorted(group_df1['sector'].unique().tolist()))
sec = group_df1[group_df1['sector']==sectorname]
st.dataframe(sec)
fig1 = px.scatter_mapbox(placeslatlong, lat="Latitude", lon="Longitude", color='title', hover_name='Name',
                         color_continuous_scale=px.colors.cyclical.HSV, zoom=10,
                         mapbox_style="open-street-map", width=1800, height=800)
fig1.update_traces(marker=dict( size=10))

fig2 = px.scatter_mapbox(sec, lat="latitude", lon="longitude",
                         color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                         mapbox_style="open-street-map", width=1800, height=800
                         , color_discrete_sequence=["red"] , hover_name='sector')
fig2.update_traces(marker=dict( size=10))

fig1.add_trace(fig2.data[0])
st.plotly_chart(fig1 , use_container_width=True)

# Age Possession

st.header('Age Possession of Flats')
st.write(" Flats are be   Available in the marked sector / locality")
agepossession = st.selectbox("Age Possession" , new_df['agePossession'].unique())
fig4 = px.scatter_mapbox(new_df[new_df['agePossession'] == agepossession], lat="latitude", lon="longitude", hover_name='sector',
                         color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                         mapbox_style="open-street-map", width=1400, height=800)
fig4.update_traces(marker=dict(size=12))
st.plotly_chart(fig4 , use_container_width=True)

# Features PLOT
st.header('Top Features Per Sector')

sector_name = st.selectbox('Sector',word_df['sector'].unique().tolist())

st.subheader("Top Features")

plt.rcParams["font.family"] = "Arial"

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text_func(sector_name))

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)
st.pyplot()

#Price Vs Built UP area
property_type = st.selectbox("Select Property Type" , ['flat' , 'house'])

fig2 = px.scatter(word_df[word_df['property_type']==property_type], x="built_up_area", y="price", color="bedRoom", title = 'Area Vs Price')
st.plotly_chart(fig2 , use_container_width=True)

# Pie Chart
st.header('BHK Pie Chart')

sector_options = word_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(word_df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(word_df[word_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)


#Side by Side BHK price comparison
st.header('Side by Side BHK price comparison')

fig3 = px.box(word_df[word_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)


st.header('Side by Side Distplot for property type')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(word_df[word_df['property_type'] == 'house']['price'],label='house')
sns.distplot(word_df[word_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)