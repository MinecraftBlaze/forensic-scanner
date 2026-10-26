import streamlit as st
from pypdf import PdfReader
from google import genai

st.set_page_config(page_title="Forensic Fine-Print Scanner", layout="wide")

st.title("🔍 Corporate Disclosure Forensic Scanner")
st.subheader("Upload a filing (PDF/HTML) to extract hidden fine-print risks.")

# Initialize Gemini client using Streamlit secrets
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    client = None

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
        if not client:
            st.error("Gemini API key is missing or invalid. Check your .streamlit/secrets.toml file.")
        else:
            with st.spinner("Analyzing fine-print, footnotes, and hidden liabilities..."):
                # Truncate text if it's too massive for a single quick pass, or send a focused prompt
                prompt = (
                    "You are a forensic financial analyst. Analyze the following corporate disclosure text. "
                    "Identify and list: 1) Hidden liabilities or off-balance-sheet arrangements, "
                    "2) Aggressive accounting or revenue recognition flags, "
                    "3) Critical risk factors or footnotes that normal investors might miss.\n\n"
                    f"Document text snippet:\n{text[:30000]}"
                )
                
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt,
                    )
                    st.subheader("🚨 Forensic Audit Findings")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error during AI analysis: {e}")