import streamlit as st
import base64
import textwrap


def header_home():
    with open("src/ui/logo_url.png", "rb") as f:
        image = base64.b64encode(f.read()).decode()

    html = f"""
<div style="
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    margin-bottom: 30px;
">
    <img
        src="data:image/png;base64,{image}"
        style="
            height: 100px;
            width: 100px;
            object-fit: contain;
        "
    >
    <div>
    <h1>SNAP CLASS</h1>
    </div>
</div>
"""

    st.markdown(
        textwrap.dedent(html),
        unsafe_allow_html=True
    )

def header_dashboard():
    with open("src/ui/logo_url.png", "rb") as f:
        image = base64.b64encode(f.read()).decode()

    html = f"""
<div style="
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px">
    <img
        src="data:image/png;base64,{image}"
        style="
            height: 100px;
            width: 100px;
            object-fit: contain;
        "
    >
    <div style="color:#5865F2">
    <h2>Snap Class</h2>
    </div>
</div>
"""

    st.markdown(
        textwrap.dedent(html),
        unsafe_allow_html=True
    )