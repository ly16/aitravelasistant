# AI-Powered Travel Assistant

An AI-powered travel assistant that allows users to upload travel-related PDFs (itineraries, booking confirmations, guides, etc.) and ask natural-language questions based on the document content. The system performs semantic search over the uploaded document and uses a large language model to generate accurate, contextual answers.

---

## ✨ Features

* Upload travel-related PDF documents
* Automatic text extraction and chunking
* Semantic search using vector embeddings
* Context-aware Q&A powered by an LLM
* Simple interactive UI
* Cloud-native vector database

---

## 🧠 Architecture

**High-level flow:**

PDF → Text Extraction → Chunking → Embeddings → Qdrant → Retrieval → LLM → Answer

### Detailed Flow

1. **PDF Upload**
   The user uploads a PDF file via the Streamlit frontend.

2. **Text Extraction & Chunking**
   The backend extracts text from the PDF and splits it into semantically meaningful chunks.

3. **Embedding Generation**
   Each text chunk is converted into a vector embedding using a Hugging Face embedding model.

4. **Vector Storage (Qdrant)**
   Embeddings and metadata are stored in Qdrant Cloud for efficient similarity search.

5. **Semantic Retrieval**
   When a user asks a question, the query is embedded and used to retrieve the most relevant chunks from Qdrant.

6. **LLM Answer Generation**
   The retrieved context is passed to a Hugging Face LLM, which generates a grounded answer based on the document content.

---

## 🛠 Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
* **Vector Database**: [Qdrant Cloud](https://qdrant.tech/)
* **LLM & Embeddings**: [Hugging Face](https://huggingface.co/)

---

## 📂 Project Structure

```
AiTravelAssistant/
├── frontend/
│   └── app.py              # Streamlit UI
├── backend/
│   ├── main.py             # FastAPI entry point
│   ├── Embeddings.py       # convert text to embeddings
│   ├── generator.py        # generate final answer
│   ├── ingest.py           # read and extract from pdf
│   └── retrievers.py       # retrieve relvant info stored in DB previous             
├── requirements.txt
├── .env
└── README.md
```

---

## ▶️ Running the App

### Start Backend (FastAPI)

```
uvicorn src.main:app --reload
```
http://127.0.0.1:8000/docs#/

### Start Frontend (Streamlit)

```
streamlit run src/app.py
```

---

## 🔌 API Examples

### Upload PDF

**Endpoint**
```
POST /upload
```

**Request**

```
multipart/form-data
file: travel.pdf
```

**Response**

```json
{
  "status": "success",
  "chunks_indexed": 42
}
```

---

### Ask a Question

**Endpoint**

```
POST /query
```

**Request Body**

```json
{
  "question": "What time is my flight to Paris?"
}
```

**Response**

```json
{
  "answer": "Your flight to Paris departs at 7:45 PM on June 12th from SFO."
}
```

---

## 🖼 Screenshots


---

## 🙌 Acknowledgements

* Hugging Face
* Qdrant
* Streamlit
* FastAPI

