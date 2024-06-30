import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("happy.csv")

st.title("In Search for Happiness")
x_axis = st.selectbox("Select data for the X axis",
                      ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select data for the Y axis",
                      ("GDP", "Happiness", "Generosity"))

st.subheader(f"{x_axis} and {y_axis}")

match x_axis:
    case "GDP":
        x_array = df["gdp"]
    case "Happiness":
        x_array = df["happiness"]
    case "Generosity":
        x_array = df["generosity"]

match y_axis:
    case "GDP":
        y_array = df["gdp"]
    case "Happiness":
        y_array = df["happiness"]
    case "Generosity":
        y_array = df["generosity"]

figure = px.scatter(x=x_array, y=y_array, labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)
