import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff

st.header('1. Altair Scatter Plot')#having 5 aprameter
# Create a DataFrame with 500 rows and 5 columns of random numbers, labeled 'a' through 'e'.
chart_data = pd.DataFrame(np.random.randn(500,5), columns = ['a','b','c','d','e'])
# Create an Altair scatter plot with x-axis as 'a', y-axis as 'b', size of the circles as 'c', and tooltip showing values of 'a', 'b', 'c', 'd', and 'e'.
# OR # Creating an Altair scatter plot with circles based on the random data
#Encoding x-axis with column 'a', y-axis with column 'b', and size with column 'c'
#Tooltip shows information for columns 'a', 'b', 'c', 'd', and 'e'
chart = alt.Chart(chart_data).mark_circle().encode(x = 'a' , y = 'b', size = 'c',
        tooltip = ['a','b','c','d','e'])
st.altair_chart(chart)#Displaying the Altair chart in the Streamlit app


st.header('2. Interactive Charts')
st.subheader('2.1 Line Chart')
df = pd.read_csv('lang_data.csv')
#Extracting the column names of the DataFrame as a list ('lang_list')
lang_list = df.columns.tolist()
#Creating a multiselect widget using Streamlit for selecting multiple languages ('lang_choices')
lang_choices = st.multiselect('Choose your language', lang_list)
#Subsetting the DataFrame ('df') to include only the selected languages ('lang_choices') in a new DataFrame ('new_df')
new_df = df[lang_choices]
#Generating a line chart using Streamlit with the selected language data ('new_df')
st.line_chart(new_df)

st.subheader('2.2 Area Chart')
st.area_chart(new_df)

st.header('3. Data Visualisation with Plotly')
st.subheader('3.1 Displaying the dataset')
df = pd.read_csv('tips.csv')
st.dataframe(df.head())#making df

st.subheader('3.2 Pie Chart') 
#Create a pie chart using Plotly Express with 'total_bill' as values and 'day' as names from the DataFrame 'df'.
fig = px.pie(df, values='total_bill', names='day')  
st.plotly_chart(fig) # Display the Plotly pie chart in the Streamlit app.

st.subheader('3.3 Pie Chart with Multiple Parameters')  # Set a subheader for the section.
# fig = px.pie(df, values='total_bill', names='day', opacity=0.7, color_discrete_sequence=px.colors.sequential.RdBu)
fig = px.pie(df,  # Create a pie chart using Plotly Express.
             values='total_bill',  # Use the 'total_bill' column for the values.
             names='day',  # Use the 'day' column for labeling different sections of the pie chart.
             opacity=0.7,  # Set the opacity of the chart to 0.7 for a semi-transparent effect.
             color_discrete_sequence=px.colors.sequential.RdBu)  # Define a color sequence for different categories.

# st.plotly_chart(fig)
st.plotly_chart(fig)  # Display the Plotly chart using Streamlit.



