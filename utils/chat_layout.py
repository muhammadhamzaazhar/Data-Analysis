import html
import streamlit as st

def render_chat(question, answer):
    st.write(
        f"""
        <div style="display:flex; justify-content:flex-end; margin:12px 0;">
            <div style="
                background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
                color: white;
                padding: 12px 18px;
                border-radius: 6px 20px 6px 20px;
                max-width: 70%;
                word-wrap: break-word;
                box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            ">
                {html.escape(question)}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
       
    if answer is not None:
        if isinstance(answer, dict) and answer["type"] == "plot":
            st.plotly_chart(
                answer["value"],
                use_container_width=False,
                config={
                    'scrollZoom': True,
                    'displayModeBar': True,
                    'responsive': False,  
                    'displaylogo': False,
                    'toImageButtonOptions': {
                        'format': 'png',
                        'filename': 'custom_image',
                        'scale': 2
                    }
                }
            )
        elif isinstance(answer, dict) and answer["type"] == "raw":
            st.write(answer["value"])
        else:
            st.write(answer)
