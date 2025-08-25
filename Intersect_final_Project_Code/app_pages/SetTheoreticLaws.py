import streamlit as st

# Set up the Streamlit interface
st.title("📘 Set Theory Laws and Interactive Lessons")

st.header("Learn Set Theory Laws Practically! 💡")
st.write("""
Understanding the basic laws of set theory is essential for solving problems involving sets.  
In this section, we’ll explore these laws step-by-step with examples, clear explanations, and interactive lessons.  
Ready to dive in? 🚀
""")

# Section: Set Theory Laws
st.subheader("Set Identities")
st.write("""
Below is a table of the most common set theory laws. We'll explain and explore these further in the interactive lessons below.
""")

# Laws table
laws = { 
        "Law Name" : [
            "Identity Laws", "Domination Laws", "Idempotent Laws", "Complementation Law", 
            "Commutative Laws", "Associative Laws", "Distributive Laws", "De Morgan's Laws", 
            "Absorption Laws", "Complement Laws"
        ],
        "Mathematical Expression" : [
            "A ∩ U = A and A ∪ ∅ = A", 
            "A ∪ U = U and A ∩ ∅ = ∅",
            "A ∪ A = A and A ∩ A = A",
            "(A')' = A",
            "A ∪ B = B ∪ A and A ∩ B = B ∩ A",
            "A ∪ (B∪C) = (A∪B) ∪ C and A ∩ (B∩C) = (A∩B) ∩ C",
            "A ∪ (B∩C) = (A∪B) ∩ (A∪C) and A ∩ (B∪C) = (A∩B) ∪ (A∩C)",
            "(A ∩ B)' = A' ∪ B' and (A ∪ B)' = A' ∩ B'",
            "A ∪ (A∩B) = A and A ∩ (A∪B) = A",
            "A ∪ A' = U and A ∩ A' = ∅"
        ]
}
st.table(laws)

# Interactive Lessons for Set Theory Laws
st.subheader("Interactive Lessons 📚")

# Identity Laws
st.write("### 1️⃣ Identity Laws")
st.write("""
- These laws describe how a set interacts with the **Universal Set (U)** and the **Empty Set (∅)**.  
- Key Rules:
  - \( A ∩ U = A \): A set intersected with the universal set remains the same.  
  - \( A ∪ ∅ = A \): A set united with the empty set remains the same.  
""")

st.write("Imagine you're sorting fruits into baskets:")
st.write("""
- If \( U \) is the set of all fruits, \( A \) could be a basket of apples, oranges, and bananas. Intersecting \( A \) with \( U \) (all fruits) doesn’t change \( A \).  
- If \( ∅ \) represents no fruits, adding it to \( A \) doesn't change \( A \).
""")

st.subheader("Try This 🧠")
answer = st.radio("What happens when you unite \( A \) with \( ∅ \)?", 
                  options=["The set becomes empty.", "The set remains \( A \).", "The set becomes the universal set (U)."])
if answer == "The set remains \( A \).":
    st.success("✅ Correct! Adding nothing (\( ∅ \)) to a set doesn’t change it.")
else:
    st.error("❌ Incorrect. Adding the empty set doesn't change the original set.")

# Domination Laws
st.write("### 2️⃣ Domination Laws")
st.write("""
- These laws describe the extremes of combining sets with \( U \) and \( ∅ \):  
  - \( A ∪ U = U \): Combining a set with \( U \) always gives \( U \).  
  - \( A ∩ ∅ = ∅ \): Intersecting a set with \( ∅ \) always gives \( ∅ \).
""")

st.write("Imagine you have all the fruits (\( U \)) in a basket and you add apples (\( A \)) to it. The basket still contains \( U \) (all fruits). Similarly, no matter what \( A \) is, if you intersect it with \( ∅ \), you'll end up with an empty basket.")

st.subheader("Try This 🧠")
answer = st.radio("What is \( A ∩ ∅ \)?", 
                  options=["The set \( A \)", "The universal set \( U \)", "The empty set \( ∅ \)."])
if answer == "The empty set \( ∅ \).":
    st.success("✅ Correct! Intersecting with \( ∅ \) always gives \( ∅ \).")
else:
    st.error("❌ Incorrect. Intersecting a set with \( ∅ \) results in no common elements.")

# Idempotent Laws
st.write("### 3️⃣ Idempotent Laws")
st.write("""
- These laws describe what happens when a set is combined with itself:  
  - \( A ∪ A = A \): Adding a set to itself doesn't change it.  
  - \( A ∩ A = A \): Intersecting a set with itself doesn’t change it.  
""")

st.write("If you already have a basket of apples (\( A \)), adding the same apples doesn’t give you more apples—it’s still the same basket.")

st.subheader("Try This 🧠")
answer = st.radio("What is \( A ∪ A \)?", 
                  options=["The set \( A \)", "The empty set \( ∅ \)", "The universal set \( U \)."])
