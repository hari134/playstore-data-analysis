import streamlit as st
import pandas as pd

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
    ["All",
     "Board",
     "Finance",
     "Role Playing",
     "Health & Fitness",
     "Productivity",
     "Comics",
     "Adventure",
     "Puzzle",
     "Strategy",
     "Shopping",
     "Casual",
     "Simulation",
     "Education",
     "Beauty",
     "Books & Reference",
     "Arcade",
     "Auto & Vehicles",
     "Sports",
     "Food & Drink",
     "Dating",
     "Weather",
     "Music",
     "Entertainment",
     "Communication",
     "Events",
     "Medical",
     "Casino",
     "Travel & Local",
     "Maps & Navigation",
     "Racing",
     "Action",
     "Card",
     "News & Magazines",
     "Art & Design",
     "Parenting",
     "Lifestyle",
     "Trivia",
     "Word",
     "House & Home",
     "Tools",
     "Business",
     "Libraries & Demo",
     "Social",
     "Personalization",
     "Video Players & Editors",
     "Photography"],
    ["Board"]
)
content_rating = st.multiselect(
    "2. SELECT CONTENT RATING OF APPS",
    ["Unrated",
     "Everyone 10+",
     "Teen",
     "Everyone",
     "Adults only 18+",
     "Mature 17+"],
    ["Everyone"]
)
rating = st.slider('3. SELECT RATINGS RANGE', 0.0, 5.0, (0.0, 5.0))

num_of_rating = st.slider("4. SELECT NUMBER OF RATINGS RANGE", 0, 56025424, (0, 56025424))

cost = st.radio(
    "5. APP SHOULD BE(FREE OR PAID)?",
    ('ANY', 'FREE', 'PAID'))

# input interpretation

# cost of app
if cost == 'ANY':
    query_cost = "AND FREE = 1 OR FREE = 0"
elif cost == 'FREE':
    query_cost = "AND FREE = 1"
else:
    query_cost = "AND FREE = 0"

# categories of app
opts = []
for i in range(0, len(options)):
    opts.append(options[i])

# content rating of apps
content_rating_opts = []
for i in range(0, len(content_rating)):
    content_rating_opts.append(content_rating[i])
rating_query = " AND RATING >= " + str(rating[0]) + " AND RATING <= " + str(rating[1])

df_category = df[df['category'].isin(opts) & df['content_rating'].isin(content_rating_opts) & (
        (df['rating'] > rating[0]) & (df['rating'] < rating[1])) & (
                         (df['rating_count'] > num_of_rating[0]) & (df['rating_count'] < num_of_rating[1]))]
# df_rating = df_category[(df_category['rating'] > rating[0]) & (df_category['rating'] < rating[1])]
# df_num_ratings = df_rating[
#     (df_rating['rating_count'] > num_of_rating[0]) & (df_rating['rating_count'] < num_of_rating[1])]
# df_final = df_num_ratings
# print(df_final)
st.write(df_category)
