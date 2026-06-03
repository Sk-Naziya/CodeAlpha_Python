import streamlit as st
import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

st.set_page_config(
    page_title="Automation Hub",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Automation Hub")
st.markdown("### CodeAlpha Task Automation Project")

tab1, tab2, tab3 = st.tabs(
    [
        "📂 JPG Organizer",
        "📧 Email Extractor",
        "🌐 Website Title Scraper"
    ]
)

# =====================================================
# TAB 1
# =====================================================

with tab1:

    st.subheader("📂 JPG File Organizer")

    uploaded_files = st.file_uploader(
        "Upload JPG Files",
        type=["jpg", "jpeg"],
        accept_multiple_files=True
    )

    if st.button("Organize JPG Files"):

        os.makedirs(
            "organized_files",
            exist_ok=True
        )

        count = 0

        for file in uploaded_files:

            temp_path = file.name

            with open(temp_path, "wb") as f:
                f.write(file.getbuffer())

            shutil.move(
                temp_path,
                os.path.join(
                    "organized_files",
                    file.name
                )
            )

            count += 1

        st.success(
            f"{count} JPG files organized successfully."
        )

# =====================================================
# TAB 2
# =====================================================

with tab2:

    st.subheader("📧 Email Extractor")

    text = st.text_area(
        "Paste text containing emails"
    )

    if st.button("Extract Emails"):

        emails = re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            text
        )

        if emails:

            os.makedirs(
                "outputs",
                exist_ok=True
            )

            with open(
                "outputs/emails.txt",
                "w"
            ) as f:

                for email in emails:
                    f.write(email + "\n")

            st.success(
                f"Found {len(emails)} emails"
            )

            st.write(emails)

            with open(
                "outputs/emails.txt",
                "rb"
            ) as f:

                st.download_button(
                    "📥 Download Emails",
                    f,
                    file_name="emails.txt"
                )

        else:

            st.warning(
                "No emails found"
            )

# =====================================================
# TAB 3
# =====================================================

with tab3:

    st.subheader(
        "🌐 Website Title Scraper"
    )

    url = st.text_input(
        "Enter Website URL"
    )

    if st.button("Get Website Title"):

        try:

            response = requests.get(url)

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            title = soup.title.string

            os.makedirs(
                "outputs",
                exist_ok=True
            )

            with open(
                "outputs/webpage_title.txt",
                "w"
            ) as f:

                f.write(title)

            st.success(
                "Title Extracted Successfully"
            )

            st.write(
                f"### {title}"
            )

            with open(
                "outputs/webpage_title.txt",
                "rb"
            ) as f:

                st.download_button(
                    "📥 Download Title",
                    f,
                    file_name="webpage_title.txt"
                )

        except Exception as e:

            st.error(str(e))