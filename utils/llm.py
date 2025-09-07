import os
from dotenv import load_dotenv
from pandasai_litellm.litellm import LiteLLM

load_dotenv()

def get_llm(model: str = None, temperature: float = 0.5):
    try:
        model = model or os.getenv("LLM_MODEL")
        temperature = float(temperature or os.getenv("LLM_TEMPERATURE"))
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise RuntimeError("OPENROUTER_API_KEY is not set in environment.")

        return LiteLLM(
            model=model,
            api_key=api_key,
            temperature=temperature
        )
    except Exception as e:
        raise RuntimeError(f"Failed to initialize LLM: {str(e)}")
    
