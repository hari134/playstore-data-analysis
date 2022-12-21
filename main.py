import streamlit as st
import pandas as pd
import datetime
import visualization

st.title("PLAYSTORE APP DATA ANALYSIS")


# creating the dataframe for analysis
@st.cache
def create_dataset():
    data = pd.read_csv("playstore_data.csv")
    data.columns = visualization.utility_variables['column_names']
    data['released'] = pd.to_datetime(data['released'])
    return data


# loading dataframe
df = create_dataset()

# showing categories to users for analysis
with st.sidebar:

    st.header("FILTERS")

    categories = st.multiselect(
    "1. SELECT CATEGORY OF APPS",visualization.utility_variables['all_categories'],["All"],)

    content_rating = st.multiselect(
        "2. SELECT CONTENT RATING OF APPS",visualization.utility_variables['content_ratings'],["Everyone"])

    rating = st.slider("3. SELECT RATINGS RANGE", 0.0, 5.0, (0.0, 5.0))

    num_of_rating = st.slider(
        "4. SELECT NUMBER OF RATINGS RANGE", 0, 56025424, (0, 56025424)
    )

    cost = st.radio("5. APP SHOULD BE(FREE OR PAID)?", ("ANY", "FREE", "PAID"))

    app_size = st.slider(
        "6. SELECT RANGE OF SIZE OF THE APP(in MB)", 1, 999, (1, 999))

    min_installs_col, max_installs_col = st.columns(2)
    with min_installs_col:
        min_installs = st.number_input("7. MINIMUM INSTALLS",0,1704495994,0)

    with max_installs_col:
        max_installs = st.number_input("MAXIMUM INSTALLS",0,1704495994,1704495994)


    min_date_col, max_date_col = st.columns(2)
    with min_date_col:
        min_date = st.date_input("8. ENTER MINIMUM RELEASE DATE ",datetime.date(2010,1,28))

    with max_date_col:
        max_date = st.date_input("  ENTER MAXIMUM RELEASE DATE ",datetime.date(2021,6,15))
    # input interpretation

# cost of app
if cost == "FREE":
    query_cost = 1
elif cost == "PAID":
    query_cost = 0
else:
    query_cost = 2



if query_cost == 1:
    if "All" in categories:
        df_category = df[
            ~df["category"].isin([])
            & df["content_rating"].isin(content_rating)
            & ((df["rating"] > rating[0]) & (df["rating"] < rating[1]))
            & (
                (df["rating_count"] > num_of_rating[0])
                & (df["rating_count"] < num_of_rating[1])
                & df["free"]
                == 1
            )
            & ((df["size"] > app_size[0]) & (df["size"] < app_size[1]))
        ]
    else:
        df_category = df[
            df["category"].isin(categories)
            & df["content_rating"].isin(content_rating)
            & ((df["rating"] > rating[0]) & (df["rating"] < rating[1]))
            & (
                (df["rating_count"] > num_of_rating[0])
                & (df["rating_count"] < num_of_rating[1])
                & df["free"]
                == 1
            )
            & ((df["size"] > app_size[0]) & (df["size"] < app_size[1]))
        ]

elif query_cost == 0:
    if "All" in categories:
        df_final = df[
            ~df["category"].isin([])
            & df["content_rating"].isin(content_rating)
            & ((df["rating"] > rating[0]) & (df["rating"] < rating[1]))
            & (
                (df["rating_count"] > num_of_rating[0])
                & (df["rating_count"] < num_of_rating[1])
                & df["free"]
                == 0
            )
            & ((df["size"] > app_size[0]) & (df["size"] < app_size[1]))
        ]
    else:
        df_final = df[
            df["category"].isin(categories)
            & df["content_rating"].isin(content_rating)
            & (df["rating"] > rating[0])
            & (df["rating"] < rating[1])
            & (
                (df["rating_count"] > num_of_rating[0])
                & (df["rating_count"] < num_of_rating[1])
                & df["free"]
                == 0
            )
            & ((df["size"] > app_size[0]) & (df["size"] < app_size[1]))
        ]
else:
    if "All" in categories:
        df_final = df[
            ~df["category"].isin([])
            & df["content_rating"].isin(content_rating)
            & ((df["rating"] > rating[0]) & (df["rating"] < rating[1]))
            & (
                (df["rating_count"] > num_of_rating[0])
                & (df["rating_count"] < num_of_rating[1])
            )
            & (df["size"] > app_size[0]) & (df["size"] < app_size[1])
            & ((df['maximum_installs'] < max_installs) & (df['maximum_installs'] > min_installs))
            & ((df['released'] < '2021-06-15') & (df['released'] > '2010-01-28'))
        ]
    else:
        df_final = df[
            df["category"].isin(categories)
            & df["content_rating"].isin(content_rating)
            & ((df["rating"] > rating[0]) & (df["rating"] < rating[1]))
            & (
                (df["rating_count"] > num_of_rating[0])
                & (df["rating_count"] < num_of_rating[1])
            )
            & ((df["size"] > app_size[0]) & (df["size"] < app_size[1]))
        ]
# df_rating = df_category[(df_category['rating'] > rating[0]) & (df_category['rating'] < rating[1])]
# df_num_ratings = df_rating[
#     (df_rating['rating_count'] > num_of_rating[0]) & (df_rating['rating_count'] < num_of_rating[1])]
# df_final = df_num_ratings
# print(df_final)
st.success("FILTERED RESULT")
st.write(df_final)

visualization.plot_bar_categories(categories, df_final)
visualization.plot_bar_content_rating(content_rating, df_final)
