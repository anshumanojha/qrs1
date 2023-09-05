import streamlit as st
import qrcode
from PIL import Image
import io

def generate_qr_code(url):
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Convert the QR code image to bytes
        qr_byte_io = io.BytesIO()
        qr_img.save(qr_byte_io, format="PNG")
        qr_byte_io.seek(0)

        return Image.open(qr_byte_io)

def main():
    st.title("QR Code Generator")

    user_url = st.text_input("Enter the URL:")
    
    if user_url:
        qr_img = generate_qr_code(user_url)
        st.image(qr_img, caption="QR Code", use_column_width=True)

if __name__ == "__main__":
    main()
