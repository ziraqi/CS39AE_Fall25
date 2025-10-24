import streamlit as st

st.title("👋 My Bio")

NAME = "Zakaria Iraqi"
PROGRAM = "MSU Denver Computer Science Bachelor's of Science"
INTRO = (
    "Hello everyone! I'm Zakaria Iraqi, currently pursuing my Bachelor's degree in Computer Science at MSU Denver. " \
    "I am a self-motivated and passionate individual with a keen interest in technology and programming. " \
    "I am currently working on a project that involves building a web application that displays drift detection" \
    " in a machine learning model using React + Vite for the frontend."
    "Data Visualization is very exciting because it enables the viewer to analyze separate patters that may not have" \
    " been obvious in raw data. I am eager to learn more and contribute to the field of computer science" \
    " through my studies and projects."
)
FUN_FACTS = [
    "I love playing basketball and pickleball during my free time.",
    "I'm learning Spanish to add on to my repertoire of languages and hope to become fluent one day.",
    "I want to build a tech startup that enables 3rd world countries to have better access to technology.",
]
PHOTO_PATH = "profile.jpg"  # Put a file in repo root or set a URL

# ---------- Debug Section (REMOVE AFTER TESTING) ----------
st.write("🔍 **Debug Info:**")
st.write(f"Looking for image at: {PHOTO_PATH}")
st.write(f"File exists: {os.path.exists(PHOTO_PATH)}")
st.write(f"Current directory: {os.getcwd()}")
st.write(f"Files in current directory: {os.listdir('.')}")
if os.path.exists('assets'):
    st.write(f"Files in assets: {os.listdir('assets')}")
st.write("---")

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    # Try multiple paths
    paths_to_try = ["profile.jpg", "assets/profile.jpg", "./profile.jpg"]
    image_loaded = False
    
    for path in paths_to_try:
        if os.path.exists(path):
            try:
                st.image(path, caption=NAME, width="auto")
                image_loaded = True
                st.success(f"✅ Image loaded from: {path}")
                break
            except Exception as e:
                st.error(f"Error loading from {path}: {str(e)}")
    
    if not image_loaded:
        st.error("❌ Could not load image from any path")
        st.info("Add a photo named 'profile.jpg' to the repo root")
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
