# Use streamlit to create an app to explore Uber Pickup Data
# Tutorial: https://streamlit.io/docs/tutorial/create_a_data_explorer_app.html

import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber Pickups in NYC')

# Load some data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache
def load_data(nrows):
    """Load and clean a given number of rows of data"""
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element to let user know the data is loading.
data_load_state = st.text('Loading Data ...')

# Load 10,000 rows of data into the dataframe
data = load_data(10_000)

# Notify user that data was successfully loaded
data_load_state.text('Loading data ... Done! (using @st.cache)')

# add a subheader and a printout of the raw data table
if st.checkbox('Show data table'):
    st.subheader('Raw data')
    st.write(data)

# what are the busiest hours
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# add a map 
hour_to_filter = st.slider('hour', 0, 24, 17)
filtered_data  = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
