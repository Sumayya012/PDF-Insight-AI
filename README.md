# 📄 PDF Insight AI

> An AI-powered PDF question-answering application built with Streamlit, LangChain, FAISS, local sentence-transformer embeddings, and Google Gemini.

[![Live Demo](https://img.shields.io/badge/LIVE%20DEMO-PDF%20INSIGHT%20AI-6366F1?style=for-the-badge)](https://pdfinsightapp.streamlit.app)
[![GitHub](https://img.shields.io/badge/-GITHUB-555555?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Sumayya012/PDF-Insight-AI)
[![Sumayya012](https://img.shields.io/badge/-SUMAYYA012-000000?style=for-the-badge)](https://github.com/Sumayya012)

---

## 🚀 Live Demo

Try the deployed application directly in your browser:

👉 https://pdfinsightapp.streamlit.app

No local installation is required to try the live application.

---

## 📌 Overview

**PDF Insight AI** is a Retrieval-Augmented Generation (RAG) application that allows users to upload one or more PDF documents and ask questions about their content.

Instead of sending the entire document directly to the language model, the application:

1. Extracts text from uploaded PDFs.
2. Splits the extracted text into smaller chunks.
3. Generates vector embeddings locally using `sentence-transformers/all-MiniLM-L6-v2`.
4. Stores the embeddings in a FAISS vector database.
5. Retrieves the most relevant document sections for a user's question.
6. Sends the retrieved context to Google Gemini.
7. Generates an answer based only on the retrieved PDF context.

---

## ✨ Key Features

- 📄 Upload multiple PDF files
- 🔎 Ask natural-language questions about uploaded documents
- 🧠 Retrieval-Augmented Generation (RAG)
- 🤖 Google Gemini-powered answer generation
- 🔢 Local semantic embeddings using Sentence Transformers
- ⚡ Fast similarity search using FAISS
- 🛡️ Context-restricted responses to reduce unsupported answers
- 💻 Simple Streamlit interface
- ☁️ Deployed on Streamlit Community Cloud
- 🔐 API key handled through environment variables / Streamlit Secrets

---

## 🏗️ Application Workflow

```text
             PDF Files
                 │
                 ▼
        ┌─────────────────┐
        │    PyPDF2       │
        │ Text Extraction │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Text Chunking   │
        │ 1500 / 200      │
        └────────┬────────┘
                 │
                 ▼
        ┌────────────────────────────┐
        │ Sentence Transformer       │
        │ all-MiniLM-L6-v2           │
        │ Local Embeddings           │
        └────────────┬───────────────┘
                     │
                     ▼
              ┌─────────────┐
              │    FAISS    │
              │ Vector Store│
              └──────┬──────┘
                     │
              User Question
                     │
                     ▼
          ┌─────────────────────┐
          │ Similarity Search   │
          │ Relevant PDF Chunks │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │    Google Gemini   │
          │   Answer Generation │
          └──────────┬──────────┘
                     │
                     ▼
                  Answer
```

---

## 🧠 RAG Pipeline

### 1. Document Loading

Uploaded PDF files are processed using **PyPDF2** and their text is extracted page by page.

### 2. Text Chunking

The extracted text is divided into smaller chunks using LangChain's `RecursiveCharacterTextSplitter`.

- **Chunk size:** 1500 characters
- **Chunk overlap:** 200 characters

### 3. Embedding Generation

Each text chunk is converted into a vector using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

The embedding model runs locally rather than using a paid embedding API.

### 4. Vector Storage

The generated embeddings are stored in a **FAISS** vector store for efficient similarity search.

### 5. Retrieval

When a question is submitted, the application searches the vector store and retrieves the most semantically relevant document chunks.

### 6. Answer Generation

The retrieved chunks are passed as context to **Google Gemini** through LangChain.

The prompt instructs the model to answer from the supplied context and return:

```text
answer is not available in the context
```

when the requested information is not present in the retrieved context.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| PyPDF2 | PDF text extraction |
| LangChain | RAG and LLM orchestration |
| FAISS | Vector similarity search |
| Sentence Transformers | Local text embeddings |
| Google Gemini | Answer generation |
| python-dotenv | Environment variable management |
| Git & GitHub | Version control and source code hosting |
| Streamlit Community Cloud | Deployment |

---

## 📂 Project Structure

```text
PDF-Insight-AI/
│
├── chatapp.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
└── img/
    ├── my_logo.png
    └── architecture.png
```

### Generated / Local Files

The following are intentionally not committed to GitHub:

```text
.env
venv/
__pycache__/
faiss_index/
.streamlit/secrets.toml
```

These are excluded through `.gitignore`.

---

## ⚙️ Requirements

- Python 3.x
- A Google Gemini API key
- Internet connection for Gemini API access
- Required Python packages listed in `requirements.txt`

### Python Environment

The application has been tested locally with:

```text
Python 3.14.3
```

The deployed Streamlit application uses:

```text
Python 3.12.14
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Do not commit `.env` to GitHub.

For Streamlit Community Cloud, configure the API key through the app's **Secrets** settings:

```toml
GOOGLE_API_KEY = "your_gemini_api_key"
```

Never expose your actual API key in source code or public repositories.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/Sumayya012/PDF-Insight-AI.git
cd PDF-Insight-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

Start the Streamlit application:

```bash
streamlit run chatapp.py
```

Then open the local Streamlit URL shown in the terminal.

---

## 📖 How to Use

1. Open the application.
2. Expand the sidebar.
3. Upload one or more PDF files.
4. Click **Submit & Process**.
5. Wait until processing is completed.
6. Enter a question in the question box.
7. The application retrieves relevant content from the uploaded PDFs.
8. Gemini generates an answer using the retrieved context.

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

Live application:

https://pdfinsightapp.streamlit.app

For deployment:

1. Push the project to GitHub.
2. Create a Streamlit Community Cloud application.
3. Select the GitHub repository.
4. Select `chatapp.py` as the main file.
5. Configure `GOOGLE_API_KEY` under Streamlit Secrets.
6. Deploy the application.

---

## 🔐 Privacy & API Usage

- PDF text is processed by the application to create chunks and embeddings.
- The embedding model `all-MiniLM-L6-v2` runs locally.
- Retrieved document context is sent to Google Gemini for answer generation.
- API credentials should be stored using environment variables locally and Streamlit Secrets in deployment.
- Users should avoid uploading confidential or sensitive documents unless they are comfortable with the application's processing and API usage.

---

## ⚠️ Limitations

- The application currently processes **PDF files** only.
- Text extraction depends on the PDF containing machine-readable text.
- Scanned/image-only PDFs may require OCR and are not automatically OCR-processed.
- Answer quality depends on extracted text, chunking, retrieval, and the language model.
- The FAISS vector store is generated from the currently processed documents.
- A Gemini API key is required for answer generation.
- The application is designed as a document question-answering system rather than a general-purpose chatbot.

---

## 🔮 Future Improvements

- Add OCR support for scanned PDFs.
- Add document-level source citations in answers.
- Improve conversation history and multi-turn questioning.
- Support additional document formats.
- Add persistent vector-store management.
- Add configurable retrieval parameters.
- Migrate to newer Google GenAI and LangChain integrations as the project evolves.

---

## 📸 Architecture

The project architecture diagram is available at:

```text
img/architecture.png
```

---

## 📜 License

This project is distributed under the license included in the `LICENSE` file.

---

## 👩‍💻 Author

**Mohammed Sumayya**

- GitHub: https://github.com/Sumayya012
- LinkedIn: https://www.linkedin.com/in/mohammed-sumayya/
