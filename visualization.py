import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from typing import Tuple,List,Dict


class visualizer:
    def __init__(self):
        pass

    @classmethod
    def parse_input(**parameters):
        categories: Tuple = parameters["categories"]
        content_rating: Tuple = parameters["content_rating"]
        rating: Tuple= parameters["rating"]
        num_of_rating: Tuple = parameters["num_of_rating"]
        cost: str = parameters["cost"]
        app_size: tuple[str] = parameters["app_size"]

        query_cost = 1 if cost == 'FREE' else 2 if cost == "PAID" else 2
        parsed_input = {'categories':list(categories),
                        }

    


def plot_bar_categories(categories, df):
    categories_list = []
    count_list = []
    for category in categories:
        count_list.append(df.loc[df.category == category, "category"].count())
        categories_list.append(category)
    fig = plt.figure(figsize=(20, 10))
    plt.bar(categories_list, count_list, color="maroon", width=0.4)
    plt.xlabel("Category of app ")
    plt.ylabel("Number of occurrences ")
    plt.title("Category wise bar graph of number of occurrences")
    st.success("APP CATEGORY WISE BAR GRAPH")
    st.pyplot(fig)


def plot_bar_content_rating(content_ratings, df):
    content_rating_list = []
    count_list = []
    for content_rating in content_ratings:
        count_list.append(
            df.loc[df.content_rating == content_rating,
                   "content_rating"].count()
        )
        content_rating_list.append(content_rating)
    fig = plt.figure(figsize=(20, 10))
    plt.bar(content_rating_list, count_list, color="blue", width=0.4)
    plt.xlabel("Content rating of app ")
    plt.ylabel("Number of occurrences ")
    plt.title("Category wise bar graph of number of occurrences")
    st.success("CONTENT RATING WISE BAR GRAPH")
    st.pyplot(fig)
