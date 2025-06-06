import streamlit as st
import asyncio
import os
from brand_extractor import BrandExtractor

st.set_page_config(page_title="Brand Extractor", layout="centered")
st.title("🌐 Brand Style Guide Extractor")
st.write("Enter a website URL to analyze and download a PDF branding report with colors, fonts, and logos.")

url = st.text_input("Website URL", placeholder="https://www.example.com")

if st.button("Generate Report") and url:
    with st.spinner("Analyzing website. This may take a moment..."):
        async def run_extractor():
            extractor = BrandExtractor(url, output_dir='reports', auto_open=False)
            result = await extractor.extract_branding()
            return result['pdf'] if result else None

        pdf_path = asyncio.run(run_extractor())

        if pdf_path and os.path.exists(pdf_path):
            st.success("✅ Report generated successfully!")
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📄 Download PDF Report",
                    data=f,
                    file_name=os.path.basename(pdf_path),
                    mime="application/pdf"
                )
        else:
            st.error("❌ Failed to generate the report. Try another URL.")
