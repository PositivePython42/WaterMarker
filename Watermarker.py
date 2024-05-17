#WaterMarker v0.1, watermark your PDFs in a click beat!

import streamlit as st
from pathlib import Path
from typing import Union, Literal, List
from PyPDF2 import PdfWriter, PdfReader

def add_watermark_to_pdf(content_pdf, watermark_text: str, pdf_result: Path):
    # Create a watermark page with the specified text
    watermark_page = PdfReader().add_page(width=100, height=100)
    watermark_page.merge_text_watermark(watermark_text)

    # Read the original PDF
    reader = PdfReader(content_pdf)
    writer = PdfWriter()

    # Merge the watermark page with each page in the original PDF
    for index, content_page in enumerate(reader.pages):
        content_page.merge_page(watermark_page)
        writer.add_page(content_page)

    # Save the modified PDF with the watermark
    with open(pdf_result, "wb") as fp:
        writer.write(fp)

#Setup The Streamlit Screen
st.set_page_config(layout="wide")
st.title('**WaterMarker** *Personalise your PDFs*')

with st.expander('About This App'):
    st.write('Use WaterMarker to put personalised water marks on your PDFs to personalise them before distribution;\n'
             '1. Drag and Drop your original PDF file in the box below.\n'
             '2. Enter the text you\'d like at the top, middle and bottom of your document.\n'
             '3. Check the text is exactly what you want!\n'
             '4. Press the button and the file will get saved to your computer.'
             )
    st.write('Email me at sean@positiveatwork.co.uk with any feedback, or raise an issue on GitHub https://github.com/PositivePython42/WaterMarket/issues')
st.header('Upload your data here')
st.subheader('Please make sure the file is a PDF.')
uploaded_file = st.file_uploader("Choose a file")

#Main Programe Loop
if uploaded_file is not None:
    input_text = st.text_input("Watermark Text :")
    add_watermark_to_pdf(uploaded_file, input_text, 'watermarkedfile.pdf')

