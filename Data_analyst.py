import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='white', context='notebook', # Styles de Seaborn
        palette=['#ff5252', '#1de9b6'])

def main():
    st.title("Hi, l'm Hermann ! welcome to my EDA Streamlit Application")

    st.header("Upload your CSV data file")
    data_file = st.file_uploader("Upload CSV", type=["csv"])

    if data_file is not None:
        data = pd.read_csv(data_file)
        st.write("Data overview:")
        st.write(data.head())

        st.sidebar.header("Choose the visualization type")
        plot_options = ["Bar plot", "Scatter plot", "Histogram", "Box plot","Line plot"]
        selected_plot = st.sidebar.selectbox("Choose a plot type", plot_options)

        st.write("Information on your data (Shape and type of columns) :")
        st.write(data.shape)
        st.write(data.dtypes)


        st.write("descriptive statistics of your data :")
        st.write(data.describe())

        st.write("Missing Values : ")
        st.write(data.isna().sum())

        if selected_plot == "Bar plot":
            x_axis = st.sidebar.selectbox("Select x-axis", data.columns)
            y_axis = st.sidebar.selectbox("Select y-axis", data.columns)
            st.write("Bar plot:")
            fig, ax = plt.subplots()
            sns.barplot(x=data[x_axis], y=data[y_axis], ax=ax)
            st.pyplot(fig)
        if selected_plot == "Line plot":
            x_axis = st.sidebar.selectbox("Select x-axis", data.columns)
            y_axis = st.sidebar.selectbox("Select y-axis", data.columns)
            st.write("Line plot :")
            fig, ax = plt.subplots()
            sns.lineplot(x=data[x_axis], y=data[y_axis], ax=ax)
            st.pyplot(fig)
        elif selected_plot == "Scatter plot":
            x_axis = st.sidebar.selectbox("Select x-axis", data.columns)
            y_axis = st.sidebar.selectbox("Select y-axis", data.columns)
            st.write("Scatter plot:")
            fig, ax = plt.subplots()
            sns.scatterplot(x=data[x_axis], y=data[y_axis], ax=ax)
            st.pyplot(fig)

        elif selected_plot == "Histogram":
            column = st.sidebar.selectbox("Select a column", data.columns)
            bins = st.sidebar.slider("Number of bins", 5, 100, 20)
            st.write("Histogram:")
            fig, ax = plt.subplots()
            sns.histplot(data[column], bins=bins, ax=ax)
            st.pyplot(fig)

        elif selected_plot == "Box plot":
            column = st.sidebar.selectbox("Select a column", data.columns)
            st.write("Box plot:")
            fig, ax = plt.subplots()
            sns.boxplot(data[column], ax=ax)
            st.pyplot(fig)

if __name__ == "__main__":
    main()