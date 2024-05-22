#WaterMarker v0.1, watermark your PDFs in a click beat!
"""
import streamlit as st
from io import BytesIO
from PyPDF2 import PdfWriter, PdfReader

def add_watermark_to_pdf(input_pdf, watermark_text):

    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        # Add the watermark text
        page.merge_text(watermark_text, x=100, y=100, fontsize=20)
        # Add the modified page to the output PDF
        pdf_writer.add_page(page)

    # Save the output PDF to a bytes buffer
    output_pdf = BytesIO()
    pdf_writer.write(output_pdf)
    output_pdf.seek(0)
    return output_pdf

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
uploaded_file = st.file_uploader("Choose a file", type="pdf")
watermark_text = st.text_area("Watermark Text :", max_chars=250)

#Main Programe Loop
if uploaded_file is not None:
    # Add watermark to the PDF
    watermarked_pdf = add_watermark_to_pdf(uploaded_file, watermark_text)

    # Display download button for the watermarked PDF
    st.download_button(
        label="Download Watermarked PDF",
        data=watermarked_pdf,
        file_name="output.pdf",
        mime="application/pdf"
    )"""

import streamlit as st
from PyPDF2 import PdfReader, PdfWriter

def watermark_pdf(input_pdf, watermark_text, output_filename):
  """Adds watermark text to each page of a PDF

  Args:
      input_pdf (str): Path to the input PDF file
      watermark_text (str): Text to be added as watermark
      output_filename (str): Name of the output PDF file
  """
  watermark_reader = PdfReader(input_pdf)
  watermark_writer = PdfWriter()

  for page_num in range(watermark_reader.getNumPages()):
    page = watermark_reader.getPage(page_num)
    watermark_writer.addPage(page)

  # Add watermark text properties
  text_width = watermark_reader.getPage(0).mediaBox.getWidth()  # Adjust width as needed
  text_height = watermark_reader.getPage(0).mediaBox.getHeight()  # Adjust height as needed
  watermark_writer.addOverlay({'/Contents': f"q {text_width} 0 0 {text_height} 0 0 cm /Tx BMC /Font /Helvetica 12.0 Tf {watermark_text} Tj EMC Q"})

  with open(output_filename, 'wb') as output_file:
    watermark_writer.write(output_file)

st.title("PDF Watermark App")

uploaded_file = st.file_uploader("Choose a PDF file to watermark")

if uploaded_file is not None:
  watermark_text = st.text_input("Enter watermark text (up to 250 characters)", max_chars=250)
  if watermark_text:
    if len(watermark_text) > 250:
      st.error("Watermark text exceeds character limit (250 characters)")
    else:
      with open(uploaded_file.name, 'rb') as input_pdf:
        output_filename = f"watermarked_{uploaded_file.name}"
        watermark_pdf(input_pdf, watermark_text, output_filename)
        st.success(f"Watermark added! Download your watermarked PDF: {output_filename}")
        st.download_button("Download", data=open(output_filename, 'rb').read(), file_name=output_filename)
