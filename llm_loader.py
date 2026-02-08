from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
from langchain_google_genai._common import GoogleGenerativeAIError


def get_llm():
    try:
        print("🔹 Using Gemini LLM")
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            temperature=0.2
        )
        llm.invoke("hello")
        return llm

    except GoogleGenerativeAIError:
        print("⚠️ Gemini quota exceeded")

    except Exception as e:
        print("⚠️ LLM error:", e)

    print("🔁 Falling back to Ollama (local)")
    return Ollama(
        model="llama3",
        temperature=0.2
    )
