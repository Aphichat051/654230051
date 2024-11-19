import streamlit as st
import requests as pd

st.titla("website Developing using Python")
st.header("website Developing using Python")

st.image('img/323283346_5718974981503456_3654895059501341451_n.jpg')
st.subheader("Kairung Hengpraprohm")

dt=pd.read_csv('./data/iris-3.csv')
st.header()
st.wite(dt.head(10))