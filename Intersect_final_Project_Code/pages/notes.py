import streamlit as st
from io import BytesIO


# Our Custom CSS for a better UI
st.markdown(
    """
    <style>
    .stTextArea {
        background-color: #f9f9f9;
        border-radius: 8px;
        padding: 10px;
        font-family: "Courier New", Courier, monospace;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .success-message {
        color: #4CAF50;
        font-weight: bold;
    }
    .warning-message {
        color: #FF9800;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for notes
if "notes" not in st.session_state:
    st.session_state.notes = ""

# Notes Header
st.title("📝 Notes")
st.write("Keep track of your thoughts and learnings with this handy note-taking tool. Your notes are **automatically saved** during this session!")

# Text area for notes input
user_notes = st.text_area(
    "🖊️ Write your notes below:",
    value=st.session_state.notes,
    placeholder="Start typing here...",
    height=200,
)

# Save notes to session state
if user_notes != st.session_state.notes:
    st.session_state.notes = user_notes
    st.markdown('<p class="success-message">✅ Notes saved successfully!</p>', unsafe_allow_html=True)

# Buttons Section
col1, col2 = st.columns(2)

with col1:
    if st.button("💾 Save Session"):
        st.markdown('<p class="success-message">Your notes are saved for this session!</p>', unsafe_allow_html=True)

with col2:
    if st.button("📤 Export Notes"):
        if st.session_state.notes.strip():
            # Export notes as a downloadable file
            notes_file = BytesIO()
            notes_file.write(st.session_state.notes.encode("utf-8"))
            notes_file.seek(0)
            st.download_button(
                label="📂 Download Your Notes",
                data=notes_file,
                file_name="my_notes.txt",
                mime="text/plain",
            )
        else:
            st.markdown('<p class="warning-message">⚠️ No notes to export. Please type your notes first!</p>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    ---
    💡 *Pro Tip:* Your notes are saved during this session. Export them for permanent storage or when you're ready to revisit your insights.
    """
)
