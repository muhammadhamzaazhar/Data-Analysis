import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def check_env_vars():
    required_vars = ["OPENROUTER_API_KEY", "LLM_MODEL"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        st.error("Configuration Error")
        st.markdown("""
        The required environment variables are missing:
        
        Please create a `.env` file in the project root with these variables:
        ```
        OPENROUTER_API_KEY=your_api_key_here
        LLM_MODEL=openrouter/deepseek/deepseek-chat-v3.1:free   # or any other supported model
        LLM_TEMPERATURE=0.5        # optional, default is 0.5
        ```
        """)
        return False
    return True