# TASK 3 of Gemini Quizzify

# Necessary imports
import streamlit as st
from langchain.document_loaders import PyPDFLoader
import os
import tempfile
import uuid

# Ensure to set the path to your Google service account JSON key
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\project\\.venv\\gemini_project\\your-project-key.json"

class DocumentProcessor:
    """
    This class encapsulates the functionality for processing uploaded PDF documents using Streamlit
    and Langchain's PyPDFLoader. It provides a method to render a file uploader widget, process the
    uploaded PDF files, extract their pages, and display the total number of pages extracted.
    """
    def __init__(self):
        self.pages = []  # List to keep track of pages from all documents
    
    def ingest_documents(self):
        """
        Renders a file uploader in a Streamlit app, processes uploaded PDF files,
        extracts their pages, and updates the self.pages list with the total number of pages.
        """
        
        # Step 1: Render a file uploader widget. Replace 'None' with the Streamlit file uploader code.
        uploaded_files = st.file_uploader("Upload a PDF file", type=["pdf"], accept_multiple_files=True)
        
        if uploaded_files is not None:
            for uploaded_file in uploaded_files:
                # Generate a unique identifier to append to the file's original name
                unique_id = uuid.uuid4().hex
                original_name, file_extension = os.path.splitext(uploaded_file.name)
                temp_file_name = f"{original_name}_{unique_id}{file_extension}"
                temp_file_path = os.path.join(tempfile.gettempdir(), temp_file_name)

                # Write the uploaded PDF to a temporary file
                with open(temp_file_path, 'wb') as f:
                    f.write(uploaded_file.getvalue())

                # Step 2: Process the temporary file
                loader = PyPDFLoader(temp_file_path)
                pages = loader.load()
                
                # Add the extracted pages to the 'pages' list.
                self.pages.extend(pages)
                
                # Clean up by deleting the temporary file.
                os.unlink(temp_file_path)
            
            # Display the total number of pages processed.
            st.write(f"Total pages processed: {len(self.pages)}")
        
if __name__ == "__main__":
    processor = DocumentProcessor()
    processor.ingest_documents()
