import streamlit as st
import pandas as pd
from generate import make_invoice, make_certificate
import os
st.title("PDF Money Maker")
st.write("Upload CSV to generate PDFs")
uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df)
    if st.button("Generate"):
        os.makedirs("output", exist_ok=True)
        for _, row in df.iterrows():
            make_invoice(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]))
        st.success("Done! Check output folder")
