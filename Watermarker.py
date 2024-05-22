#WaterMarker v0.1, watermark your PDFs in a click beat!

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
      with open(uploaded_file, 'rb') as input_pdf:
        output_filename = f"watermarked_{uploaded_file}"
        watermark_pdf(input_pdf, watermark_text, output_filename)
        st.success(f"Watermark added! Download your watermarked PDF: {output_filename}")
        st.download_button("Download", data=open(output_filename, 'rb').read(), file_name=output_filename)