import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

@st.cache()
def predict(df,feat):
	x=df[feat]
	y=df["price"]
	X_train,X_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.33)
	lr=LinearRegression().fit(X_train,y_train)
	score_train=lr.score(X_train,y_train)
	y_train_pred=lr.predict(X_train)
	score_test=lr.score(X_test,y_test)
	y_test_pred=lr.predict(X_test)
	r2=r2_score(y_test,y_test_pred)
	mae=mean_absolute_error(y_test,y_test_pred)
	mse=mean_squared_error(y_test,y_test_pred)
	rmse=np.sqrt(mse)
	return score_train,score_test,y_train_pred,y_test_pred,r2,mse,mae,rmse

def app(cars_df):
	st.markdown("<p style='color:green;fontsize:40px'>App uses <b>Linear Regression</b> to predict the price of a car.",unsafe_allow_html=True)
	st.subheader("Label")
	feats=cars_df.columns[:-1]
	for i in feats[:-1]:
		st.slider(i,float(cars_df[i].min()),float(cars_df[i].max()))
	dr_fd=st.radio("Is it a forward drivewheel car?",("Yes","No"))
	if dr_fd=="No":
		dr_fd=0
	else:
		dr_fd=1
	if st.button("Predict"):
		st.subheader("Results")
		score_train,score_test,y_train_pred,y_test_pred,r2,mse,mae,rmse=predict(cars_df,feats)
		st.success(f"The predicted price of the car is {y_test_pred[0]:.2f}$.")
		st.info(f"Accuracy of this model is {score_train*100:.3f}%.")
		st.info(f"The R² score of the model is {r2*100:.3f}%.")
		st.info(f"The Mean Squared Error of the model is {mse*100:.3f}%.")
		st.info(f"The Mean Absolute Error of the model is {mae*100:.3f}%.")
		st.info(f"The Root Mean Squred Error of the model is {rmse*100:.3f}%.")