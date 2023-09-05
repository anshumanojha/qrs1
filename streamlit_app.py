import streamlit as st
import qrcode
from PIL import Image, ImageDraw

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
        
        # Create a blank white image to place the QR code on
        qr_img = Image.new("RGB", (300, 300), "white")
        draw = ImageDraw.Draw(qr_img)
        
        # Convert the QR code matrix to a Pillow Image
        qr_img.paste(qr.make_image(fill_color="black", back_color="white"))
        
        return qr_img

def main():
    st.title("QR Code Generator")

    user_url = st.text_input("Enter the URL:")
    
    if user_url:
        qr_img = generate_qr_code(user_url)
        st.image(qr_img, caption="QR Code", use_column_width=True, format="JPEG")

if __name__ == "__main__":
    main()
