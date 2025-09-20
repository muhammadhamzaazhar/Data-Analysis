import html
import streamlit as st

def render_chat(question: str, answer: str | dict | None):
    st.markdown(
        f"""
        <div style="display:flex; justify-content:flex-end; margin:14px 0;">
            <div style="
                position:relative;
                background:#1e9bff;
                color:#ffffff;
                padding:12px 18px;
                border-radius:18px 18px 4px 18px;
                max-width:70%;
                word-wrap:break-word;
                box-shadow:0 4px 10px rgba(0,0,0,0.15);
            ">
                {question}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if answer is None:
        return

    if isinstance(answer, dict) and answer.get("type") == "plot":
        st.image(
            answer["value"], 
            width=600,
            caption=answer.get("chart_description", "")
        )
        return

    answer_text = answer["value"] if isinstance(answer, dict) else str(answer)

    st.write(
        f"""
        <div style="display:flex; justify-content:flex-start; margin:14px 0;">
            <div style="
                position:relative;
                background:#3b3b3d;
                color:#ffffff;
                padding:12px 18px;
                border-radius:18px 18px 18px 4px;
                max-width:70%;
                word-wrap:break-word;
                box-shadow:0 4px 10px rgba(0,0,0,0.15);
            ">
                {answer_text}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
