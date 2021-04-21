import streamlit as st 
import pandas as pd 
import base64
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
import requests 
from bs4 import BeautifulSoup


#web scraping to get the list of world countries
@st.cache
def countries():
    url='https://www.worldometers.info/geography/alphabetical-list-of-countries/'
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'lxml')
    elements=soup.find_all('td',style="font-weight: bold; font-size:15px")
    a=[]
    for i in elements:
        a.append(i.text)

    return a 
country=countries()
#sidebar section
st.sidebar.header('User Input Features')
selected=st.sidebar.selectbox('Country',country)
#main section
st.title('World Covid-19 Exploratory Data Analysis')
st.markdown("""
*Built by Igata John*""")
@st.cache
def load_data():
   url='https://www.worldometers.info/coronavirus/country/'+selected.lower()+'/'
   r=requests.get(url)
   soup=BeautifulSoup(r.content,'lxml')
   frank=soup.find_all('div',id='maincounter-wrap')
   another=[]
   data=[]
   for i in frank:
       another.append(i.h1.text)
       data.append(i.span.text)
   main=dict(zip(another,data))
   return main
igatus=load_data()
col1,col2=st.beta_columns((1,3))
with col1:
    for j in igatus.keys():
        st.info(j)
with col2:
    for v in igatus.values():
        st.warning(v)
value=igatus.values()
if st.button('Visualize'):
    st.line_chart(value)


