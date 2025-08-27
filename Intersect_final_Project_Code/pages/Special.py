import streamlit as st

st.title("🌟 Special Sets 🌟")

st.write("""
In this section, we’ll explore three special types of sets with fun examples and interactive questions:  
- 🌎 **Universal Set** - 🌀 **Empty Set** - 🎯 **Singleton Set** Each type is unique, and we’ll discover how they work in both real-life scenarios and mathematics. Let's dive in! 🚀
""")

st.header("📖 __Definitions__")
st.write("""
- **Cardinality**: This is just a fancy word for how many elements a set has.  
  For example, if a set contains {1, 2, 3}, its cardinality is 3 because there are three elements.  
""")

tab1, tab2, tab3 = st.tabs(["🌎 Universal Set", "🌀 Empty Set", "🎯 Singleton Set"])

# Tab for Universal Set
with tab1:
    st.header("🌎 Universal Set")

    st.write("""
A **Universal Set** is like the "big picture." It includes all possible elements related to a certain context or group.  
It’s usually denoted by **Ų**. For example, think about all the flowers in the world—that’s your universal set! Roses, tulips, and sunflowers would then be subsets of this universal set. 🌸🌻🌷  
    """)

    st.image("images/Universal-Set.png", caption="Universal Set containing subsets A and C")

    st.write("""
In the diagram above, even though the 'Heptagon' is not part of sets A or C, it’s still a member of the universal set. 🔺  
    """)

    st.subheader("Complement of a Universal Set")
    st.write("""
Since the universal set includes **everything**, its complement would be an **empty set** (because there’s nothing outside the universal set). The complement is denoted by **Φ** or **{}**.
    """)

    st.subheader("Venn Diagram")
    st.write("""
In a Venn diagram, the universal set is usually shown as a large rectangle that contains all subsets. Smaller circles inside the rectangle represent the subsets.
    """)

    st.subheader("Examples of Universal Sets")
    st.write("""
- The set of **all letters in the English alphabet**: A, B, C, ..., Z.  
- The set of **all students in a school**.  
- The set of **all numbers on a dice (1 to 6)**.  
""")

    # Interactive Questions
    st.subheader("🧠 Test Your Knowledge!")
    
    question_1 = st.radio("1️⃣ Can a universal set have subsets that don’t overlap with each other?", 
                           options=["Yes", "No"], key="universal_q1")
    if question_1 == "Yes":
        st.write("❌ Incorrect. Subsets can be non-overlapping as long as their elements belong to the universal set.")
    elif question_1 == "No":
        st.write("✅ Correct! Subsets can have no common elements but must still belong to the universal set.")
    
    question_2 = st.radio("2️⃣ If the universal set is the set of all pets, which of these is NOT a valid subset?", 
                           options=["Dogs", "Cats", "Unicorns"], key="universal_q2")
    if question_2 == "Dogs" or question_2 == "Cats":
        st.write("❌ Incorrect. Dogs and Cats are valid subsets of the universal set of pets.")
    elif question_2 == "Unicorns":
        st.write("✅ Correct! Unicorns aren’t real, so they wouldn’t belong in this universal set. 🦄")

# Tab for Empty Set
with tab2:
    st.header("🌀 Empty Set")
    
    st.write("""
An **Empty Set** (also called a null set) is a set that has no members. It’s completely empty! It is represented by the symbol '∅' or '{}'.  
For example, if you create a set of all unicorns in your neighborhood, it will be an empty set (because there are no unicorns around). 🦄❌  
    """)

    st.image("images/Empty-Set.png", caption="Example of an Empty Set in a Venn Diagram")

    st.write("""
### Key Points:  
- Its cardinality is **0** (because there are no elements in it).  
- The empty set is a subset of every set.  
    """)

    st.subheader("Examples of Empty Sets")
    st.write("""
- The set of all humans who can fly without any equipment. 🦸‍♂️❌  
- The set of negative numbers greater than 0.  
""")

    # Interactive Questions
    st.subheader("🧠 Test Your Knowledge!")
    
    question_1 = st.radio("1️⃣ Can an empty set ever have a cardinality greater than 0?", 
                           options=["Yes", "No"], key="empty_q1")
    if question_1 == "Yes":
        st.write("❌ Incorrect. An empty set, by definition, has no elements, so its cardinality is always 0.")
    elif question_1 == "No":
        st.write("✅ Correct! An empty set will always have a cardinality of 0.")

    question_2 = st.radio("2️⃣ Which of these is an example of an empty set?", 
                           options=["The set of all even numbers", "The set of flying elephants", "The set of all whole numbers"], 
                           key="empty_q2")
    if question_2 == "The set of all even numbers" or question_2 == "The set of all whole numbers":
        st.write("❌ Incorrect. Even numbers and whole numbers exist, so these are not empty sets.")
    elif question_2 == "The set of flying elephants":
        st.write("✅ Correct! Flying elephants don’t exist, so this is an empty set. 🐘❌")

# Tab for Singleton Set
with tab3:
    st.header("🎯 Singleton Set")
    
    st.write("""
A **Singleton Set** is a set that contains exactly **one element**. Its cardinality is 1.  
For example, if you make a set of your favorite number and it only contains {7}, that’s a singleton set.  
    """)

    st.image("images/Singleton-Set.jpg", caption="Example of a Singleton Set")

    st.write("""
### Key Points:  
- Singleton sets are important because they show the simplest form of a non-empty set.  
- Mathematicians often use singleton sets when dealing with specific values in larger contexts.  
    """)

    st.subheader("Examples of Singleton Sets")
    st.write("""
- The set of the **fastest sprinter in the world**: {Usain Bolt}. 🏃‍♂️  
- The set of the **only person in a room**: {John}. 🧍‍♂️  
- The set of a specific number, like {0}.  
""")

    # Interactive Questions
    st.subheader("🧠 Test Your Knowledge!")
    
    question_1 = st.radio("1️⃣ Can a singleton set contain more than one element?", 
                           options=["Yes", "No"], key="singleton_q1")
    if question_1 == "Yes":
        st.write("❌ Incorrect. A singleton set, by definition, can only contain one element.")
    elif question_1 == "No":
        st.write("✅ Correct! Singleton sets only have one element.")

    question_2 = st.radio("2️⃣ Which of these is a singleton set?", 
                           options=["{0}", "{1, 2}", "{}"], key="singleton_q2")
    if question_2 == "{1, 2}" or question_2 == "{}":
        st.write("❌ Incorrect. {1, 2} has more than one element, and {} is an empty set.")
    elif question_2 == "{0}":
        st.write("✅ Correct! {0} is a singleton set because it has exactly one element.")