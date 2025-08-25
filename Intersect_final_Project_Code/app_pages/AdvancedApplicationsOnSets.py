import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import time

# Streamlit Interface
st.title("Advanced Applications of Sets in Computer Science")
st.header("Explore How Sets Are Applied in CS and DSA!", divider = "blue")
st.write("From search engines to efficient algorithms, sets play a pivotal role in solving real-world computer science problems.")
st.write("The point of this module is not to understand everything...")
st.write("It's to spark your interest in the real-world applications of what we have learned!")

# Section: Applications Overview
st.subheader("Applications of Sets in Computer Science")
applications = {
    "Application": [
        "Hash-Based Data Structures",
        "Graph Algorithms",
        "Database Query Optimization",
        "Text Processing",
        "Networking",
        "Search Algorithms",
        "Dynamic Programming",
        "Web Development",
    ],
    "Description": [
        "Hash sets enable O(1) insertion and lookup, critical for fast data access.",
        "Set operations like union and intersection are used in graph traversal (e.g., finding connected components).",
        "Relational operations like INTERSECT and MINUS are implemented using sets in query languages like SQL.",
        "Sets help identify unique words or substrings efficiently in natural language processing.",
        "Routing protocols use set theory to determine shortest paths and avoid loops.",
        "Sets are used in keyword matching for efficient search and retrieval.",
        "State sets are used to track subproblem solutions, reducing redundant computation.",
        "Sets manage cookies, sessions, and permissions to optimize web performance."
    ]
}

st.write("Below is a table of key applications:")
st.table(applications)

# Section: Visualization
st.subheader("Set-Based Operations in DSA")

# Dropdown to Select DSA Example
example = st.selectbox(
    "Select a DSA concept to visualize:",
    ["Finding Duplicates in an Array", "Union-Find for Disjoint Sets", "Common Elements in Two Arrays", "Graph Traversal with Set"]
)

# Define Set-Based Operations
if example == "Finding Duplicates in an Array":
    st.write("**Problem:** Identify duplicates in an array efficiently.")
    array = [1, 2, 3, 4, 3, 5, 1, 6]
    st.write("Array:", array)
    seen = set()
    duplicates = set(x for x in array if x in seen or seen.add(x))
    st.write("**Duplicates:**", duplicates)

elif example == "Union-Find for Disjoint Sets":
    st.write("**Problem:** Implement union and find operations for disjoint sets.")
    st.write("""
    Suppose we have three sets:  
    Set A = {1, 2}  
    Set B = {3, 4}  
    Set C = {5, 6}  
    **Union of A and B:** {1, 2, 3, 4}  
    **Find if 2 and 3 are in the same set:** False
    """)
    st.write("Union-Find is used in Kruskal's algorithm to find MSTs efficiently.")

elif example == "Common Elements in Two Arrays":
    st.write("**Problem:** Find common elements in two arrays.")
    array1 = [10, 15, 20, 25, 30]
    array2 = [15, 20, 35, 40]
    st.write("Array 1:", array1)
    st.write("Array 2:", array2)
    common_elements = set(array1) & set(array2)
    st.write("**Common Elements:**", common_elements)

elif example == "Graph Traversal with Set":
    st.write("**Problem:** Use sets to avoid revisiting nodes in a graph traversal.")
    st.write("""
    Graph:  
    Node A connects to B, C  
    Node B connects to D  
    Node C connects to D  
    **Visited Nodes:** {A, B, C, D}  
    **Result:** No cycles detected due to visited set tracking.
    """)

# Section: Interactive Simulations
st.subheader("Interactive Simulations for Set-Based Algorithms")

# Choose Simulation
simulation = st.selectbox(
    "Select an algorithm to simulate:",
    ["Set Intersection for Text Processing", "Subset Problem in Dynamic Programming", "Set Operations in BFS"]
)

if simulation == "Set Intersection for Text Processing":
    st.write("**Problem:** Find the overlap of keywords between two documents.")
    doc1 = {"algorithm", "data", "structure", "hash"}
    doc2 = {"data", "structure", "tree", "graph"}
    st.write("Keywords in Document 1:", doc1)
    st.write("Keywords in Document 2:", doc2)
    overlap = doc1 & doc2
    st.write("**Overlapping Keywords:**", overlap)

elif simulation == "Subset Problem in Dynamic Programming":
    st.write("**Problem:** Can a subset of numbers sum to a target value?")
    numbers = [3, 34, 4, 12, 5, 2]
    target = 9
    st.write("Numbers:", numbers)
    st.write("Target:", target)
    possible_sums = {0}
    for num in numbers:
        possible_sums |= {x + num for x in possible_sums}
    st.write("**Is the Target Achievable?**", target in possible_sums)

elif simulation == "Set Operations in BFS":
    st.write("**Problem:** Explore a graph using BFS without revisiting nodes.")
    graph = {
        "A": {"B", "C"},
        "B": {"D"},
        "C": {"D"},
        "D": set()
    }
    start = "A"
    visited = set()
    queue = [start]

    st.write("**Graph Representation:**")
    st.json(graph)

    st.write("BFS Traversal:")
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            st.write("Visited:", node)
            queue.extend(graph[node] - visited)
            time.sleep(0.5)

# Section: Interactive Challenges
st.subheader("Test Your Understanding")
challenge = st.selectbox(
    "Select a challenge to solve:",
    ["Check Subset Relation", "Simulate Set Operations", "Write a Set-Based Algorithm"]
)

if challenge == "Check Subset Relation":
    st.write("**Challenge:** Determine if Set A is a subset of Set B.")
    set_A = {1, 2, 3}
    set_B = {1, 2, 3, 4, 5}
    st.write("Set A:", set_A)
    st.write("Set B:", set_B)
    st.write("**Is A a subset of B?**", set_A <= set_B)

elif challenge == "Simulate Set Operations":
    st.write("**Challenge:** Perform union, intersection, and difference on sets.")
    set_X = {5, 10, 15}
    set_Y = {10, 20, 30}
    st.write("Set X:", set_X)
    st.write("Set Y:", set_Y)
    st.write("Union:", set_X | set_Y)
    st.write("Intersection:", set_X & set_Y)
    st.write("Difference (X - Y):", set_X - set_Y)

elif challenge == "Write a Set-Based Algorithm":
    st.write("**Challenge:** Implement an algorithm to find unique elements from two arrays.")
    st.write("Try it in your editor or discuss your approach!")
    
