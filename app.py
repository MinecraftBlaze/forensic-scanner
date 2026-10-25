import streamlit as st

st.set_page_config(page_title="Forensic Fine-Print Scanner", layout="wide")

st.title("🔍 Corporate Disclosure Forensic Scanner")
st.subheader("Upload a filing (PDF/HTML) to extract hidden fine-print risks.")

# Upload file
uploaded_file = st.file_uploader("Upload 10-K, 10-Q, or Annual Report", type=["pdf", "html", "txt"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write(f"Analyzing: **{uploaded_file.name}**...")
    
    if st.button("Run Forensic Audit"):
        st.info("Extracting Notes to Financial Statements, Risk Factors, and Auditor Disclosures...")