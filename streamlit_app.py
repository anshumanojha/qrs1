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

        # Calculate the minimum size to fit the QR code without cutting off
        qr_size = qr.modules_count
        min_size = max(150, qr_size * 10)

        # Create a blank white image with the calculated size
        qr_img = Image.new("RGB", (min_size, min_size), "white")
        draw = ImageDraw.Draw(qr_img)

        # Calculate the position to center the QR code
        qr_code_img = qr.make_image(fill_color="black", back_color="white")
        position = ((min_size - qr_code_img.size[0]) // 2, (min_size - qr_code_img.size[1]) // 2)

        # Paste the QR code in the center
        qr_img.paste(qr_code_img, position)

        return qr_img

def generate_qr_code_contact_info(contact_info):
    if contact_info:
        # Generate a vCard string
        vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{contact_info['Name']}\nEMAIL:{contact_info['Email']}\nTEL:{contact_info['Phone']}\nORG:{contact_info['Current Designation']}\nEND:VCARD"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=2,
        )
        qr.add_data(vcard)
        qr.make(fit=True)

        # Calculate the minimum size to fit the QR code without cutting off
        qr_size = qr.modules_count
        min_size = max(150, qr_size * 10)

        # Create a blank white image with the calculated size
        qr_img = Image.new("RGB", (min_size, min_size), "white")
        draw = ImageDraw.Draw(qr_img)

        # Calculate the position to center the QR code
        qr_code_img = qr.make_image(fill_color="black", back_color="white")
        position = ((min_size - qr_code_img.size[0]) // 2, (min_size - qr_code_img.size[1]) // 2)

        # Paste the QR code in the center
        qr_img.paste(qr_code_img, position)

        return qr_img

def main():
    st.title("QR Code Generator")

    # Box for generating QR code for a URL
    st.header("Generate QR Code for a Desired URL")
    user_url = st.text_input("Enter the URL:")

    if user_url:
        qr_img_url = generate_qr_code_url(user_url)
        st.image(qr_img_url, caption="QR Code for URL", use_column_width=False)
        img_bytes_url = io.BytesIO()
        qr_img_url.save(img_bytes_url, format="PNG")
        st.download_button(
            label="Download QR Code (URL)",
            data=img_bytes_url.getvalue(),
            file_name="qr_code_url.png",
            mime="image/png",
        )

    # Box for generating QR code for personal information
    st.header("Generate QR Code for Contact Information")
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    phone = st.text_input("Phone:")
    designation = st.text_input("Current Designation:")

    if st.button("Generate QR Code (Contact Info)") and (name or email or phone or designation):
        contact_info = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Current Designation": designation,
        }
        qr_img_contact_info = generate_qr_code_contact_info(contact_info)
        st.image(qr_img_contact_info, caption="QR Code with Contact Info", use_column_width=False)
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
