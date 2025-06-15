from crewai import LLM

def get_llm():
    return LLM(
        model="ollama/llama3.2:latest",
        base_url="http://localhost:11434"
    )