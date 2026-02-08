import streamlit as st
from rag_chain import get_rag_chain

st.set_page_config(page_title="Healthcare RAG Chatbot")

st.title("🩺 Healthcare RAG Chatbot")
st.write("Gemini → Ollama | Gemini → HuggingFace fallback")

qa_chain = get_rag_chain()

question = st.text_input("Ask a healthcare question")

if question:
    with st.spinner("Thinking..."):
        response = qa_chain.invoke(question)

        st.subheader("📌 Answer")
        if hasattr(response, "content"):
            st.write(response.content)
        else:
            st.write(response)