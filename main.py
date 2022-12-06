import streamlit as st
import pandas as pd

st.write("PLAYSTORE APP DATA ANALYSIS")


@st.cache
def create_dataset():
    data = pd.read_csv('playstore_data.csv')
    data.columns = ['app_name', 'category', 'rating',
                    'rating_count', 'maximum_installs',
                    'free', 'price', 'currency',
                    'size', 'released', 'content_rating']
    return data


df = create_dataset()

st.write(df[((df['rating'] > 4) & (df['content_rating'] == 'Everyone'))])
