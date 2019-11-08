# This is the "Getting Started" tutotial for streamlit
# https://streamlit.io/docs/getting_started.html


"()"
import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('My First App')

# Write a DataFrame
st.write("First attempt at writing a dataframe")
st.write(pd.DataFrame({
    'first_column': [1, 2, 3, 4], 
    'second_column': [10, 20, 30, 40]
}))

# check out other functions for displaying data like st.dataframe and st.table

# with python 3, you can write to the app with no streamlit commands 
st.write("Another attempt at writing a table, this time with no streamlit commands")
df = pd.DataFrame({
    'first_column': [1, 2, 3, 4], 
    'second_column': [10, 20, 30, 40]
})

df # write the dataframe to the app

# Draw a line chart with pandas
st.write("draw a line chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

# Draw a map
st.write("Draw a map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

#Add some widgets

# checkbox
st.write('Use a checkbox')
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )

    st.line_chart(chart_data)

# selectbox
st.write('use a select box to choose from a series')
option = st.selectbox(
    'Which number do you like best?',
    df['first_column']
)

'You selected: ', option

# move widgets into a sidebar for a cleaner look
option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first_column'],
    key=1
)

'You Selected: ', option

# progress bar
'Starting a long computation'

# Add a place holder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i+1)
    time.sleep(0.1)

'And we are done'