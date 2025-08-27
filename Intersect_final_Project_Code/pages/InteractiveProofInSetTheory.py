import streamlit as st

# Title and Introduction
st.title("Interactive Set Proofs")
st.write(
    """
    Welcome to the Interactive Set Proofs module! 
    Dive into set theory concepts through **membership tables** and **set builder notation**. 
    Practice solving proofs, verifying results, and expanding your understanding of set theory.
    """
)

# Sidebar Navigation
st.sidebar.title("Topics")
topic = st.sidebar.radio(
    "Choose a topic to explore:", ["Membership Tables", "Set Builder Notation"]
)

# Membership Tables Section
if topic == "Membership Tables":
    st.header("Membership Tables Practice")
    st.write(
        """
        Membership tables help verify set-theoretic proofs by analyzing the relationship 
        between elements and their sets. Complete the challenges below to test your knowledge!
        """
    )

    # Example 1: Prove A ∩ B ⊆ A
    st.subheader("Challenge 1: Prove A ∩ B ⊆ A")
    st.write("Here’s a membership table that breaks down the proof:")
    st.table(
        {
            "x": ["x ∈ A", "x ∈ B", "x ∈ A ∩ B", "x ∈ A ∩ B ⊆ A"],
            "Example 1": ["True", "True", "True", "True"],
            "Example 2": ["True", "False", "False", "True"],
            "Example 3": ["False", "True", "False", "True"],
        }
    )
    proof = st.radio(
        "Based on the table, does the proof hold?", 
        ["Yes, the proof holds.", "No, the proof does not hold."]
    )
    if st.button("Submit Proof", key="membership_1"):
        if proof == "Yes, the proof holds.":
            st.success("Correct! Every x in A ∩ B is also in A by definition of intersection.")
        else:
            st.error("Incorrect. Revisit the membership table to understand why.")

    # Example 2: Prove A ⊆ A ∪ B
    st.subheader("Challenge 2: Prove A ⊆ A ∪ B")
    st.write("Analyze the following membership table:")
    st.table(
        {
            "x": ["x ∈ A", "x ∈ B", "x ∈ A ∪ B", "x ∈ A ⊆ A ∪ B"],
            "Example 1": ["True", "True", "True", "True"],
            "Example 2": ["True", "False", "True", "True"],
            "Example 3": ["False", "True", "True", "True"],
        }
    )
    proof_2 = st.radio(
        "Does this proof hold?", 
        ["Yes, it holds.", "No, it doesn't hold."],
        key="membership_2"
    )
    if st.button("Submit Proof", key="membership_2_submit"):
        if proof_2 == "Yes, it holds.":
            st.success("Well done! Every x in A is also in A ∪ B, satisfying the union property.")
        else:
            st.error("Incorrect. Recall that union includes all elements of A and B.")
            
    # Example 3: Prove A ⊆ U
    st.subheader("Challenge 3: Prove A ⊆ U")
    st.write("Check the following membership table for the proof:")
    st.table(
        {
            "x": ["x ∈ A", "x ∈ U", "x ∈ A ⊆ U"],
            "Example 1": ["True", "True", "True"],
            "Example 2": ["False", "True", "True"],
        }
    )
    proof_3 = st.radio(
        "Is the proof valid?", 
        ["Yes, it's valid.", "No, it's not valid."],
        key="membership_3"
    )
    if st.button("Submit Proof", key="membership_3_submit"):
        if proof_3 == "Yes, it's valid.":
            st.success("Correct! By definition, every set A is a subset of the universal set U.")
        else:
            st.error("Incorrect. Recall that U contains all elements.")

    # Example 4: Prove ∅ ⊆ A
    st.subheader("Challenge 4: Prove ∅ ⊆ A")
    st.write("Review this membership table:")
    st.table(
        {
            "x": ["x ∈ ∅", "x ∈ A", "x ∈ ∅ ⊆ A"],
            "Example 1": ["False", "True", "True"],
            "Example 2": ["False", "False", "True"],
        }
    )
    proof_4 = st.radio(
        "Does the proof hold?", 
        ["Yes, the proof holds.", "No, the proof doesn't hold."],
        key="membership_4"
    )
    if st.button("Submit Proof", key="membership_4_submit"):
        if proof_4 == "Yes, the proof holds.":
            st.success("Well done! The empty set is a subset of every set, including A.")
        else:
            st.error("Incorrect. Remember, ∅ contains no elements, so it’s always a subset.")

    # Example 5: Prove A ∩ ∅ = ∅
    st.subheader("Challenge 5: Prove A ∩ ∅ = ∅")
    st.write("Analyze the membership table below:")
    st.table(
        {
            "x": ["x ∈ A", "x ∈ ∅", "x ∈ A ∩ ∅", "x ∈ A ∩ ∅ = ∅"],
            "Example 1": ["True", "False", "False", "True"],
            "Example 2": ["False", "False", "False", "True"],
        }
    )
    proof_5 = st.radio(
        "Is the proof correct?", 
        ["Yes, it's correct.", "No, it's not correct."],
        key="membership_5"
    )
    if st.button("Submit Proof", key="membership_5_submit"):
        if proof_5 == "Yes, it's correct.":
            st.success("Correct! The intersection of any set with ∅ is always ∅, as there are no shared elements.")
        else:
            st.error("Incorrect. Remember, ∅ has no elements to intersect with.")

