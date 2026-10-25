import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="Forensic Fine-Print Scanner", layout="wide")

st.title("🔍 Corporate Disclosure Forensic Scanner")
st.subheader("Upload a filing (PDF/HTML) to extract hidden fine-print risks.")

uploaded_file = st.file_uploader("Upload 10-K, 10-Q, or Annual Report", type=["pdf", "html", "txt"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    
    # Extract text if it's a PDF
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        st.write(f"Extracted **{len(text):,}** characters from **{uploaded_file.name}**.")
    else:
        text = uploaded_file.read().decode("utf-8", errors="ignore")
        st.write(f"Loaded **{len(text):,}** characters from **{uploaded_file.name}**.")
    
    if st.button("Run Forensic Audit"):
        st.info("Parsing financial statements and risk factors...")
        # Placeholder for AI analysis