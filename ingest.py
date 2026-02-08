import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from embeddings_loader import get_embeddings

DATA_PATH = "data/sample_docs"
DB_PATH = "chroma_db"


def ingest_documents():
    docs = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_PATH, file))
            docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(docs)
    embeddings = get_embeddings()

    Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=DB_PATH
    )

    print("✅ Documents ingested successfully")


if __name__ == "__main__":
    ingest_documents()
