import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

import src.home
import src.skills
import src.tests
import src.radar
import src.ny_taxi
import src.cheatsheet
import src.kmeans
import src.spacy_test

import utils.display as udisp


MENU = {
    "Home" : src.home,
    "Skills": src.skills,
    "Test code": src.tests,
    "Radar chart": src.radar,
    "NY Taxi example": src.ny_taxi,
    "Cheat Sheet": src.cheatsheet,
    "K-means clustering": src.kmeans,
    "NLP with Spacy": src.spacy_test
}

def main():
    st.sidebar.title("Navigate yourself...")
    menu_selection = st.sidebar.radio("Choice your option...", list(MENU.keys()))

    menu = MENU[menu_selection]

    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)

    st.sidebar.info(
        "mailto:mark.versteegh@ogd.nl"
    )
    st.sidebar.info(
        "Skillmatrix/demoapp"
    )

if __name__ == "__main__":
    main()
