import streamlit as st

from utils.config_validator import check_env_vars
from core.data_analyzer import DataAnalyzer
from utils.chat_layout import render_chat

st.set_page_config(page_title="AI Data Analyst", page_icon="📊", layout="wide")
               
def main():
    if not check_env_vars():
        return
    
    st.title("AI Data Analyst")
    st.write("Upload your data and let the AI analyze it for you!")

    st.sidebar.header("1. Upload Your Data")
    uploaded_file = st.sidebar.file_uploader(
        "Choose a CSV or Excel file",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:
        st.sidebar.success(f"File uploaded: {uploaded_file.name}")

    st.session_state.setdefault("analyzing", False)
    st.session_state.setdefault("chat_history", [])

    chat_container = st.container()

    st.sidebar.header("2. Ask a Question")
    with st.sidebar.form("query_form"):
        query = st.text_area(
            "Enter your question about the data:",
            height=100,
            placeholder="E.g., What are the key insights from this data?"
        )
        analyze_btn = st.form_submit_button(
            "Analyze Data",
            type="primary",
            disabled=(not uploaded_file or st.session_state.analyzing)
        )

    if analyze_btn and uploaded_file and query:
        st.session_state.analyzing = True
        st.session_state.chat_history.append({
            "question": query,
            "answer": None 
        })
        st.rerun()

    if st.session_state.analyzing and st.session_state.chat_history and st.session_state.chat_history[-1]["answer"] is None:
        query = st.session_state.chat_history[-1]["question"]
        with st.spinner("Analyzing your data..."):
            try:
                analyzer = DataAnalyzer(uploaded_file)
                response = analyzer.analyze(query)
                st.session_state.chat_history[-1]["answer"] = response
            except Exception as e:
                st.error(f"An error occurred during processing: {str(e)}")
                st.exception(e)
            finally:
                st.session_state.analyzing = False
                st.rerun()

    for chat in st.session_state.chat_history:
        with chat_container:
            render_chat(chat["question"], chat["answer"])

if __name__ == "__main__":
    main()