if answer == "The set \( A \)":
    st.success("✅ Correct! Combining \( A \) with itself gives the same set.")
else:
    st.error("❌ Incorrect. Adding a set to itself doesn’t change it.")

# Complement Laws
st.write("### 4️⃣ Complement Laws")
st.write("""
- Complements show how a set interacts with its opposite:  
  - \( A ∪ A' = U \): A set united with its complement gives the universal set.  
  - \( A ∩ A' = ∅ \): A set intersected with its complement gives the empty set.  
""")

st.write("If \( A \) is a basket of apples and \( A' \) is a basket of everything except apples, combining both gives all fruits (\( U \)). But if you try to find what’s common between the two, there’s nothing—they’re opposites.")

st.subheader("Try This 🧠")
answer = st.radio("What is \( A ∪ A' \)?", 
                  options=["The set \( A \)", "The empty set \( ∅ \)", "The universal set \( U \)."])
if answer == "The universal set \( U \).":
    st.success("✅ Correct! Combining a set with its complement always gives \( U \).")
else:
    st.error("❌ Incorrect. A set and its complement together form the universal set.")

# De Morgan's Laws
st.write("### 5️⃣ De Morgan's Laws")
st.write("""
- These laws connect **intersection** and **union** with **complements**:  
  - \( (A ∩ B)' = A' ∪ B' \): The complement of an intersection is the union of the complements.  
  - \( (A ∪ B)' = A' ∩ B' \): The complement of a union is the intersection of the complements.  
""")

st.write("Imagine you're dividing fruits into two baskets, \( A \) and \( B \):")
st.write("""
- If \( A \) is apples, \( B \) is bananas, and \( U \) is all fruits:  
  - \( (A ∩ B)' \) means "everything except apples AND bananas together."  
  - \( A' ∪ B' \) means "everything that’s NOT apples OR NOT bananas."  
Both result in the same set!
""")

st.subheader("Try This 🧠")
answer = st.radio("What is \( (A ∩ B)' \)?", 
                  options=["\( A' ∪ B' \)", "\( A ∪ B \)", "\( A' ∩ B' \)"])
if answer == "\( A' ∪ B' \)":
    st.success("✅ Correct! De Morgan’s Laws state that \( (A ∩ B)' = A' ∪ B' \).")
else:
    st.error("❌ Incorrect. Review De Morgan’s Laws.")

# Absorption Laws
st.write("### 6️⃣ Absorption Laws")
st.write("""
- These laws describe how a set behaves when combined with its subset:  
  - \( A ∪ (A ∩ B) = A \): Adding the intersection of \( A \) and \( B \) to \( A \) doesn’t change \( A \).  
  - \( A ∩ (A ∪ B) = A \): Intersecting \( A \) with the union of \( A \) and \( B \) doesn’t change \( A \).  
""")

st.write("Imagine a fruit basket \( A \) with apples and oranges, and \( B \) with bananas:")
st.write("""
- \( A ∪ (A ∩ B) \) means "all fruits in \( A \) plus any overlap with \( B \)." It’s still just \( A \).  
- \( A ∩ (A ∪ B) \) means "only the part of \( A \) that’s also in \( A \cup B \)." It’s still \( A \).
""")

st.subheader("Try This 🧠")
answer = st.radio("What is \( A ∪ (A ∩ B) \)?", 
                  options=["\( A \)", "\( B \)", "\( A ∩ B \)", "\( U \)"])
if answer == "\( A \)":
    st.success("✅ Correct! Adding the intersection doesn’t change \( A \).")
else:
    st.error("❌ Incorrect. Review the Absorption Laws.")


# Quiz Section
st.header("🎯 Test Your Knowledge")
st.write("""
Now that you’ve learned the basics of set theory laws, let’s test what you’ve understood.  
Answer the following questions:
""")

questions = [
    {"question": "1. What is \( A ∪ ∅ \)?", "options": ["\( A \)", "\( U \)", "\( ∅ \)", "\( A' \)"], "answer": "\( A \)"},
    {"question": "2. What is \( A ∩ A \)?", "options": ["\( A \)", "\( ∅ \)", "\( U \)", "\( A' \)"], "answer": "\( A \)"},
    {"question": "3. What is \( A ∪ A' \)?", "options": ["\( A \)", "\( U \)", "\( ∅ \)", "\( A' \)"], "answer": "\( U \)"},
    {"question": "4. What is \( A ∩ A' \)?", "options": ["\( A \)", "\( ∅ \)", "\( U \)", "\( A' \)"], "answer": "\( ∅ \)"}
]

score = 0
for q in questions:
    user_answer = st.radio(q["question"], q["options"], key=q["question"])
    if user_answer == q["answer"]:
        st.success(f"✅ Correct! {q['answer']} is the right answer.")
        score += 1
    else:
        st.error(f"❌ Incorrect. The correct answer is {q['answer']}.")

st.write(f"🎉 Your total score: {score}/{len(questions)}")
