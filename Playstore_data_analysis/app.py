import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

limit =1000

st.title("Playstore app data analysis")

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
rating = st.slider("2. SELECT RATINGS RANGE",0.0,5.0,(0.0,5.0))

num_of_rating = st.slider("2. SELECT NUMBER OF RATINGS RANGE",0,56025424,(0,56025424))

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


opts = "'"+str(options[0])+"'"
for i in range(1,len(options)):
    opts = opts + "," + "'"+options[i]+"'"

rating_query = " AND RATING >= "+str(rating[0])+" AND RATING <= "+str(rating[1])

limit_query = "LIMIT "+str(limit)

data = pd.DataFrame(columns=("APP_NAME","CATEGORY","RATING",
                            "RATING_COUNT","MAXIMUM_INSTALLS","FREE",
                            "PRICE","CURRENCY","SIZE","RELEASED","CONTENT_RATING"))  # type: ignore


engine = create_engine(
    "postgresql+psycopg2://postgres:Postgres%40123@localhost/postgres",
    isolation_level="SERIALIZABLE",
)
conn = engine.connect()
query = "SELECT * FROM PLAYSTORE_APPS WHERE CATEGORY IN ("+opts+")"+ rating_query +query_cost+ limit_query+";"
df = pd.read_sql_query(query, con=conn)
st.write(df)


# for row in rows:
#     i=1
#     temp_df = pd.DataFrame({"APP_NAME":row[0],"CATEGORY":row[1],"RATING":row[2],"RATING_COUNT":row[3],
#                             "MAXIMUM_INSTALLS":row[4],"FREE":row[5],"PRICE":row[6],"CURRENCY":row[7],
#                             "SIZE":row[8],"RELEASED":row[9],"CONTENT_RATING":row[10]},index = [i])
#     st.session_state.df = st.session_state.df.append(temp_df,ignore_index = True)
#     i= i+1
#     st.dataframe(st.session_state.df)

