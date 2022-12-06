import streamlit as st
import pandas as pd

st.write("PLAYSTORE APP DATA ANALYSIS")


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
    '1. SELECT CATEGORY OF APP',
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
rating = st.slider("2. SELECT RATINGS RANGE", 0.0, 5.0, (0.0, 5.0))

num_of_rating = st.slider("2. SELECT NUMBER OF RATINGS RANGE", 0, 56025424, (0, 56025424))

cost = st.radio(
    "3. APP SHOULD BE(FREE OR PAID)?",
    ('ANY', 'FREE', 'PAID'))

limit = st.number_input("How many rows do you want to display")

if cost == 'ANY':
    query_cost = "AND FREE = 1 OR FREE = 0"
elif cost == 'FREE':
    query_cost = "AND FREE = 1"
else:
    query_cost = "AND FREE = 0"

opts = "'" + str(options[0]) + "'"
for i in range(1, len(options)):
    opts = opts + "," + "'" + options[i] + "'"

rating_query = " AND RATING >= " + str(rating[0]) + " AND RATING <= " + str(rating[1])

limit_query = "LIMIT " + str(limit)

st.write(df[((df['rating'] > 4) & (df['content_rating'] == 'Everyone'))])
