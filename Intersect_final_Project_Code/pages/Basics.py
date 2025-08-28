import streamlit as st
from pathlib import Path

# Get the directory of the current script (e.g., '/pages')
pages_dir = Path(__file__).parent

# Get the root directory of the project (go up one level from 'pages')
root_dir = pages_dir.parent

# Main Title
st.title("🌟 **Basics of Set Theory** 🌟")

# Introduction Section
st.markdown("""
### Welcome to Set Theory Basics!
Explore key concepts in set theory through clear explanations, visuals, and examples.  
Here’s what we’ll cover:
- 🌍 Universal Set  
- 🔢 Natural Numbers  
- 📂 Subsets  
- ⚖️ Equal Sets  
- ➕ Union of Sets  
- 🛠️ Finite Sets  
""")

# Tab Layout for Topics
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🌍 Universal Set", 
    "🔢 Natural Numbers", 
    "📂 Subsets", 
    "⚖️ Equal Sets", 
    "➕ Union of Sets", 
    "🛠️ Finite Sets"
])

# Tab 1: Universal Set
with tab1:
    st.header("🌍 Universal Set")
    st.write("""
    A **Universal Set** contains all possible elements under consideration for a specific topic, denoted by `U`.  
    For example: If the universal set represents "all flowers," subsets might include roses, tulips, and sunflowers.  
    """)
    # Pathlib adjusted image path
    image_path = root_dir / "images" / "Universal-Set.png"
    st.image(str(image_path), caption="Universal Set Visualization (Placeholder Image)")
    st.markdown("""
    #### Key Points:
    - The complement of a universal set is an **empty set** (`Φ` or `{}`).
    - In Venn diagrams, the universal set is represented as a rectangle enclosing all subsets.
    #### Examples:
    - The set of all English letters in the alphabet.
    """)

# Tab 2: Natural Numbers
with tab2:
    st.header("🔢 Natural Numbers")
    st.write("""
    The **Natural Numbers** are all positive integers starting from 0 to infinity, denoted by `ℕ`.  
    Examples: `ℕ = {0, 1, 2, 3, ...}`  
    """)
    st.markdown("""
    #### Subsets of Natural Numbers:
    - Set of all even numbers: `{2, 4, 6, ...}`  
    - Set of all odd numbers: `{1, 3, 5, ...}`  
    - Multiples of a number: `{n, 2n, 3n, ...}`  
    """)
    # Pathlib adjusted image path
    image_path = root_dir / "images" / "Natural-Numbers.png"
    st.image(str(image_path), caption="Visualizing Natural Numbers (Placeholder Image)")

# Tab 3: Subsets
with tab3:
    st.header("📂 Subsets")
    st.write("""
    A **Subset** contains elements that are all found in another set (called the **superset**).  
    For example: If `A = {1, 2}` and `B = {1, 2, 3, 4}`, then `A ⊆ B`.  
    """)
    # Pathlib adjusted image path
    image_path = root_dir / "images" / "Subset.jpeg"
    st.image(str(image_path), caption="Subsets Representation (Placeholder Image)")
    st.markdown("""
    #### Key Points:
    - Every set is a subset of itself: `A ⊆ A`.  
    - The empty set `{}` is a subset of every set.  
    - A **Proper Subset** is a subset that is not equal to the original set.
    """)

# Tab 4: Equal Sets
with tab4:
    st.header("⚖️ Equal Sets")
    st.write("""
    Two sets are **Equal** if they contain exactly the same elements.  
    Example: If `A = {1, 2, 3}` and `B = {3, 2, 1}`, then `A = B`.  
    """)
    # Pathlib adjusted image path
    image_path = root_dir / "images" / "Equal-Sets.jpg"
    st.image(str(image_path), caption="Equal Sets Visualization (Placeholder Image)")
    st.markdown("""
    #### Cardinality of Equal Sets:
    - Equal sets have the same **cardinality** (number of elements): `|A| = |B|`.
    - Equivalent sets have the same number of elements but not necessarily the same elements.
    """)

# Tab 5: Union of Sets
with tab5:
    st.header("➕ Union of Sets")
    st.write("""
    The **Union** of two or more sets includes all unique elements from those sets, denoted as `A ∪ B`.  
    Formula: `|A ∪ B| = |A| + |B| - |A ∩ B|`  
    """)
    # Pathlib adjusted image path
    image_path = root_dir / "images" / "Union.png"
    st.image(str(image_path), caption="Union of Sets Visualization (Placeholder Image)")
    st.markdown("""
    #### Difference from Universal Set:
    - The **union** includes elements from specific sets.  
    - The **universal set** includes all elements under consideration, even those not part of any set.  
    """)

# Tab 6: Finite Sets
with tab6:
    st.header("🛠️ Finite Sets")
    st.write("""
    A **Finite Set** is a set with a countable number of elements.  
    For example:  
    - The set of even numbers between 0 and 50: `{2, 4, 6, ..., 50}`  
    - The set of prime numbers less than 20: `{2, 3, 5, 7, 11, 13, 17, 19}`  
    """)
    # Pathlib adjusted image path
    image_path = root_dir / "images" / "Finite-Sets.jpg"
    st.image(str(image_path), caption="Finite Set Example (Placeholder Image)")

# Footer
st.markdown("---")