# Set Builder Notation Section
elif topic == "Set Builder Notation":
    st.header("Set Builder Notation Practice")
    st.write(
        """
        Set builder notation is a powerful way to describe sets using a logical condition. 
        Complete the challenges below to master this skill!
        """
    )

    # Example 1: Recognizing Sets
    st.subheader("Challenge 1: Identify the Set")
    st.write(
        "Which of the following correctly represents the set of positive even integers?"
    )
    options = [
        "{x | x is an integer and x > 0 and x % 2 == 0}",
        "{x | x is a natural number and x % 2 == 0}",
        "{x | x is an integer and x < 0}",
        "{x | x is an odd integer}",
    ]
    answer = st.radio("Choose your answer:", options)
    if st.button("Submit Answer", key="set_builder_1"):
        if answer == options[0]:
            st.success(
                "Correct! This set includes all integers greater than 0 that are divisible by 2."
            )
        else:
            st.error("Incorrect. Review the logical conditions in set builder notation.")

    # Example 2: Writing Sets
    st.subheader("Challenge 2: Write the Set")
    st.write("Write a set in builder notation for all x such that x is a real number and x^2 = 4.")
    user_input = st.text_input("Enter your set builder notation:", key="set_builder_2")
    if st.button("Submit Set", key="set_builder_2_submit"):
        if user_input.strip() == "{x | x is a real number and x^2 = 4}" or user_input.strip() == "{x | x ∈ R and x^2 = 4}":
            st.success("Great job! That’s the correct set.")
        else:
            st.error(
                "Not quite. Remember to include all conditions: x is a real number, and x^2 = 4, and put a space between each character so I can read it clearly!"
            )

    # Example 3: Prove Equality
    st.subheader("Challenge 3: Prove Set Equality")
    st.write(
        """
        Prove: {x | x > 0} ∪ {x | x < 0} = {x | x is a real number and x != 0}. 
        Write your reasoning below.
        """
    )
    reasoning = st.text_area("Write your proof here:", key="set_builder_3")
    if st.button("Submit Proof", key="set_builder_3_submit"):
        if "union" in reasoning.lower() and "real number" in reasoning.lower():
            st.success("Good proof! You correctly identified the role of union in this context.")
        else:
            st.error(
                "Your proof needs more detail. Focus on explaining how union covers all non-zero real numbers."
            )
    
    # Example 4: Set Notation for Primes
    st.subheader("Challenge 4: Identify the Prime Numbers")
    st.write(
        "Which of the following represents the set of all prime numbers greater than 10?"
    )
    options_4 = [
        "{x | x is a prime number and x > 10}",
        "{x | x is an integer and x is divisible by only 1 and itself}",
        "{x | x is greater than 10 and even}",
        "{x | x is a prime number and x ≤ 10}",
    ]
    answer_4 = st.radio("Choose your answer:", options_4)
    if st.button("Submit Answer", key="set_builder_4"):
        if answer_4 == options_4[0]:
            st.success("Correct! This set includes all prime numbers greater than 10.")
        else:
            st.error("Incorrect. Remember that prime numbers are divisible only by 1 and themselves.")

    # Example 5: Writing a Set for Negative Numbers
    st.subheader("Challenge 5: Write the Set for Negative Numbers")
    st.write("Write the set in builder notation for all x such that x is a negative integer.")
    user_input_5 = st.text_input("Enter your set builder notation:", key="set_builder_5")
    if st.button("Submit Set", key="set_builder_5_submit"):
        if user_input_5.strip() == "{x | x is an integer and x < 0}" or user_input_5.strip() == "{x | x ∈ Z and x < 0}":
            st.success("Well done! That's the correct set notation for negative integers.")
        else:
            st.error(
                "Not quite. Make sure you include that x is an integer and that x is less than 0."
            )

