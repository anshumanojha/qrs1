import streamlit as st
import qrcode
from PIL import Image, ImageDraw
import io

def generate_qr_code(url):
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create a smaller blank white image to place the QR code on
        qr_img = Image.new("RGB", (150, 150), "white")
        draw = ImageDraw.Draw(qr_img)
        
        # Convert the QR code matrix to a Pillow Image
        qr_img.paste(qr.make_image(fill_color="black", back_color="white"))
        
        return qr_img

def main():
    st.title("QR Code Generator")

    user_url = st.text_input("Enter the URL:")
    
    if user_url:
        qr_img = generate_qr_code(user_url)
        
        # Display the QR code image
        st.image(qr_img, caption="QR Code", use_column_width=True)
        
        # Create a download button for the image
        img_bytes = io.BytesIO()
        qr_img.save(img_bytes, format="PNG")
        st.download_button(
            label="Download QR Code",
            data=img_bytes.getvalue(),
            file_name="qr_code.png",
            mime="image/png",
        )

if __name__ == "__main__":
    main()
