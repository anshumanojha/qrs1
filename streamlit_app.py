import streamlit as st
import qrcode
from PIL import Image, ImageDraw
import io

def generate_qr_code(contact_details):
    if contact_details:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=2,
        )
        qr.add_data(contact_details)
        qr.make(fit=True)
        
        # Create a smaller blank white image to place the QR code on
        qr_img = Image.new("RGB", (150, 150), "white")
        draw = ImageDraw.Draw(qr_img)
        
        # Convert the QR code matrix to a Pillow Image
        qr_img.paste(qr.make_image(fill_color="black", back_color="white"))
        
        return qr_img

def main():
    st.title("QR Code Generator")

    # Box for entering personal information
    st.header("Enter Personal Information")
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    phone = st.text_input("Phone:")
    designation = st.text_input("Current Designation:")
    
    if st.button("Generate QR Code") and (name or email or phone or designation):
        contact_info = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Current Designation": designation,
        }
        contact_details = "\n".join(f"{key}: {value}" for key, value in contact_info.items() if value)
        
        if contact_details:
            qr_img_contact_info = generate_qr_code(contact_details)
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
