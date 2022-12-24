import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


# utility variables
column_names: list[str] = [
    "app_name",
    "category",
    "rating",
    "rating_count",
    "maximum_installs",
    "free",
    "price",
    "currency",
    "size",
    "released",
    "content_rating",
]

all_categories: list[str] = [
    "All",
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
    "Photography",
]

content_ratings: list[str] = ["Unrated", "Everyone 10+",
                              "Teen", "Everyone", "Adults only 18+", "Mature 17+"]


utility_variables: dict[str, list[str]] = {
    "all_categories": all_categories,
    "content_ratings": content_ratings,
    "column_names": column_names,
}


class visualizer:
    def __init__(self, dataframe, **kwargs):
        self.parameters = kwargs
        self.df = dataframe

    def parse_input(parameters) -> dict[str, any]:
        categories: list[str] = parameters["categories"]
        cost: str = parameters["cost"]

        query_cost = [1] if cost == "FREE" else [
            0] if cost == "PAID" else [1, 0]
        categories = (
            categories
            if "All" not in categories
            else utility_variables["all_categories"]
        )
        parsed_input = {
            "categories": categories,
            "cost": query_cost,
            "content_rating": parameters["content_rating"],
            "rating": parameters["rating"],
            "num_of_rating": parameters["num_of_rating"],
            "app_size": parameters["app_size"],
            "installs": parameters["installs"],
            "released": parameters['released']
        }
        return parsed_input

    def get_filtered_data(self) -> pd.DataFrame:
        df = self.df
        parsed_input = visualizer.parse_input(self.parameters)
        df_filtered = df[
            df["category"].isin(parsed_input['categories'])
            & (df['free'].isin(parsed_input['cost']))
            & df["content_rating"].isin(parsed_input['content_rating'])
            & ((df["rating"] > parsed_input['rating'][0]) & (df["rating"] < parsed_input['rating'][1]))
            & (
                (df["rating_count"] > parsed_input['num_of_rating'][0])
                & (df["rating_count"] < parsed_input['num_of_rating'][1])
            )
            & (df["size"] > parsed_input['app_size'][0]) & (df["size"] < parsed_input['app_size'][1])
            & ((df['maximum_installs'] < parsed_input['installs']['max_installs'])
               & (df['maximum_installs'] > parsed_input['installs']['min_installs']))
            & ((df['released'] < parsed_input['released']['max_date'])
               & (df['released'] > parsed_input['released']['min_date']))
        ]
        self.fileterd_df = df_filtered
        return df_filtered

    def plot_bar_categories(self):
        df = self.fileterd_df
        categories_list = []
        count_list = []
        for category in self.parameters["categories"]:
            count_list.append(
                df.loc[df.category == category, "category"].count())
            categories_list.append(category)
        fig = plt.figure(figsize=(20, 10))
        plt.bar(categories_list, count_list, color="maroon", width=0.4)
        plt.xlabel("Category of app ")
        plt.ylabel("Number of occurrences ")
        plt.title("Category wise bar graph of number of occurrences")
        st.success("""APP CATEGORY WISE BAR GRAPH""")
        st.pyplot(fig)

    def plot_bar_content_rating(self):
        df = self.fileterd_df
        content_rating_list = []
        count_list = []
        for content_rating in self.parameters['content_rating']:
            count_list.append(
                df.loc[df.content_rating == content_rating, "content_rating"].count())
            content_rating_list.append(content_rating)
        fig = plt.figure(figsize=(20, 10))
        plt.bar(content_rating_list, count_list, color="blue", width=0.4)
        plt.xlabel("Content rating of app ")
        plt.ylabel("Number of occurrences ")
        plt.title("Category wise bar graph of number of occurrences")
        st.success("CONTENT RATING WISE BAR GRAPH")
        st.pyplot(fig)
