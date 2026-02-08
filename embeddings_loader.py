
"""
Returns embeddings with automatic fallback:
1. Try Gemini embeddings
2. If quota / rate limit occurs → switch to HuggingFace
"""

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai._common import GoogleGenerativeAIError


def get_embeddings():
    try:
        print("🔹 Trying Gemini embeddings...")
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001"
        )

        # Test call to verify quota
        embeddings.embed_query("test")

        print("✅ Using Gemini embeddings")
        return embeddings

    except GoogleGenerativeAIError:
        print("⚠️ Gemini quota exceeded → switching to HuggingFace")

    except Exception as e:
        print("⚠️ Embedding error:", e)
        print("🔁 Switching to HuggingFace")

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
