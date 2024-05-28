import streamlit as st
from PyPDF2 import PdfReader, PdfWriter

def watermark_pdf(input_pdf, watermark_text, output_filename):
  """
  Watermarks a PDF document with the provided text string.

  Args:
      input_pdf (str): Path to the input PDF file.
      watermark_text (str): Text string to be used as the watermark.
      output_filename (str): Name of the watermarked output PDF file.

  Returns:
      None
  """

  with open(input_pdf, 'rb') as input_file, open(output_filename, 'wb') as output_file:
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]
      page.merge_page(PdfReader(open('watermark.pdf', 'rb')).pages[0])  # Pre-created watermark PDF

      pdf_writer.addPage(page)

    pdf_writer.write(output_file)

st.title('PDF Watermark App')

uploaded_file = st.file_uploader("Choose a PDF document:", type='pdf')
watermark_text = st.text_input("Enter watermark text:")
save_as = st.text_input("Save watermarked PDF as:")

if uploaded_file is not None and watermark_text and save_as:
  # Create a temporary watermark PDF with formatting options
  with open('watermark.pdf', 'wb') as watermark_file:
    from reportlab.pdfgen import canvas
    c = canvas.Canvas(watermark_file)
    c.setFont("Helvetica", 30)  # Adjust font and size as desired
    c.setFillColorRGB(0.8, 0.8, 0.8)  # Set gray color (opacity can be adjusted)
    c.drawCenteredString(300, 200, watermark_file.name)  # Center watermark
    c.save()

  try:
    with open(uploaded_file.name, 'rb') as in_f, open(save_as, 'wb') as out_f:
      watermark_pdf(in_f.name, watermark_text, out_f.name)
    st.success('PDF watermarked successfully!')
  except Exception as e:
    st.error(f"Error: {e}")
  finally:
    # Remove temporary watermark PDF after processing
    import os
    os.remove('watermark.pdf')

else:
  st.info("Please upload a PDF, enter watermark text, and a filename to save the output.")
