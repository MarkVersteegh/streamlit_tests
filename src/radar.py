import pandas as pd
import time
import random
import plotly.express as px
import streamlit as st

def write():
    placeholder = st.empty()
    start_button = st.empty()

    def radar_chart():  
        df = pd.DataFrame(dict(
        r=[random.randint(0,5),
        random.randint(0,5),
        random.randint(0,5),
        random.randint(0,5),
        random.randint(0,5),
        random.randint(0,5),
        random.randint(0,5),
        random.randint(0,5),
        random.randint(0,5),
        random.randint(0,5)],
        #theta=['0','1','2','3','4','5','6','7','8','9']))
        theta=['a','b','c','d','e','f','g','h','i','j']))
        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
        placeholder.write(fig)

    radar_chart()
    
if __name__ == "__main__":
    write()
