import streamlit as st



quiz_generator_page = st.Page(
    page = "app_pages/quiz_generator.py",
    title = "Quiz",
    icon = "🎓"
)

home_page = st.Page(
    page = "app_pages/home_page.py",
    title = "Home Page",
    icon = "🏠",
    default = True
)
resources_page = st.Page(
    page = "app_pages/resources.py",
    title = "Helpful Resources",
    icon = "📚"
)

Introduction_to_sets_page = st.Page(
    page = "app_pages/Basics.py",
    title = "Introduction To Sets",
    icon = "📝"
)
Sets_Theoretic_Laws_page = st.Page(
    page = "app_pages/SetTheoreticLaws.py",
    title = "Set Theoretic Laws",
    icon = "📝"
)
ApplicationsOfSets_page = st.Page(
    page = "app_pages/ApplicationsOfSets.py",
    title = "Applications of Sets",
    icon = "📝"
)
Interactive_Proof_in_set_theory_page = st.Page(
    page = "app_pages/InteractiveProofInSetTheory.py",
    title = "Interactive Set Proofs",
    icon = "📝"
)
Advanced_Applications_on_sets_page = st.Page(
    page = "app_pages/AdvancedApplicationsOnSets.py",
    title = "Advanced Applications On Sets",
    icon = "📝"
)

Operations_page = st.Page(
    page = "app_pages/Operations.py",
    title = "Operations on Sets",
    icon = "📝"
)
Relations_page = st.Page(
    page = "app_pages/Relations.py",
    title = "Set Relations",
    icon = "📝"
)

Special_page = st.Page(
    page = "app_pages/Special.py",
    title = "Special",
    icon = "📝"
)

set_visualizer_page = st.Page(
    page = "app_pages/set_visualizers.py",
    title = "Set Visualizer",
    icon = "📊"
)
notes_page = st.Page(
    page = "app_pages/notes.py",
    title = "Personal Notes",
    icon = "📒"
)




pg = st.navigation(
    {
        "General" : [home_page],
        "Modules" : [Introduction_to_sets_page, Operations_page, Relations_page, Special_page,Sets_Theoretic_Laws_page,Interactive_Proof_in_set_theory_page,ApplicationsOfSets_page,Advanced_Applications_on_sets_page],
        "Quiz": {quiz_generator_page},
        "Help": {set_visualizer_page, resources_page, notes_page}
    }
)

pg.run()
