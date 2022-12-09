import streamlit as st
import pandas as pd

import visualization

st.title("PLAYSTORE APP DATA ANALYSIS")


# creating the dataframe for analysis
@st.cache
def create_dataset():
    data = pd.read_csv('playstore_data.csv')
    data.columns = ['app_name', 'category', 'rating',
                    'rating_count', 'maximum_installs',
                    'free', 'price', 'currency',
                    'size', 'released', 'content_rating']
    return data


# loading dataframe
df = create_dataset()

# showing options to users for analysis

options = st.multiselect(
    "1. SELECT CATEGORY OF APPS",
    ["All", "Board", "Finance", "Role Playing", "Health & Fitness",
     "Productivity", "Comics", "Adventure", "Puzzle", "Strategy",
     "Shopping", "Casual", "Simulation", "Education", "Beauty",
     "Books & Reference", "Arcade", "Auto & Vehicles", "Sports",
     "Food & Drink", "Dating", "Weather", "Music", "Entertainment",
     "Communication", "Events", "Medical", "Casino", "Travel & Local",
     "Maps & Navigation", "Racing", "Action", "Card", "News & Magazines",
     "Art & Design", "Parenting", "Lifestyle", "Trivia", "Word",
     "House & Home", "Tools", "Business", "Libraries & Demo", "Social",
     "Personalization", "Video Players & Editors", "Photography"],
    ["All"]
)
content_rating = st.multiselect(
    "2. SELECT CONTENT RATING OF APPS",
    ["Unrated", "Everyone 10+", "Teen",
     "Everyone", "Adults only 18+", "Mature 17+"],
    ["Everyone"]
)
rating = st.slider('3. SELECT RATINGS RANGE', 0.0, 5.0, (0.0, 5.0))

num_of_rating = st.slider("4. SELECT NUMBER OF RATINGS RANGE", 0, 56025424, (0, 56025424))

cost = st.radio(
    "5. APP SHOULD BE(FREE OR PAID)?",
    ('ANY', 'FREE', 'PAID'))

app_size = st.slider("6. SELECT RANGE OF SIZE OF THE APP(in MB)", 1, 999, (1, 999))


# input interpretation

# cost of app
if cost == 'FREE':
    query_cost = 1
elif cost == 'PAID':
    query_cost = 0
else:
    query_cost = 2

# categories of app
opts = []
for i in range(0, len(options)):
    opts.append(options[i])

# content rating of apps
content_rating_opts = []
for i in range(0, len(content_rating)):
    content_rating_opts.append(content_rating[i])


if query_cost == 1:
    if 'All' in opts:
        df_category = df[~df['category'].isin([]) & df['content_rating'].isin(content_rating_opts) & (
            (df['rating'] > rating[0]) & (df['rating'] < rating[1])) &
            ((df['rating_count'] > num_of_rating[0]) & (df['rating_count'] < num_of_rating[1]) & df['free'] == 1) &
            ((df['size'] > app_size[0]) & (df['size'] < app_size[1]))]
    else:
        df_category = df[df['category'].isin(opts) & df['content_rating'].isin(content_rating_opts) & (
            (df['rating'] > rating[0]) & (df['rating'] < rating[1])) &
            ((df['rating_count'] > num_of_rating[0]) & (df['rating_count'] < num_of_rating[1]) & df['free'] == 1) &
            ((df['size'] > app_size[0]) & (df['size'] < app_size[1]))]

elif query_cost == 0:
    if 'All' in opts:
        df_final = df[~df['category'].isin([]) & df['content_rating'].isin(content_rating_opts) & (
            (df['rating'] > rating[0]) & (df['rating'] < rating[1])) &
            ((df['rating_count'] > num_of_rating[0]) & (df['rating_count'] < num_of_rating[1]) & df['free'] == 0) &
            ((df['size'] > app_size[0]) & (df['size'] < app_size[1]))]
    else:
        df_final = df[df['category'].isin(opts) & df['content_rating'].isin(content_rating_opts) & (
            df['rating'] > rating[0]) & (df['rating'] < rating[1]) &((df['rating_count'] > num_of_rating[0]) &
            (df['rating_count'] < num_of_rating[1]) & df['free'] == 0) &
            ((df['size'] > app_size[0]) & (df['size'] < app_size[1]))]
else:
    if 'All' in opts:
        df_final = df[~df['category'].isin([]) & df['content_rating'].isin(content_rating_opts) & (
            (df['rating'] > rating[0]) & (df['rating'] < rating[1])) &
            ((df['rating_count'] > num_of_rating[0]) & (df['rating_count'] < num_of_rating[1])) &
            ((df['size'] > app_size[0]) & (df['size'] < app_size[1]))]
    else:
        df_final = df[df['category'].isin(opts) & df['content_rating'].isin(content_rating_opts) & (
            (df['rating'] > rating[0]) & (df['rating'] < rating[1])) &
            ((df['rating_count'] > num_of_rating[0]) & (df['rating_count'] < num_of_rating[1])) & (
            (df['size'] > app_size[0]) & (df['size'] < app_size[1]))]
# df_rating = df_category[(df_category['rating'] > rating[0]) & (df_category['rating'] < rating[1])]
# df_num_ratings = df_rating[
#     (df_rating['rating_count'] > num_of_rating[0]) & (df_rating['rating_count'] < num_of_rating[1])]
# df_final = df_num_ratings
# print(df_final)
st.success("FILTERED RESULT")
st.write(df_final)

visualization.plot_bar_categories(opts,df_final)
visualization.plot_bar_content_rating(content_rating_opts,df_final)