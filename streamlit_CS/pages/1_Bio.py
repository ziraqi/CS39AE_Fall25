import streamlit as st

st.title("👋 My Bio")

NAME = "Zakaria Iraqi"
PROGRAM = "MSU Denver Computer Science Bachelor's of Science"
INTRO = (
    "Hello everyone! I'm Zakaria Iraqi, currently pursuing my Bachelor's degree in Computer Science at MSU Denver. "
    "I am a self-motivated and passionate individual with a keen interest in technology and programming. "
    "I am currently working on a project that involves building a web application that displays drift detection "
    "in a machine learning model using React + Vite for the frontend. "
    "Data Visualization is very exciting because it enables the viewer to analyze separate patterns that may not have "
    "been obvious in raw data. I am eager to learn more and contribute to the field of computer science "
    "through my studies and projects."
)
FUN_FACTS = [
    "I love playing basketball and pickleball during my free time.",
    "I'm learning Spanish to add on to my repertoire of languages and hope to become fluent one day.",
    "I want to build a tech startup that enables 3rd world countries to have better access to technology.",
]
PHOTO_PATH = "profile.jpg"

# ---------- Layout ----------
# Remove vertical_alignment parameter
col1, col2 = st.columns([1, 2])  # ← CHANGED THIS LINE

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception as e:
        st.info(f"Add profile.jpg to the streamlit_CS folder")
        st.write(f"Error: {e}")  # This will help debug
        
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for f in FUN_FACTS:
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")