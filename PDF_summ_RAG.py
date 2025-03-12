import streamlit as st
import pdfplumber
import pytesseract
from pdf2image import convert_from_bytes
from langchain.chains import RetrievalQA
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.schema import Document
import os
import io
import chromadb
from chromadb.config import Settings  # ✅ Proper ChromaDB settings

# Persistent ChromaDB directory
CHROMA_DB_DIR = "./chroma_db"
COLLECTION_NAME = "pdf_context"  # ✅ Ensures unique context per document

def extract_text_from_pdf(pdf_bytes):
    """Extracts text, tables, and images from a PDF."""
    text = ""
    pdf_stream = io.BytesIO(pdf_bytes)

    with pdfplumber.open(pdf_stream) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    text += " ".join(str(cell) if cell is not None else "" for cell in row) + "\n"

    # ✅ OCR for images
    images = convert_from_bytes(pdf_bytes)
    for img in images:
        text += pytesseract.image_to_string(img)

    return text.strip()

def create_rag_chain(documents):
    """Creates the RAG chain using ChromaDB and LLaMA 3.2"""

    # ✅ Initialize ChromaDB with PersistentClient
    chroma_client = chromadb.PersistentClient(
        path=CHROMA_DB_DIR, 
        settings=Settings(anonymized_telemetry=False)  # ✅ Explicit settings
    )

    # ✅ Delete old collection to clear previous context
    try:
        chroma_client.delete_collection(COLLECTION_NAME)
    except Exception as e:
        print("⚠️ No previous collection found or error deleting:", e)

    # ✅ Create a fresh Chroma vector store
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=OllamaEmbeddings(model="llama3.1"),  # ✅ Latest LLaMA 3.1
        persist_directory=CHROMA_DB_DIR,
        client=chroma_client
    )

    retriever = vector_store.as_retriever()
    llm = Ollama(model="llama3.1")

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

def main():
    st.title("📄 PDF Summarizer and Chatbot")

    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    if uploaded_file:
        pdf_bytes = uploaded_file.read()  # ✅ Read file as bytes

        text = extract_text_from_pdf(pdf_bytes)

        if text:
            documents = [Document(page_content=text)]
            qa_chain = create_rag_chain(documents)  # ✅ Clears old context before processing

            st.success("✅ PDF content loaded successfully. Ask me anything!")

            user_question = st.text_input("Ask a question about the PDF:")
            if user_question:
                answer = qa_chain.run(user_question)
                st.write("**Answer:**", answer)
        else:
            st.error("❌ No readable text was extracted. Try another file.")

if __name__ == "__main__":
    main()
