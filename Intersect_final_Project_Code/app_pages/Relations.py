import streamlit as st

# Relations between sets
st.title("🔗 Relations Between Sets")

st.write("""A list of topics to be covered in this section includes:
- 🔵 Venn diagram
- 🟠 Superset
- 🟡 Subset
- 🟢 Disjoint Sets
""")

st.header("📖 __Definitions__")
st.write("__Intersection__: An intersection of sets is the elements that both sets have in common. 🛠️")

# Creating tabs for topics
tab1, tab2, tab3, tab4 = st.tabs(["📊 Venn Diagram", "🔝 Superset", "📉 Subset", "🚫 Disjoint Set"])

# Tab 1: Venn Diagram
with tab1:
    st.header("📊 Venn Diagram")
    st.write("A Venn Diagram is a graphical representation of various sets and their relationships with each other.")
    st.write("Venn diagrams can represent intersections, unions, complements, and other operations regarding sets.")
    st.image("intersection-of-sets---venn-diagram.jpg", caption="Venn Diagram", use_container_width=True)
    st.write("The Venn diagram above shows the relationships between sets A and B, such as \( A \cap B \) (highlighted) and \( A \cup B \).")

    # Question for Venn Diagram
    st.subheader("❓ Question")
    answer = st.radio(
        "What does the highlighted region in the Venn Diagram represent?",
        options=["Union of sets A and B", "Intersection of sets A and B", "Complement of sets A and B"]
    )
    if st.button("Submit Answer (Venn Diagram)"):
        if answer == "Intersection of sets A and B":
            st.success("✅ Correct! The highlighted region shows the intersection, where sets A and B overlap.")
        else:
            st.error("❌ Incorrect. The highlighted region represents the intersection, not the union or complement.")

# Tab 2: Superset
with tab2:
    st.header("🔝 Superset")
    st.write("If one set is the superset of another, all the members in the other set can be found in the superset.")
    st.write("__For Example__: If Set B is the superset of Set A, all elements in Set A are found in Set B.")
    st.image("Superset.png", caption="Superset and Subset", use_container_width=True)
    st.write("In the image above, Set B is the superset of Set A because Set A contains {4, 2, 1} and Set B contains {1, 2, 3, 4, 5}.")

    # Question for Superset
    st.subheader("❓ Question")
    answer = st.radio(
        "Which statement is true if B is the superset of A?",
        options=[
            "All members of A are found in B.",
            "All members of B are found in A.",
            "A and B have no members in common."
        ]
    )
    if st.button("Submit Answer (Superset)"):
        if answer == "All members of A are found in B.":
            st.success("✅ Correct! By definition, a superset contains all members of the subset.")
        else:
            st.error("❌ Incorrect. A superset must include all members of the subset.")

# Tab 3: Subset
with tab3:
    st.header("📉 Subset")
    st.write("One set is a subset of another if all the members of that set can be found in another set.")
    st.subheader("For Example")
    st.write("The set of all dogs is a subset of the set of all animals because all dogs are animals.")
    st.image("Subset.jpeg", caption="Superset and Subset", use_container_width=True)
    st.write("Supersets and subsets are inversely related. If B is the superset of A, then A is the subset of B.")

    # Question for Subset
    st.subheader("❓ Question")
    answer = st.radio(
        "What does it mean if A is a subset of B?",
        options=[
            "A contains all members of B.",
            "All members of A are found in B.",
            "A and B are disjoint."
        ]
    )
    if st.button("Submit Answer (Subset)"):
        if answer == "All members of A are found in B.":
            st.success("✅ Correct! A subset is entirely contained within another set.")
        else:
            st.error("❌ Incorrect. A subset must have all its members in the other set.")

# Tab 4: Disjoint Sets
with tab4:
    st.header("🚫 Disjoint Sets")
    st.write("Disjoint sets are sets with no common members. Thus, they have no intersection.")
    st.subheader("For Example")
    st.write("The set of even numbers and the set of odd numbers are disjoint because they have no members in common.")
    st.image("Disjoint.png", caption="Disjoint Sets", use_container_width=True)
    st.caption("Image Credit: MathMonks.com")
    st.write("In the image above, Sets A and B are disjoint as they do not intersect.")

    # Question for Disjoint Sets
    st.subheader("❓ Question")
    answer = st.radio(
        "What is true about disjoint sets?",
        options=[
            "They have no members in common.",
            "One is a subset of the other.",
            "They always have an intersection."
        ]
    )
    if st.button("Submit Answer (Disjoint Sets)"):
        if answer == "They have no members in common.":
            st.success("✅ Correct! By definition, disjoint sets share no common elements.")
        else:
            st.error("❌ Incorrect. Disjoint sets do not intersect or share members.")

