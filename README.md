# 📄 PDF Summarizer & Chatbot

## 🚀 Overview
This is a **PDF-based AI chatbot** that extracts text, tables, and images (via OCR) from a PDF and allows users to ask questions about the document. It uses **Retrieval-Augmented Generation (RAG)** powered by **ChromaDB** and **LLaMA 3.1** to provide accurate answers.

## 🔥 Features
- 📂 Upload a PDF file
- 🔍 Extract text, tables, and OCR-based content
- 🧠 Store text embeddings in **ChromaDB**
- 🤖 Answer user questions using **LLaMA 3.1**
- ⚡ Fast retrieval using **vector embeddings**
- 🎯 Supports **multi-page PDFs**

## 🛠️ Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

## 🚀 Usage

### Run the Streamlit App
```sh
streamlit run app.py
```

### Upload a PDF and Ask Questions!
- The app will **extract text** from the uploaded PDF.
- You can **type any question**, and the chatbot will provide answers based on the document.

## 🏗️ Project Structure
```
📂 pdf-chatbot
│── app.py                # Main Streamlit app
│── extract.py            # PDF text & OCR extraction logic
│── rag.py                # ChromaDB vector storage & retrieval
│── requirements.txt      # Python dependencies
│── README.md             # Documentation
│── .gitignore            # Files to ignore in Git
└── chroma_db/            # Persistent ChromaDB storage
```

## 🛠️ Technologies Used
- **Streamlit** → Interactive UI
- **pdfplumber** → Extract text & tables
- **pytesseract** → OCR for images
- **pdf2image** → Convert PDFs to images
- **ChromaDB** → Vector store for retrieval
- **Ollama (LLaMA 3.1)** → LLM for answering questions

## 🔍 Example Question
```sh
Q: What is the main topic of this PDF?
A: The document discusses [extracted summary].
```

