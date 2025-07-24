from langchain_groq import ChatGroq

# Inizialization of LLM model
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)
