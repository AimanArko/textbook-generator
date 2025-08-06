import streamlit as st
import zipfile
import os

st.set_page_config(page_title="GEMMA Textbook Generator", layout="wide")

st.title("📚 GEMMA Textbook Generator")
st.markdown("Generate structured textbooks from syllabus inputs using AI-powered pipelines.")

# Upload ZIP file
uploaded_file = st.file_uploader("Upload your syllabus ZIP file", type="zip")

if uploaded_file:
    with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
        zip_ref.extractall("uploaded_syllabus")
    st.success("✅ Syllabus extracted successfully!")

    # Placeholder for pipeline trigger
    st.markdown("### 🔄 Run Textbook Generation")
    if st.button("Generate Textbook"):
        st.info("Running pipeline... (mocked for demo)")
        # Replace with actual pipeline call
        st.success("🎉 Textbook generated! Check the output folder.")

# Footer
st.markdown("---")
st.caption("Built by AimanArko • Powered by GEMMA + Ollama + OCR + Modular Pipelines")
