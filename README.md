# DocuDroid: RAG-based PDF Analyzer & Semantic Q&A Chatbot

---

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)  
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red?logo=streamlit)  
![OpenAI GPT-4](https://img.shields.io/badge/OpenAI-GPT--4-blue?logo=openai)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-green)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

I developed DOCUDROID, a **Retrieval-Augmented Generation (RAG) based PDF analyzer** that can read and understand large PDF documents even 50+ pages and answer questions from them in real time. The main goal was to make document analysis fast, accurate, and affordable using AI.

---

### Images

<img width="900" alt="DocuDroid Screenshot 1" src="./assets/DocuDroid 1.png">
<br>

<img width="900" alt="DocuDroid Screenshot 2" src="./assets/DocuDroid 2.png">
<br>

## <img width="900" alt="DocuDroid Screenshot 3" src="./assets/DocuDroid 3.png">

## About The Project

DocuDroid solves the problem of quickly understanding complex PDF documents. Users can upload PDFs and the system will:

- Generate multiple types of summaries
- Answer questions in a conversational manner

Each chunk is then converted into a vector embedding which is a numerical representation of its meaning and stored in ChromaDB, which allows semantic search. Semantic search means the system finds content by meaning, not just keywords.

When the user asks a question, the query is also converted into an embedding. ChromaDB compares it with stored chunks and retrieves only the most relevant ones. Those chunks are then passed to GPT-4o-mini, which generates an accurate and context-aware answer or a short summary. This whole process is known as Retrieval Augmented Generation (RAG). This combined process of retrieval using semantic search and generation of answer using OpenAI forms the RAG pipeline.

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend & AI**:
  - LangChain for LLM orchestration
  - OpenAI GPT models for semantic understanding
  - ChromaDB for vector storage and semantic search
  - PyPDF for PDF text extraction
- **Data Processing**: pandas
- **Language**: Python
- **Environment Management**: python-dotenv

---

## Key Features

- **RAG-based Summarization**:

  - **Concise Summary**: Quick overview
  - **Section-wise Summary**: Detailed breakdown
  - **Key Bullet Points**: Critical insights

- **Semantic Q&A**: Ask questions and get context-aware answers

- **Downloadable Output**: Export summaries or answers as .txt files

- **Modern UI**: Streamlit-powered, responsive, and user-friendly

- **Privacy-focused**: Documents are processed locally in-memory

---

## Setup & Installation

### 1. Clone the repository:

```sh
git clone https://github.com/yourusername/DocuDroid.git
cd DocuDroid
```

### 2. Create and activate a virtual environment:

```sh

python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:

```sh

pip install --upgrade langchain langchain-community langchain-openai chromadb
pip install --upgrade pypdf pandas streamlit python-dotenv tiktoken
```

### 4. Set up environment variables:

Create a .env file in the root directory:

```sh
OPENAI_API_KEY="YOUR_OPENAI_API_KEY_HERE"
```

5. Run the Streamlit app:

```sh
streamlit run app.py
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

### Acknowledgements

- Thanks to **Streamlit** for easy Python web apps
- Thanks to **OpenAI** for LLM APIs
- Thanks to **ChromaDB** for semantic search
