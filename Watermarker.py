#WaterMarker v0.1, watermark your PDFs in a click beat!

import streamlit as st

st.set_page_config(layout="wide")
st.title('**WaterMarker** *Personalise your PDFs*')

with st.expander('About This App'):
    st.write('Use WaterMarker to put personalised water marks on your PDFs to personalise them before distribution;\n'
             '1. Drag and Drop your original PDF file in the box below.\n'
             '2. Enter the text you\'d like at the top, middle and bottom of your document.\n'
             '3. Check the text is exactly what you want!\n'
             '4. Press the button and the file will get saved to your computer.'
             )
    st.write('Email me at sean@positivepython.co.uk with any feedback, or raise an issue on GitHub https://github.com/PositivePython42/WaterMarket/issues')


st.header('Upload your data here')
st.subheader('Please make sure the file is a PDF.')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    #put the code to ask for the text here
    
    #then a watermark now button to do the work!


