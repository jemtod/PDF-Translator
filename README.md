# PDF Translator Tool

A simple Python-based tool to translate PDF documents between English and Indonesian using Streamlit and Google Translate.

## Features
- **PDF Text Extraction**: Extracts text from uploaded PDF files.
- **Translation**: Translates text between English and Indonesian (supports Auto-detection).
- **Export**: Download translated text as `.txt` or `.docx`.
- **User Interface**: Clean and easy-to-use web interface built with Streamlit.

## Installation

1.  Clone the repository or download the files.
2.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    *Note: This usually requires Python 3.8 or higher.*

## Usage

1.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2.  The application will open in your default web browser (usually at `http://localhost:8501`).
3.  Upload a PDF file.
4.  Select the translation direction (e.g., English -> Indonesian).
5.  Click "Translate Text".
6.  Download the result.

## Limitations
- **Layout**: The tool extracts text and translates it. It does *not* preserve the original PDF layout, images, or formatting perfectly. It reconstructs the text into a new document.
- **Scanned PDFs**: It may not work well with scanned PDFs (images containing text) unless OCR is added (not included in this version).
- **Rate Limits**: Uses a free translation library which may have rate limits for very large documents.
