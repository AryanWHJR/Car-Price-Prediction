import streamlit as st
import pandas as pd
import numpy as np

def app(cars_df):
	st.header("View Data")
	with st.beta_expander("View Dataset"):
		st.table(cars_df)
	st.subheader("Column Description")
	col1,col2=st.beta_columns(2)
	with col1:
		if st.checkbox("Show All Column Names"):
			st.table(cars_df.columns)
	with col2:
		if st.checkbox("View Column Data"):
			col=st.selectbox("Select Column",('carwidth', 'enginesize', 'horsepower', 'drivewheel', 'price'))
			if col=="carwidth":
				st.write(cars_df[col])
			elif col=="enginesize":
				st.write(cars_df[col])
			elif col=="horsepower":
				st.write(cars_df[col])
			elif col=="drivewheel":
				st.write(cars_df[col])
			else:
				st.write(cars_df[col])
	if st.checkbox("Show Summary"):
		st.table(cars_df.describe())