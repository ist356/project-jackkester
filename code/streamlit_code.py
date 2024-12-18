import pandas as pd 
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import folium
import geopandas as gpd
import streamlit_folium as sf
from streamlit_folium import st_folium
import plotly.express as px

list_of_categories = {"Mens Flyweight": ['cache/men_fly_df.csv'], "Mens Bantamweight": ['cache/men_bantham_df.csv'], "Mens Featherweight": ['cache/men_feather_df.csv'], "Mens Lightweight": ['cache/men_light_df.csv'], "Mens Welterweight": ['cache/men_welter_df.csv'], "Mens Middleweight": ['cache/men_middle_df.csv'], "Mens Light Heavyweight": ['cache/men_light_heavy_df.csv'], "Mens Heavyweight": ['cache/men_heavy_df'], "Womens Strawweight": ['cache/women_straw_df.csv'], "Womens Flyweight": ['cache/women_fly_df.csv'], "Womens Bantamweight": ['cache/women_bantam_df.csv'], 'All Weight Classes': ['cache/merged_df.csv'], 'All Mens Weight Classes': ['cache/men_merged_df.csv'], 'All Womens Weight': ['cache/women_merged_df.csv']}  

st.title('The Characteristics that Form the Best UFC Fighters')
st.caption('This project analyzes the characteristics of the top UFC fighters in each weight class')
weight_choice = st.selectbox('Select a Weight Class', list_of_categories.keys())

if weight_choice:
    file = pd.read_csv(list_of_categories[weight_choice][0])
    df = pd.DataFrame(file)
    st.write(df)
    col1, col2 = st.columns(2)

    with col1:
        numerical_items = ['Age', 'Height (cm)', 'Reach (cm)', 'Leg Reach (cm)']
        choice = st.selectbox('Select a Numerical Characteristic to Analyze', numerical_items)
        fig1, ax1 = plt.subplots()
        sns.histplot(df[choice], bins = 5, kde=True, ax = ax1)
        plt.title(f'{choice} Distribution of Fighters')
        st.pyplot(fig1)
    
    with col2:
        str_items = ['Team', 'Fighting Style', 'Training Location']
        str_choice = st.selectbox('Select a Characteristic to Analyze', str_items)
        data_to_plot = df[str_choice].value_counts().reset_index()
        data_to_plot.columns = [str_choice, 'Count']  
        fig2, ax2 = plt.subplots(figsize=(10, 8))
        sns.barplot(data=data_to_plot, x=str_choice, y='Count', palette='magma', ax=ax2)
        ax2.set_title(f'{str_choice} Distribution of Fighters')
        ax2.set_xlabel(str_choice)
        ax2.set_ylabel('Number of Fighters')
        plt.xticks(rotation=45, ha='right')  
        st.pyplot(fig2)

    country_counts = df['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Count']

    map = px.choropleth(country_counts, locations='Country', locationmode='country names', color='Count', hover_name='Country', color_continuous_scale='magma', title='Number of Fighters per Country')
    st.plotly_chart(map)