import streamlit as st
import qrcode
from PIL import Image, ImageDraw
import io

def generate_qr_code_url(url):
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
        qr_img = Image.new("RGB", (50, 50), "white")
        draw = ImageDraw.Draw(qr_img)
        
        # Convert the QR code matrix to a Pillow Image
        qr_img.paste(qr.make_image(fill_color="black", back_color="white"))
        
        return qr_img

def generate_qr_code_contact_info(contact_details, additional_info):
    if contact_details or additional_info:
        qr_data = f"Contact Details: {contact_details}\nAdditional Info: {additional_info}"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=2,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        # Create a blank white image to place the QR code on
        qr_img = Image.new("RGB", (50, 50), "white")
        draw = ImageDraw.Draw(qr_img)
        
        # Convert the QR code matrix to a Pillow Image
        qr_img.paste(qr.make_image(fill_color="black", back_color="white"))
        
        return qr_img

def main():
    st.title("QR Code Generator")

    user_url = st.text_input("Enter the URL:")
    contact_details = st.text_input("Enter Contact Details:")
    additional_info = st.text_input("Enter Additional Information:")
    
    if user_url:
        qr_img_url = generate_qr_code_url(user_url)
        st.image(qr_img_url, caption="QR Code for URL", use_column_width=True)
        img_bytes_url = io.BytesIO()
        qr_img_url.save(img_bytes_url, format="PNG")
        st.download_button(
            label="Download QR Code (URL)",
            data=img_bytes_url.getvalue(),
            file_name="qr_code_url.png",
            mime="image/png",
        )
    
    if contact_details or additional_info:
        qr_img_contact_info = generate_qr_code_contact_info(contact_details, additional_info)
        st.image(qr_img_contact_info, caption="QR Code with Contact Info", use_column_width=True)
        img_bytes_contact_info = io.BytesIO()
        qr_img_contact_info.save(img_bytes_contact_info, format="PNG")
        st.download_button(
            label="Download QR Code (Contact Info)",
            data=img_bytes_contact_info.getvalue(),
            file_name="qr_code_contact_info.png",
            mime="image/png",
        )

if __name__ == "__main__":
    main()
