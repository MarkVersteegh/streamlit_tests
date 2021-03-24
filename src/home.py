import pathlib
import utils.display as udisp

import streamlit as st


def write():
    udisp.title_awesome("Streamlit Demo App- Explanation")
    udisp.render_md("resources/home_info.md")
    with st.beta_expander('Covid dashboard example'):
        st.video("resources/streamlit-app-2021-03-03-21-03-01.webm")
