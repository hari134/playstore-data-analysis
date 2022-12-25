import streamlit as st
import pandas as pd
import numpy as np
import datetime
from visualization import visualizer ,utility_variables

st.title("PLAYSTORE APP DATA ANALYSIS")
st.markdown("This is an app for exploratory data analysis on the **Playstore apps dataset**.")
st.markdown("The dataset has over **_1_ _million_ _rows_** and is a cleaned version of the original Kaggle dataset.")
st.markdown("The cleaned dataset can be found here: https://drive.google.com/file/d/1jiL0Qy_ulouhOEK7amaGweuuh_CRwEF4/view?usp=sharing")

# creating the dataframe for analysis
@st.cache
def create_dataset():
    data = pd.read_csv("playstore_data.csv")
    data.columns = utility_variables['column_names']
    data['released'] = pd.to_datetime(data['released'])
    return data


# loading dataframe
df = create_dataset()

# showing categories to users for analysis
with st.sidebar:

    st.header("FILTERS")

    categories = st.multiselect(
        "1. SELECT CATEGORY OF APPS", utility_variables['all_categories'], ["All"])

    content_rating = st.multiselect("2. SELECT CONTENT RATING OF APPS", utility_variables['content_ratings'], ["Everyone"])

    rating = st.slider("3. SELECT RATINGS RANGE", 0.0, 5.0, (0.0, 5.0))

    num_of_rating = st.slider(
        "4. SELECT NUMBER OF RATINGS RANGE", 0, 56025424, (0, 56025424)
    )

    cost = st.radio("5. APP SHOULD BE(FREE OR PAID)?", ("ANY", "FREE", "PAID"))

    app_size = st.slider(
        "6. SELECT RANGE OF SIZE OF THE APP(in MB)", 1, 999, (1, 999))

    min_installs_col, max_installs_col = st.columns(2)
    with min_installs_col:
        min_installs = st.number_input("7. MINIMUM INSTALLS", 0, 1704495994, 0)

    with max_installs_col:
        max_installs = st.number_input(
            "MAXIMUM INSTALLS", 0, 1704495994, 1704495994)

    min_date_col, max_date_col = st.columns(2)
    with min_date_col:
        min_date = st.date_input(
            "8. ENTER MINIMUM RELEASE DATE ", datetime.date(2010, 1, 28))

    with max_date_col:
        max_date = st.date_input(
            "  ENTER MAXIMUM RELEASE DATE ", datetime.date(2021, 6, 15))
    # input interpretation

filter_input = {"categories": categories, "cost": cost, "content_rating": content_rating, "rating": rating,
                "num_of_rating": num_of_rating, "app_size": app_size, "installs": {"min_installs": min_installs, "max_installs": max_installs},
                "released":{"min_date":np.datetime64(min_date),"max_date":np.datetime64(max_date)}}

v = visualizer(df,**filter_input)
filtered_df = v.get_filtered_data()
v.display_table()
v.plot_bar_categories()
v.plot_bar_content_rating()




