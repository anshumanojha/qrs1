import streamlit as st
import qrcode
from PIL import Image, ImageDraw
import io

# Unchanged functions for QR code generation

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

def generate_experience_summary(company, role, summary):
    experience_summary = f"Company: {company}\nRole: {role}\nSummary: {summary}"
    return experience_summary

def main():
    st.title("Andrew's Portfolio")

    st.header("Portfolio Details")
    full_name = st.text_input("Full Name:")
    email = st.text_input("Email:")
    phone = st.text_input("Phone:")
    linkedin_profile = st.text_input("LinkedIn Profile:")

    st.header("Generate QR Code for LinkedIn Profile")
    if linkedin_profile:
        qr_img_linkedin = generate_qr_code_url(linkedin_profile)
        st.image(qr_img_linkedin, caption="QR Code for LinkedIn Profile", use_column_width=False)
        img_bytes_linkedin = io.BytesIO()
        qr_img_linkedin.save(img_bytes_linkedin, format="PNG")
        st.download_button(
            label="Download QR Code (LinkedIn)",
            data=img_bytes_linkedin.getvalue(),
            file_name="qr_code_linkedin.png",
            mime="image/png",
        )

    st.header("Experience Summary")
    company = st.text_input("Company:")
    role = st.text_input("Role:")
    summary = st.text_area("Summary:")
    
    if st.button("Generate Experience Summary") and (company or role or summary):
        experience_summary = generate_experience_summary(company, role, summary)
        st.text(experience_summary)

    st.header("Skills and Projects")
    skills = st.text_area("Skills:")
    projects = st.text_area("Related Projects:")

    if st.button("Save Skills and Projects") and (skills or projects):
        # You can save or display the skills and projects as needed
        st.text(f"Skills: {skills}")
        st.text(f"Related Projects: {projects}")

if __name__ == "__main__":
    main()
