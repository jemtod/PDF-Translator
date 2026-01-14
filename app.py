import streamlit as st
from translator_utils import extract_text_from_pdf, translate_content, create_docx

st.set_page_config(page_title="PDF Translator (EN <-> ID)", layout="wide")

st.title("📄 PDF Translator Utility")
st.markdown("Translate PDF documents between English and Indonesian with layout structure preservation.")

# Sidebar for controls
with st.sidebar:
    st.header("Settings")
    
    # Language Selection
    direction = st.radio(
        "Translation Direction",
        ("English -> Indonesian", "Indonesian -> English", "Auto -> Indonesian", "Auto -> English")
    )
    
    source_lang = "auto"
    target_lang = "id"
    
    if direction == "English -> Indonesian":
        source_lang = "en"
        target_lang = "id"
    elif direction == "Indonesian -> English":
        source_lang = "id"
        target_lang = "en"
    elif direction == "Auto -> Indonesian":
        source_lang = "auto"
        target_lang = "id"
    elif direction == "Auto -> English":
        source_lang = "auto"
        target_lang = "en"

# File Uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # 1. Extract Text
    with st.spinner("Extracting text and analyzing structure..."):
        content_blocks = extract_text_from_pdf(uploaded_file)
        
    # Check if text was extracted
    if not content_blocks:
        st.error("Could not extract text from this PDF. It might be a scanned image.")
    else:
        # Show extraction metrics
        st.success(f"Analysis complete! Found {len(content_blocks)} text blocks/lines.")
        
        # Display Preview (Just raw text for quick check)
        raw_preview = "\n".join([b['text'] for b in content_blocks])
        with st.expander("View Extracted Text Preview", expanded=False):
            st.text_area("Preview", raw_preview, height=200)

        # 2. Translate
        if st.button("Translate Document"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            with st.spinner("Translating... Processing text in batches to speed up..."):
                # We could implement a callback in utils for progress, but for now just spinner
                translated_blocks = translate_content(content_blocks, source_lang, target_lang)
            
            progress_bar.progress(100)
            st.success("Translation Complete!")
            
            # Display Translated Preview
            st.subheader("Translation Preview")
            translated_preview = "\n".join([b['text'] for b in translated_blocks])
            st.text_area("Preview", translated_preview, height=300)
            
            # 3. Download Options
            st.subheader("Download Structured Results")
            cols = st.columns(2)
            
            # Download as TXT (Flat)
            with cols[0]:
                st.download_button(
                    label="Download as .txt",
                    data=translated_preview,
                    file_name="translated.txt",
                    mime="text/plain"
                )
                
            # Download as DOCX (Structured)
            with cols[1]:
                docx_file = create_docx(translated_blocks)
                st.download_button(
                    label="Download as .docx (Formatted)",
                    data=docx_file,
                    file_name="translated_structured.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
