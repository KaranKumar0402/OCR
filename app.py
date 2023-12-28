import streamlit as st
from streamlit_cropperjs import st_cropperjs
import imageio.v3 as iio
import easyocr
import cv2

@st.cache_resource(show_spinner=True)
def loading_model(langlist):
    rdr = easyocr.Reader(langlist,gpu = True)
    return (rdr)

reader = load_model(['en'])
st.header('Image to Text Converter 🔠')
img = st.file_uploader('Upoad Image Here!!', type=['png', 'jpg', 'jpeg'], key='uploaded_pic')
if img:
    img = img.read()
    cropped_pic = st_cropperjs(pic=img, btn_text="Submit!", key="foo")
    if cropped_pic:
        cropped_pic = iio.imread(cropped_pic)
        cropped_pic = cv2.convertScaleAbs(cropped_pic, alpha = 0.8, beta = -25)
        st.image(cropped_pic)

if st.button('Show Output'):
    result = reader.readtext(cropped_pic, detail=0, paragraph=True)
    st.success(result)
