import streamlit as st
import requests
import base64

BACKEND_URL = "http://127.0.0.1:5000/generate"

st.set_page_config(page_title="GenSpark Lite", layout="wide")

st.markdown(
    """
    <h1 style='text-align:center; color:#1E3A8A;'>GenSpark Lite</h1>
    """,
    unsafe_allow_html=True,
)

topic = st.text_input("Enter your topic", placeholder="e.g. Artificial Intelligence")
slides = st.number_input("Number of slides", min_value=5, max_value=16, value=3)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<h3 style='text-align:center;'>Select a Theme</h3>",
    unsafe_allow_html=True,
)

themes = {
    " Navy ": "#1E3A8A",
    " White ": "#F5F5F5",
    " Modern Dark ": "#1E1E1E",
    " Baby Blue ": "#2563EB"
}

cols = st.columns(len(themes))
selected_theme = list(themes.keys())[0]

for i, (theme_name, color) in enumerate(themes.items()):
    with cols[i]:
        st.markdown(f"<p style='text-align:center; font-weight:bold;'>{theme_name}</p>", unsafe_allow_html=True)
        if st.button("", key=theme_name, help=theme_name, use_container_width=True):
            selected_theme = theme_name
        st.markdown(
            f"<div style='height:30px; background-color:{color}; border-radius:6px;'></div>",
            unsafe_allow_html=True,
        )

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Generate Presentation", use_container_width=True):
        if not topic.strip():
            st.error("Please enter a topic first.")
        else:
            with st.spinner("Generating presentation ...."):
                try:
                    response = requests.post(BACKEND_URL, json={"topic": topic, "slides": slides})
                    if response.status_code == 200:
                        file_data = response.content
                        b64 = base64.b64encode(file_data).decode()
                        href = f'<a href="data:application/vnd.openxmlformats-officedocument.presentationml.presentation;base64,{b64}" download="{topic.replace(" ", "_")}.pptx">Download Presentation</a>'
                        st.success("Presentation generated successfully")
                        st.markdown(href, unsafe_allow_html=True)
                    else:
                        st.error(f"Server error: {response.status_code}")
                except Exception as e:
                    st.error(f"Error connecting to server: {e}")


