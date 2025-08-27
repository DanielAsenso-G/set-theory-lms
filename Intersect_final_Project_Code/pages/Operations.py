import streamlit as st
import os

# Operations on sets
st.title("🛠️ Operations on Sets")

st.write("""
In this section, we’ll explore four key operations on sets:  
- 🌀 **Complement** - ➖ **Difference** - 📚 **Power Set** - 🔄 **Cartesian Product** Let’s learn and interact with these operations! 🚀
""")

st.header("📖 __Definitions__")

# Creating tabs for each operation
tab1, tab2, tab3, tab4 = st.tabs(["🌀 Complement", "➖ Difference", "📚 Power Set", "🔄 Cartesian Product"])

# Tab 1: Complement
with tab1:
    st.header("🌀 Complement")
    st.write("""
The **complement** of a set includes all the members of the universal set that are NOT in that set.  
It is denoted by \( A' \).  
For example, if the universal set \( U = \{a, b, c, d\} \) and \( A = \{a, b\} \), then \( A' = \{c, d\} \).
    """)

    st.image("images/Universal-Set.png", caption="Complement Example (Placeholder Image)")

    st.write("""
In the image above:  
- \( A' \) contains all elements outside set \( A \).  
- If \( C = \{c\} \), then \( C' = \{a, b, d\} \).  
    """)

    st.subheader("💡 Key Points:")
    st.write("""
    - The complement depends on the universal set.  
    - \( A \\cup A' = U \) (the union of a set and its complement gives the universal set).  
    - \( A \\cap A' = \\emptyset \) (a set and its complement have no common elements).  
    """)

    # Interactive Question
    st.subheader("❓ Question")
    answer = st.radio(
        "If \( U = \{1, 2, 3, 4, 5\} \) and \( A = \{1, 3\} \), what is \( A' \)?",
        options=["{2, 4, 5}", "{1, 3, 5}", "{1, 2}"]
    )
    if st.button("Submit Answer (Complement)"):
        if answer == "{2, 4, 5}":
            st.success("✅ Correct! \( A' \) includes all elements of \( U \) not in \( A \).")
        else:
            st.error("❌ Incorrect. Review the definition of complement.")

# Tab 2: Difference
with tab2:
    st.header("➖ Difference")
    st.write("""
The **difference** of two sets, \( A \) and \( B \), is the set of elements that are in \( A \) but not in \( B \).  
It is written as \( A - B \).  
For example, if \( A = \{1, 3, 5, 7\} \) and \( B = \{1, 5\} \), then \( A - B = \{3, 7\} \).  
    """)

    st.image("images/Difference.png", caption="Difference of Sets")

    st.subheader("💡 Key Points:")
    st.write("""
    - \( A - B \) removes all elements of \( B \) from \( A \).  
    - \( A - A = \\emptyset \) (the difference of a set with itself is empty).  
    - \( A - \\emptyset = A \).  
    """)

    # Interactive Question
    st.subheader("❓ Question")
    answer = st.radio(
        "If \( A = \{2, 4, 6, 8\} \) and \( B = \{4, 8\} \), what is \( A - B \)?",
        options=["{2, 6}", "{4, 8}", "{2, 4, 6, 8}"]
    )
    if st.button("Submit Answer (Difference)"):
        if answer == "{2, 6}":
            st.success("✅ Correct! \( A - B \) removes elements in \( B \) from \( A \).")
        else:
            st.error("❌ Incorrect. Make sure to subtract all elements of \( B \) from \( A \).")

# Tab 3: Power Set
with tab3:
    st.header("📚 Power Set")
    st.write("""
The **power set** of a set is the set of all possible subsets of that set, including the empty set and the set itself.  
For example, if \( A = \{1, 2\} \), then:  
\[ P(A) = \{\\emptyset, \{1\}, \{2\}, \{1, 2\}\} \]  
    """)

    st.image("images/Power-Set.png", caption="Power Set")

    st.subheader("💡 Key Points:")
    st.write("""
    - If a set has \( n \) elements, its power set will have \( 2^n \) subsets.  
    - The empty set \( \\emptyset \) is always a subset.  
    - The original set is included in the power set.  
    """)

    # Interactive Question
    st.subheader("❓ Question")
    answer = st.radio(
        "If \( A = \{x, y\} \), how many subsets are in \( P(A) \)?",
        options=["2", "3", "4"]
    )
    if st.button("Submit Answer (Power Set)"):
        if answer == "4":
            st.success("✅ Correct! A set with 2 elements has \( 2^2 = 4 \) subsets.")
        else:
            st.error("❌ Incorrect. Remember, the number of subsets is \( 2^n \).")

# Tab 4: Cartesian Product
with tab4:
    st.header("🔄 Cartesian Product")
    st.write("""
The **Cartesian Product** of two sets, \( A \) and \( B \), is the set of all ordered pairs \( (a, b) \), where \( a \\in A \) and \( b \\in B \).  
For example, if \( A = \{1, 2\} \) and \( B = \{x, y\} \), then:  
\[ A \\times B = \{(1, x), (1, y), (2, x), (2, y)\} \]  
    """)

    st.image("images/Cartesian.jpeg", caption="Cartesian Product")

    st.subheader("💡 Key Points:")
    st.write("""
    - The Cartesian product creates pairs from elements of two sets.  
    - If \( A \) has \( m \) elements and \( B \) has \( n \) elements, \( A \\times B \) will have \( m \\times n \) elements.  
    - \( A \\times B \\neq B \\times A \) (order matters!).  
    """)

    # Interactive Question
    st.subheader("❓ Question")
    answer = st.radio(
        "If \( A = \{1\} \) and \( B = \{2, 3\} \), what is \( A \\times B \)?",
        options=["{(1, 2), (1, 3)}", "{(2, 1), (3, 1)}", "{(1, 2), (1, 3), (2, 1)}"]
    )
    if st.button("Submit Answer (Cartesian Product)"):
        if answer == "{(1, 2), (1, 3)}":
            st.success("✅ Correct! Each element in \( A \) pairs with all elements in \( B \).")
        else:
            st.error("❌ Incorrect. Remember to pair every element in \( A \) with each element in \( B \).")