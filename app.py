import streamlit as st 
import pickle 
import pandas as pd
import requests

def fetch_poster(movie_id):
    requests.get("")


similarity = pickle.load(open("similarity.pkl" , "rb"))
def recommend(movie):
    indx = movies[movies["title"] == movie].index[0]
    dist = similarity[indx]
    movie_list = sorted(list(enumerate(dist)) , reverse= True , key = lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        #fetch poster from api 
        recommended_movies.append(movies["title"][i[0]])
    
    return recommended_movies

movie_dict = pickle.load(open("movie_dict.pkl" , "rb"))
movies = pd.DataFrame(movie_dict)

st.title("movie Recommender System")

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies["title"].values)

if st.button("recommend"):
    recomendations = recommend(selected_movie_name)
    for i in recomendations:
        st.write(i)






