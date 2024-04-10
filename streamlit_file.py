#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# In[2]:


df = pd.read_csv('car_data.csv')


# In[3]:


car_name = st.sidebar.text_input('Car Name')


# In[4]:


transmission = st.sidebar.multiselect('Transmission', ['Automatic', 'Manual'], default = ['Automatic', 'Manual'])


# In[5]:


selling_price = st.sidebar.slider('Selling Price Range', 0, 20, (0, 20))


# In[6]:


year = st.sidebar.slider('Year Range', 2000, 2024, (2000, 2024))


# In[7]:


submit = st.sidebar.button('Submit')
if submit:
    if car_name:
        df = df[df['Car_Name'].str.contains(car_name, case=False)]
    if transmission:
        df = df[df['Transmission'].isin(transmission)]
    df = df[df['Selling_Price'].between(*selling_price)]
    df = df[df['Year'].between(*year)]
st.write(df)


# In[ ]:




