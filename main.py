import streamlit as st
import base64 

st.set_page_config(layout='wide')

def displayPDF(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}#view=TwoPage" width="100%" height="1000" type="application/pdf"></iframe>'

    st.markdown(pdf_display, unsafe_allow_html=True)