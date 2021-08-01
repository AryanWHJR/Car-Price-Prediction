import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="Car price prediction",page_icon=":car:",layout="centered",initial_sidebar_state="auto")

@st.cache()

def load_data():
	df=pd.read_csv("car-prices.csv")
	df=df[['carwidth', 'enginesize', 'horsepower', 'drivewheel', 'price']]
	df["drivewheel"]=df["drivewheel"].map({"rwd":0,"fwd":1,"4wd":2})
	return df
df=load_data()
import home,data,plots,predict
pages_dict = {"Home": home,
             "View Data": data, 
             "Visualise Data": plots,
             "Predict": predict}
st.sidebar.title("Navigation")
page=st.sidebar.radio("Go to ...",tuple(pages_dict.keys()))
if page=="Home":
	home.app()
elif page=="View Data":
	data.app(df)
elif page=="Visualise Data":
	plots.app(df)
else:
	predict.app(df)