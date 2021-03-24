import streamlit as st
import numpy as np
import pandas as pd

def write():
    if st.checkbox('Show testing stuff'):
        st.write("Here's our first attempt at using data to create a table:")
        st.write(pd.DataFrame({
            'first column': [1, 2, 3, 4],
            'second column': [10, 20, 30, 40]
        }))


        map_data = pd.DataFrame(
            np.random.randn(10, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon'])

        st.map(map_data)


        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

        st.line_chart(chart_data)



        df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
        })

        option = st.selectbox(
            'Which number do you like best?',
            df['first column'])

        'You selected: ', option

        #Progress bar example

        import time
        my_bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)