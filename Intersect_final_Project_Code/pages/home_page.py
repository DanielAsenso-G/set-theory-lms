import streamlit as st
from Intersect_app import *
from pathlib import Path

# Get the directory of the current script (e.g., '/pages')
pages_dir = Path(__file__).parent

# Get the root directory of the project (go up one level from 'pages')
root_dir = pages_dir.parent


st.title("Welcome to the Intersect Set Learning Platform 🎉")
st.write("Our goal is to make learning about sets fun and easy for you! 🚀 Let's dive into the world of sets and see how they connect to everything around us. 🌍")

# Define sections and corresponding page paths
# Structured Sections
sections = [
    {"title": "Home Page 🏠",
     "desc": "Welcome to the Set Theory Learning Platform! Explore the modules and boost your set theory skills. 🔍",
     "page": home_page,
     "image": root_dir / "images" / "16.png"},

    {"title": "Introduction to Sets 📚",
     "desc": "Let's start with the basics of sets and see why they're so important in math! 🤓",
     "page": Introduction_to_sets_page,
     "image": root_dir / "images" / "1.png"},

    {"title": "Operations on Sets 🔄",
     "desc": "Learn how to perform set operations like union, intersection, and difference. ⚡",
     "page": Operations_page,
     "image": root_dir / "images" / "2.png"},

    {"title": "Set Relations 🔗",
     "desc": "Discover the relationships between sets, like subsets and supersets. 💡",
     "page": Relations_page,
     "image": root_dir / "images" / "3.png"},

    {"title": "Special Sets 🌟",
     "desc": "Explore some unique sets like singleton, empty, and universal sets. 🌐",
     "page": Special_page,
     "image": root_dir / "images" / "4.png"},

    {"title": "Set Theoretic Laws 📜",
     "desc": "Learn the core laws of set theory, like De Morgan's laws. 🔍",
     "page": Sets_Theoretic_Laws_page,
     "image": root_dir / "images" / "5.png"},

    {"title": "Interactive Set Proofs 🔐",
     "desc": "Engage with cool interactive proofs to deepen your set theory knowledge. 🧠",
     "page": Interactive_Proof_in_set_theory_page,
     "image": root_dir / "images" / "6.png"},

    {"title": "Applications of Sets 💼",
     "desc": "See how set theory helps in real-world fields like tech, healthcare, and more! 🌍",
     "page": ApplicationsOfSets_page,
     "image": root_dir / "images" / "7.png"},

    {"title": "Advanced Applications on Sets 🚀",
     "desc": "Go deeper into complex set theory applications in data science, AI, and more. 🤖",
     "page": Advanced_Applications_on_sets_page,
     "image": root_dir / "images" / "8.png"},

    {"title": "Quiz 🎮",
     "desc": "Test your knowledge with fun quizzes on each topic. 📝",
     "page": quiz_generator_page,
     "image": root_dir / "images" / "9.png"},

    {"title": "Set Visualizer 🎨",
     "desc": "Visualize set operations and relationships with interactive diagrams. 🔍",
     "page": set_visualizer_page,
     "image": root_dir / "images" / "11.png"},

    {"title": "Helpful Resources 📘",
     "desc": "Find extra resources to take your learning to the next level! 🚀",
     "page": resources_page,
     "image": root_dir / "images" / "10.png"},

    {"title": "Personal Notes 📝",
     "desc": "Keep track of your progress and jot down personal notes. 💡",
     "page": notes_page,
     "image": root_dir / "images" / "15.png"}
]

# Displaying sections in a two-column layout
for i in range(0, len(sections), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(sections):
            section = sections[i + j]
            with cols[j]:
                st.markdown(f"### {section['title']}")
                st.write(section['desc'])
                # Use str() to convert the Path object to a string for st.image
                st.image(str(section["image"]), width=100)
                st.page_link(label=f"Go to {section['title']} 👉", page=section["page"])
    st.write("---")
    st.write("\n")