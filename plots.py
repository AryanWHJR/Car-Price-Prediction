import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
def app(df):
	st.header("Viualise Data")
	plot_types=st.multiselect("Choose plots to visualise",("Scatter plot","Correlation heatmap","Box plot","Histogram"))
	st.set_option('deprecation.showPyplotGlobalUse', False)
	if "Correlation heatmap" in plot_types:
		st.subheader("Correlation Heatmap")
		plt.figure(figsize=(12,12))
		sns.heatmap(df.corr(),annot=True)
		st.pyplot()
	if "Scatter plot" in plot_types:
		st.subheader("Scatter Plot")
		column=st.selectbox("Select the X-axis to create Scatter plot.",tuple(df.columns[:-1]))
		plt.figure(figsize=(12,8))
		sns.scatterplot(x=df[column],y=df["price"])
		st.pyplot()
	if "Box plot" in plot_types:
		st.subheader("Box Plot")
		column=st.selectbox("Select the column to create Box plot.",tuple(df.columns))
		plt.figure(figsize=(12,2))
		sns.boxplot(df[column])
		st.pyplot()
	if "Histogram" in plot_types:
		st.subheader("Histogram")
		column=st.selectbox("Select the column to create Histogram.",tuple(df.columns))
		plt.figure(figsize=(12,8))
		sns.histplot(x=df[column])
		st.pyplot()