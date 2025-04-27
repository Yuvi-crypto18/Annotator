# pages/1_Ingestion.py

import streamlit as st
from db import conn
import pandas as pd
import uuid

st.title("🛠 Slide Ingestion")

uploaded_file = st.file_uploader("Upload your presentation (PPTX)", type=["pptx"])

if uploaded_file:
    # Dummy: we will simulate reading slides
    presentation_id = str(uuid.uuid4())
    slides = [
        {"name": f"Slide {i}", "slide_id": str(uuid.uuid4()), "slide_number": i, "image": None}
        for i in range(1, 6)
    ]

    cursor = conn.cursor()
    for slide in slides:
        cursor.execute('''
            INSERT INTO input (presentation_id, name, slide_id, slide_number, image)
            VALUES (?, ?, ?, ?, ?)
        ''', (presentation_id, slide['name'], slide['slide_id'], slide['slide_number'], slide['image']))
    
    conn.commit()
    st.success(f"Uploaded {len(slides)} slides!")

# Show table
df = pd.read_sql_query("SELECT * FROM input", conn)
st.dataframe(df)
