#WaterMarker v0.1, watermark your PDFs in a click beat!

import streamlit as st
from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader

def add_watermark_to_pdf(input_pdf, output_pdf_path, watermark_text):
    """
    Adds a watermark (text) to each page of the input PDF file.

    Args:
        input_pdf_path (str): Path to the input PDF file.
        output_pdf_path (str): Path to save the output PDF file.
        watermark_text (str): Text to be used as the watermark.

    Returns:
        None
    """
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()

    for page_num, page in enumerate(pdf_reader.pages, start=1):
        # Create a new page with the watermark
        watermark_page = pdf_reader.getPage(page_num)
        watermark_page.mergePage(page)

        # Add the watermark text
        watermark_page.merge_text(watermark_text, x=100, y=100, fontsize=20)

        # Add the modified page to the output PDF
        pdf_writer.addPage(watermark_page)

    # Save the output PDF
    with open(output_pdf_path, "wb") as output_file:
        pdf_writer.write(output_file)

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
    if input_text is not None:
        add_watermark_to_pdf(uploaded_file, input_text, 'watermarkedfile.pdf')