st.write(" ")
# BONUS SECTION (SINCE ABSORPTION LAW PROOF IS TRICKY)
st.subheader("_Bonus Section_", divider = "green")
laws = ["-", "Identity Laws",
            "Domination Laws",
            "Idempotent Laws",
            "Complementation Law or Involution Law",
            "Commutative Laws",
            "Associative Laws",
            "Distributive Laws",
            "De Morgan's Laws",
            "Absorption Laws",
            "Complement laws"]

def definition_of_dual():
    st.write(" ")
    st.write("Now that you've made it this far, we can trust you with a secret...")
    st.subheader("Duals", divider = "blue")
    st.write("A dual of an expression is gotten by replacing a U with a ∅, a ∩ with a ∪, and vice versa")
    st.write("After you've tried writing out the proof for the first absorption law, find the duals of all the steps...")
    st.write("What did you notice?")
    st.write("This gives you the proof for the second absorption law!")
    st.write("A lot of proofs can be found this way...")
    st.write("How did the laws change when you used the dual trick 👀?")

# Proving the first Absorption Law
st.write("Let's prove the first Absorption Law: A ∪ (A ∩ B) = A")
st.write("If you know the steps, then I assume you know the laws for each step...")
st.write("So this is what I will be testing you on instead.")
st.write("")
st.write("We will start with the premise: A ∪ (A ∩ B)")

app_selection = st.selectbox("📌 Which laws are used for the first step?", laws)
if app_selection == "Identity Laws":
    st.success("Correct!")
    app_selection = st.selectbox("📌 Which laws are used for the second step?", laws)
    if app_selection == "Distributive Laws":
        st.success("Correct!")
        app_selection = st.selectbox("📌 Now for the third?", laws)
        if app_selection == "Domination Laws":
            st.success("Correct!")
            app_selection = st.selectbox("📌 And the last...", laws)
            if app_selection == "Identity Laws":
                st.success("Correct!")
                st.write(" = A")
                st.write("We now have our final term! 🥳")
                definition_of_dual()
            else:
               st.error("Think of how to simplify to a single term") 
        else:
            st.error("Think of what could go away within the parentheses()")
    else:
        st.error("Think of a common factor 🤷")
else:
    st.error("Think of how to get an even number of terms.")

# Fun and Educational Sidebar
st.sidebar.title("Fun Facts")
st.sidebar.write("💡 Did you know?")
st.sidebar.write("Set theory was introduced by German mathematician Georg Cantor in the late 19th century!")
st.sidebar.write("Sets are used in artificial intelligence to represent knowledge and reasoning.")
st.sidebar.write("The empty set is represented by ∅ and has no elements.")
st.sidebar.write("Set operations like union and intersection are similar to logical operations in programming.")
st.sidebar.write("The power set of a set contains all possible subsets, including the empty set and the set itself.")

st.sidebar.title("Tips")
st.sidebar.write("- Break down complex sets into smaller parts for better understanding.")
st.sidebar.write("- Use set-builder notation to describe infinite sets concisely.")
st.sidebar.write("- Solve membership table exercises to understand proofs more deeply.")
st.sidebar.write("- When working with large sets, organize elements in categories.")
st.sidebar.write("- Relate set operations to real-life examples, like sorting and categorizing objects.")