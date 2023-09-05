import streamlit as st
import qrcode
from PIL import Image

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
        
        # Convert the PIL Image to bytes
        img_byte_array = io.BytesIO()
        qr_img.save(img_byte_array, format="PNG")
        return img_byte_array.getvalue()

def main():
    st.title("QR Code Generator")

    user_url = st.text_input("Enter the URL:")
    
    if user_url:
        qr_img_data = generate_qr_code(user_url)
        st.image(qr_img_data, caption="QR Code", use_column_width=True, format="PNG")

if __name__ == "__main__":
    main()
