🩺 Healthcare RAG Chatbot (Free-Tier, Production-Safe)

An end-to-end Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions from healthcare PDF documents.
The system is designed to work entirely on free tiers, with robust fallbacks to avoid runtime failures.

🚀 Project Overview

This project demonstrates a real-world RAG pipeline used in healthcare document analysis:

Upload healthcare PDFs (guidelines, reports, notes)

Convert documents into embeddings

Store embeddings in a vector database

Retrieve relevant context for each query

Generate accurate answers using LLMs

The architecture avoids unstable LangChain abstractions and uses LCEL (Runnable pipelines) for long-term stability.

🧠 Architecture (High Level)
PDFs
  ↓
Text Splitter
  ↓
Embeddings (Gemini → HuggingFace fallback)
  ↓
ChromaDB (Vector Store)
  ↓
Retriever (Top-K similarity search)
  ↓
LLM (Gemini → HuggingFace / Ollama fallback)
  ↓
Streamlit UI

🛠️ Tech Stack

Python

LangChain (LCEL / Runnable architecture)

Google Gemini API (Primary LLM + Embeddings)

HuggingFace Embeddings (Fallback)

Ollama (Local LLM – Optional)

ChromaDB (Vector Database)

Streamlit (UI)

PyPDF (PDF ingestion)

📂 Project Structure
Healthcare_RAG_Chatbot/
│
├── app.py                 # Streamlit UI
├── ingest.py              # PDF ingestion + embedding
├── rag_chain.py           # RAG pipeline (LCEL-based)
├── embeddings_loader.py   # Embedding fallback logic
├── llm_loader.py          # LLM fallback logic
├── requirements.txt
├── .env                   # API keys (not committed)
│
├── data/
│   └── sample_docs/       # Healthcare PDFs
│
└── chroma_db/             # Vector database (auto-generated)

⚙️ Setup Instructions
1️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token

4️⃣ Add Healthcare PDFs

Place PDFs inside:

data/sample_docs/

5️⃣ Ingest Documents
python ingest.py


This will:

Load PDFs

Split text into chunks

Generate embeddings

Store them in ChromaDB

6️⃣ Run the App
streamlit run app.py

💬 Example Questions to Ask

“What is the main topic discussed in the document?”

“Summarize the key medical recommendations.”

“What are the risks or precautions mentioned?”

“Explain this document in simple terms.”

🖥️ UI Demo

![alt text](image-3.png)
![alt text](image-4.png)



🔁 Local vs Cloud Model Strategy (IMPORTANT)

This project is intentionally designed to work in both local and cloud environments.

☁️ Cloud Mode (Recommended for Deployment)

Used when:

Deploying to Streamlit Cloud / AWS / GCP

Demonstrating to recruiters

Models:

✅ Gemini (Primary)

✅ HuggingFace (Fallback)

Why:

No hardware dependency

Stable on free tiers

Works in production environments

💻 Local Mode (Optional – Development Only)

Used when:

Experimenting locally

Learning about local LLMs

Model:

Ollama (e.g., phi3, quantized models)

Important Notes:

Requires Ollama to be running on localhost:11434

Needs sufficient RAM

Not suitable for cloud deployment

Disabled by default in production logic

Ollama is treated as an optional local enhancement, not a hard dependency.

🧩 Key Engineering Decisions

❌ Avoided langchain.chains (frequent breaking changes)

✅ Used LCEL (Runnable pipelines) for stability

✅ Normalized LLM outputs (str vs AIMessage)

✅ Graceful fallback logic to prevent crashes

✅ Free-tier friendly design

📈 Why This Project Matters

This project demonstrates:

Practical RAG implementation

Handling API rate limits & failures

Production-safe fallback strategies

Awareness of local vs cloud constraints

Clean architecture suitable for real deployments

🔮 Future Enhancements

Source document citations in UI

Chat history memory

User PDF upload from UI

Role-based access (doctor / patient views)

Cloud deployment (Streamlit Cloud / AWS)

👤 Author

Rohithkumar Bala
Aspiring AI Engineer | GenAI | RAG | LLM Systems
