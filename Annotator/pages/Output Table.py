# pages/4_Output_Table.py

import streamlit as st
from db import conn
import pandas as pd
import json

st.title("📤 Output Table Viewer")

output_df = pd.read_sql_query("SELECT * FROM output", conn)

if not output_df.empty:
    st.dataframe(output_df)

    # Optionally decode JSON
    st.subheader("View Tags for a Slide")
    slide_id = st.selectbox("Choose Slide ID", output_df['slide_id'])
    selected = output_df[output_df['slide_id'] == slide_id].iloc[0]
    tags = json.loads(selected['tags'])
    for tag in tags:
        st.write(f"- **{tag['key']}**: {tag['value']}")
else:
    st.info("No output data yet.")
