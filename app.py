import pickle
import streamlit as st
import pip._vendor.requests as requests
import bz2

st.set_page_config(layout="wide")
hide_Menu="""
<style>
#MainMenu{
    visibility:hidden;
}
footer{
    visibility:visible;
}
footer:after{
    content:"Project Done by B.INDHRA LOCHAN KUMAR";
    display:block;
    position:relative;
    color:white;
    

}
</style>
"""
def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=088f16bc490a52bea519ce18159473a0&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def fetch_info(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=088f16bc490a52bea519ce18159473a0&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    details = data['overview']
    return details
def fetch_popularity(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=088f16bc490a52bea519ce18159473a0&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    popularity =data['vote_average']
    return popularity
def arraytostrings(val):
        x=''
        x=','.join(val)
        return x;    
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_info=[]
    recommended_movie_crew=[]
    recommended_movie_cast=[]
    recommended_movie_popularity=[]
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_info.append(fetch_info(movie_id)) 
        recommended_movie_popularity.append(fetch_popularity(movie_id))
        recommended_movie_crew.append(arraytostrings(info.iloc[i[0]].crew))
        recommended_movie_cast.append(arraytostrings(info.iloc[i[0]].cast))
    return recommended_movie_names,recommended_movie_posters,recommended_movie_info,recommended_movie_crew,recommended_movie_popularity,recommended_movie_cast


st.header('Movie Recommender System')
st.markdown(hide_Menu,unsafe_allow_html=True)
movies = pickle.load(open('movies.pkl','rb'))
similarity = decompress_pickle('similarity.pbz2')
info = pickle.load(open('info.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,recommended_movie_info,recommended_movie_crew ,recommended_movie_popularity,recommended_movie_cast= recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6,col7,col8,col9,col10 = st.columns(5)
    with col1:
        st.subheader(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        st.write(recommended_movie_info[0])
        st.text("DIRECTOR : ")
        st.text(recommended_movie_crew[0])
        st.text("Cast : \n")
        st.markdown(recommended_movie_cast[0])
        st.write("Popularity of this movies is :",recommended_movie_popularity[0])
    with col2:
        st.subheader(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        st.markdown(recommended_movie_info[1])
        st.text("DIRECTOR : "+" \n")
        st.text(recommended_movie_crew[1])
        st.text("Cast : "+" \n")
        st.markdown(recommended_movie_cast[1])
        st.write("Popularity of this movies is :",recommended_movie_popularity[1])

    with col3:
        st.subheader(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.markdown(recommended_movie_info[2])
        st.text("DIRECTOR : "+" \n")
        st.text(recommended_movie_crew[2])
        st.text("Cast : "+" \n")
        st.markdown(recommended_movie_cast[2])
        st.write("Popularity of this movies is :",recommended_movie_popularity[2])
    with col4:
        st.subheader(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        st.markdown(recommended_movie_info[3])
        st.text("DIRECTOR : "+" \n")
        st.text(recommended_movie_crew[3])
        st.text("Cast : "+" \n")
        st.markdown(recommended_movie_cast[3])
        st.write("Popularity of this movies is :",recommended_movie_popularity[3])
    with col5:
        st.subheader(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        st.markdown(recommended_movie_info[4])
        st.text("DIRECTOR : "+" \n")
        st.text(recommended_movie_crew[4])
        st.text("Cast : "+" \n")
        st.markdown(recommended_movie_cast[4])
        st.write("Popularity of this movies is :",recommended_movie_popularity[4])
    with col6:
        st.subheader(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
        st.markdown(recommended_movie_info[5])
        st.text("DIRECTOR : "+" \n")
        st.text(recommended_movie_crew[5])
        st.text("Cast : "+" \n")
        st.markdown(recommended_movie_cast[5])
        st.write("Popularity of this movies is :",recommended_movie_popularity[5])
    with col7:
        st.subheader(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
        st.markdown(recommended_movie_info[6])
        st.text("DIRECTOR : "+" \n")
        st.text(recommended_movie_crew[6])
        st.text("Cast : "+" \n")
        st.markdown(recommended_movie_cast[6])
        st.write("Popularity of this movies is :",recommended_movie_popularity[6])

    with col8:
        st.subheader(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
        st.markdown(recommended_movie_info[7])
        st.text("DIRECTOR : "+" \n")
        st.text(recommended_movie_crew[7])
        st.text("Cast : "+" \n")
        st.markdown(recommended_movie_cast[7])
        st.write("Popularity of this movies is :",recommended_movie_popularity[7])
    with col9:
        st.subheader(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
        st.markdown(recommended_movie_info[8])
        st.text("DIRECTOR : "+" \n")
        st.text(recommended_movie_crew[8])
        st.text("Cast : "+" \n")
        st.markdown(recommended_movie_cast[8])
        st.write("Popularity of this movies is :",recommended_movie_popularity[8])
    with col10:
        st.subheader(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
        st.markdown(recommended_movie_info[9])
        st.text("DIRECTOR : "+" \n")
        st.text(recommended_movie_crew[9])
        st.text("Cast : "+" \n")
        st.markdown(recommended_movie_cast[9])
        st.write("Popularity of this movies is :",recommended_movie_popularity[9]) 
      
