#WaterMarker v0.1, watermark your PDFs in a click beat!

import streamlit as st
from PyPDF2 import PdfReader, PdfWriter

def watermark_pdf(input_pdf, watermark_text, output_filename, font_size=12, font_family="Helvetica", text_position=(0.5, 0.5), text_color=(0, 0, 0)):
  """Adds watermark text to each page of a PDF with customizable properties.

  Args:
      input_pdf (str): Path to the input PDF file
      watermark_text (str): Text to be added as watermark
      output_filename (str): Name of the output PDF file
      font_size (int, optional): Size of the watermark text. Defaults to 12.
      font_family (str, optional): Font family of the watermark text. Defaults to "Helvetica".
      text_position (tuple, optional): Position of the watermark text relative to the page (x, y). Defaults to (0.5, 0.5) (center).
      text_color (tuple, optional): Color of the watermark text (RGB values). Defaults to black (0, 0, 0).
  """
  watermark_reader = PdfReader(input_pdf)
  watermark_writer = PdfWriter()

  for page_num in range(watermark_reader.getNumPages()):
    page = watermark_reader.getPage(page_num)
    watermark_writer.addPage(page)

    # Calculate text placement based on page size and position
    page_width = page.mediaBox.getWidth()
    page_height = page.mediaBox.getHeight()
    text_x = page_width * text_position[0]
    text_y = page_height * text_position[1]

    # Create content dictionary with watermark text properties
    content = f"""q {font_size} 0 0 {font_size} {text_x} {text_y} cm /Tx BMC /Font /{font_family} {font_size} Tf {text_color[0]} {text_color[1]} {text_color[2]} rg ({watermark_text}) Tj EMC Q"""

    # Add watermark text as an overlay
    watermark_writer.addOverlay({'/Contents': content})

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

        # Allow user to customize font size, family, position, and color (optional)
        font_size_option = st.slider("Font Size", min_value=8, max_value=24, value=12)
        font_family_option = st.selectbox("Font Family", ["Helvetica", "Times-Roman", "Courier"])
        text_position_option = st.slider("Text Position (X, Y)", min_value=0.0, max_value=1.0, value=(0.5, 0.5), format="%f, %f")
        text_color_option = st.color_picker("Text Color", default_color=(0, 0, 0))

        watermark_pdf(input_pdf, watermark_text, output_filename,
                      font_size=font_size_option,
                      font_family=font_family_option,
                      text_position=text_position_option,
                      text_color=text_color_option)

        st.success(f"Watermark added! Download your watermarked PDF: {output_filename}")
        st.download_button("Download", data=open(output_filename, 'rb').read(), file_name=output_filename)

    else:
      with open(uploaded_file.name, 'rb') as input_pdf:
        output_filename = f"watermarked_{uploaded_file.name}"
        watermark_pdf(input_pdf, watermark_text, output_filename)
        st.success(f"Watermark added! Download your watermarked PDF: {output_filename}")
        st.download_button("Download", data=open(output_filename, 'rb').read(), file_name=output_filename)