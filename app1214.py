import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the Titanic dataset from CSV file
titanic_data = pd.read_csv('data/titanic.csv')

# Group the data by 'Sex' and 'Survived', and count the number of occurrences
grouped_data = titanic_data.groupby(['Sex', 'Survived']).size().unstack()

# Streamlit App
st.title('Survival Ratio by Gender in Titanic Dataset')

# Plot the bar chart using Streamlit's st.pyplot
fig, ax = plt.subplots()
grouped_data.plot(kind='bar', stacked=True, color=['#FF7F50', '#87CEEB'], ax=ax)
plt.title('Survival Ratio by Gender in Titanic Dataset')
plt.xlabel('Gender')
plt.ylabel('Number of Passengers')
plt.legend(['Did not Survive', 'Survived'], loc='upper right')

# Show the bar chart
st.pyplot(fig)
