import pickle
import numpy as np
import streamlit as st
import pandas as pd

df = pickle.load(open('df.pkl', 'rb'))
df2 = pickle.load(open('df2.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
df2 = pd.DataFrame(df2)
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))


def fetch_Image(name):
    arr = books[books['Book-Title'] == name]['Image-URL-M'].head(1).tolist()

    for i in arr:
        return i


def book_recommendation(name):
    index = np.where(df2.index == name)[0][0]
    score = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

    names = []
    images = []
    for i in score:
        names.append(df2.index[i[0]])
        images.append(fetch_Image(df2.index[i[0]]))
    return names, images


st.title("Movie Recommendation System")
st.subheader("Enter to get Best Recommendation")

col1, col2 = st.columns([3, 1])
with col1:
    option = st.selectbox("",
                          df2.index)
with col2:
    st.markdown("""
            <style>
            .stButton > button {
                width: 200px;
                height: 50px;
            }
            </style>
            """, unsafe_allow_html=True)
    button = st.button("Recommend")

if button:
    st.subheader('Recommended Movie')
    recommendations, images = book_recommendation(option)
    # for i, j in zip(recommendations, images):
    #     st.write(i)
    #     st.image(j)
    c1, c2, c3, c4, c5 = st.columns(5)
    columns = [c1, c2, c3, c4, c5]
    for i, j, k in zip(recommendations, images, columns):
        with k:
            st.write(i)
            st.image(j)
