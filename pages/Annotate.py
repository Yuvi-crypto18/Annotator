# pages/2_Annotate.py

import streamlit as st
from db import conn
import pandas as pd
import json

st.title("📝 Annotate Slides")

# Load slides
slides_df = pd.read_sql_query("SELECT * FROM input", conn)

slide_number = st.selectbox("Select a slide number", slides_df['slide_number'])

slide = slides_df[slides_df['slide_number'] == slide_number].iloc[0]

st.subheader(f"Slide {slide_number}: {slide['name']}")

# Annotate
st.write("Add tags:")

tags = []
with st.form("tag_form"):
    for i in range(3):  # Allow 3 tags
        key = st.text_input(f"Key {i+1}", key=f"key_{i}")
        value = st.text_input(f"Value {i+1}", key=f"value_{i}")
        if key and value:
            tags.append({"key": key, "value": value})
    submitted = st.form_submit_button("Save Tags")
    
    if submitted:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO output (presentation_id, slide_id, tags)
            VALUES (?, ?, ?)
        ''', (slide['presentation_id'], slide['slide_id'], json.dumps(tags)))
        conn.commit()
        st.success("Tags saved!")

# View existing
output_df = pd.read_sql_query("SELECT * FROM output", conn)
if not output_df.empty:
    st.write("Existing Annotations")
    st.dataframe(output_df)
