# pages/3_Input_Table.py

import streamlit as st
from db import conn
import pandas as pd

st.title("📥 Input Table Viewer")

input_df = pd.read_sql_query("SELECT * FROM input", conn)
st.dataframe(input_df)
