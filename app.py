import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=148f24150e8bedc00965e4a735f02e1f&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']

similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    rec_movies = []
    rec_poster = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        rec_movies.append(movies.iloc[i[0]].title)
        rec_poster.append(fetch_poster(movie_id))
    return rec_movies,rec_poster

m_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(m_dict)
st.title('Movie Recommendation System')

selected_option = st.selectbox(
    'Select the movie you like:',
    (movies['title'].values)
)

if st.button('Recommend'):
    names,posters = recommend(selected_option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

