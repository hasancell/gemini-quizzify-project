# Task 5 of Gemini Quizzify

import streamlit as st
import os
import sys
import asyncio
import tempfile
import shutil
import time
import gc
import chromadb

sys.path.append(os.path.abspath('../../'))

# Ensure to set the path to your Google service account JSON key
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\project\\.venv\\gemini_project\\your-project-key.json"

from gemini_project.document_processor import DocumentProcessor
from gemini_project.embedding_documents import EmbeddingClient

from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader

st.cache_data.clear()

class ChromaCollectionCreator:
    def __init__(self, processor, embed_model):
        self.processor = processor
        self.embed_model = embed_model
        self.db = None
        self.temp_dir = None  # Store the temporary directory

    def create_chroma_collection(self):
        if len(self.processor.pages) == 0:
            st.error("No documents found!", icon="🚨")
            return

        text_splitter = CharacterTextSplitter(
            separator="\n\n",
            chunk_size=500,
            chunk_overlap=100,
            length_function=len,
            is_separator_regex=False,
        )

        aux_array = list(map(lambda page: page.page_content, self.processor.pages))
        texts = text_splitter.create_documents(aux_array)

        if texts:
            st.success(f"Successfully split pages to {len(texts)} documents!", icon="✅")

        # Create a temporary directory
        self.temp_dir = tempfile.TemporaryDirectory()
        persist_dir = self.temp_dir.name

        # Create the Chroma collection with the temporary directory
        self.db = Chroma.from_documents(texts, self.embed_model.client, persist_directory=persist_dir)

        if self.db:
            st.success("Successfully created Chroma Collection!", icon="✅")
        else:
            st.error("Failed to create Chroma Collection!", icon="🚨")

    def query_chroma_collection(self, query) -> Document:
        """
        Queries the created Chroma collection for documents similar to the query.
        :param query: The query string to search for in the Chroma collection.
        
        Returns the first matching document from the collection with similarity score.
        """
        if self.db:
            docs = self.db.similarity_search_with_relevance_scores(query)
            if docs:
                return docs[0]
            else:
                st.error("No matching documents found!", icon="🚨")
        else:
            st.error("Chroma Collection has not been created!", icon="🚨")
    
    def as_retriever(self):
        return self.db.as_retriever()



# Main script to run Chroma collection creation
if __name__ == "__main__":
    processor = DocumentProcessor()
    processor.ingest_documents()

    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "gemini-quizzify-1",
        "location": "europe-west2"
    }

    embed_client = EmbeddingClient(**embed_config)

    chroma_creator = ChromaCollectionCreator(processor, embed_client)

    with st.form("Load Data to Chroma"):
        st.write("Select PDFs for Ingestion, then click Submit")

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Creating Chroma collection... This may take a few moments.")
            # Call the create_chroma_collection method
            chroma_creator.create_chroma_collection()
