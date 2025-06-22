import streamlit as st 
import qrcode as qr 
from PIL import Image
import io 

st.title("my QR ")
data = st.text_input(" put the url ")


if st.button("build") :
    if data :
        img = qr.make(data)
        buf=io.BytesIO()
        img.save(buf,format="PNG")
        buf.seek(0)

        st.image(buf ,caption="QR code" , use_column_width=True )
    else:
        st.warning("please put the URL first")