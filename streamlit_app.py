import streamlit as st
import qrcode
from PIL import Image, ImageDraw
import io
import webbrowser  # Added for opening WhatsApp link
import phonenumbers

# Unchanged function
def generate_qr_code_url(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_size = qr.modules_count
    min_size = max(150, qr_size * 10)

    qr_img = Image.new("RGB", (min_size, min_size), "white")
    qr_code_img = qr.make_image(fill_color="black", back_color="white")
    position = ((min_size - qr_code_img.size[0]) // 2, (min_size - qr_code_img.size[1]) // 2)
    qr_img.paste(qr_code_img, position)

    return qr_img

# Unchanged function
def generate_qr_code_contact_info(contact_info):
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{contact_info['Name']}\nEMAIL:{contact_info['Email']}\nTEL:{contact_info['Phone']}\nORG:{contact_info['Current Designation']}\nEND:VCARD"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=2,
    )
    qr.add_data(vcard)
    qr.make(fit=True)

    qr_size = qr.modules_count
    min_size = max(150, qr_size * 10)

    qr_img = Image.new("RGB", (min_size, min_size), "white")
    qr_code_img = qr.make_image(fill_color="black", back_color="white")
    position = ((min_size - qr_code_img.size[0]) // 2, (min_size - qr_code_img.size[1]) // 2)
    qr_img.paste(qr_code_img, position)

    return qr_img

# Unchanged function
def generate_whatsapp_link(phone_number, message):
    try:
        parsed_number = phonenumbers.parse(phone_number, "US")  # Change the region code as needed
        if phonenumbers.is_valid_number(parsed_number):
            phone_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
            return f"https://wa.me/{phone_number}?text={message}"
    except phonenumbers.NumberFormatException:
        pass
    return None

def main():
    st.title("QR Code Generator")

    # ... (unchanged)

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

    st.header("Send WhatsApp Message")
    whatsapp_phone_number = st.text_input("Enter WhatsApp Phone Number (with country code, e.g., +123456789):")
    whatsapp_message = st.text_input("Enter WhatsApp Message:")

    if st.button("Generate WhatsApp Message") and (whatsapp_phone_number and whatsapp_message):
        whatsapp_link = generate_whatsapp_link(whatsapp_phone_number, whatsapp_message)
        if whatsapp_link:
            st.markdown(f"Click [here]({whatsapp_link}) to open WhatsApp and send the message.")
        else:
            st.warning("Invalid phone number. Please enter a valid WhatsApp phone number.")

if __name__ == "__main__":
    main()
