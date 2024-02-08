import streamlit as st
import pandas as pd
import numpy as np 

st.header('IRIS FLOWER DAHSBOARD',divider='rainbow')
st.sidebar.title('Description')
st.sidebar.write('''The Iris dataset is a popular dataset in m
                 achine learning and statistics. It is often used for educational purposes and
                  serves as a standard reference dataset for testing classification algorithms. 
                 The dataset consists of 150 samples of iris flowers, each belonging to one of three species:
                  Setosa, Versicolor, and Virginica. Each sample contains four features:
                 -Sepal length (in cm)
                 -Sepal length (in cm)
                 -Petal length (in cm)
                 -Petal width (in cm)''')

data= pd.read_csv('my_env\Data\iris.csv')
species_counts = data['species'].value_counts()
st.title('Distribution of Iris Species')
st.write("Percentage of each species in the dataset:")
st.write(species_counts)
st.write("Pie chart:")
st.write(species_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90))



















