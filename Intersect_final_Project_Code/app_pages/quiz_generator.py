import streamlit as st


# Sample questions stored in dictionaries
questions = {
    "Basics": [
        {"question": "What is a set?", "options": ["A collection of items", "A single item", "A number"], 
         "answer": "A collection of items", "feedback": "A set is defined as a collection of distinct objects."},
        {"question": "Is {1, 2, 3} equal to {3, 2, 1}?", "options": ["Yes", "No"], 
         "answer": "Yes", "feedback": "Sets are unordered, so {1, 2, 3} is equal to {3, 2, 1}."},
        {"question": "What is the cardinality of the set {a, b, c}?", "options": ["1", "2", "3"], 
         "answer": "3", "feedback": "Cardinality is the number of elements in the set."},
        {"question": "What symbol represents the universal set?", "options": ["∅", "U", "A"], 
         "answer": "U", "feedback": "The universal set is typically denoted by U."},
        {"question": "Which of these is a singleton set?", "options": ["{1, 2}", "{1}", "{}"], 
         "answer": "{1}", "feedback": "A singleton set has exactly one element."},
        {"question": "What is an empty set?", "options": ["A set with one element", "A set with no elements", "All sets"], 
         "answer": "A set with no elements", "feedback": "An empty set contains no elements and is denoted by ∅."},
        {"question": "What does A ∩ B represent?", "options": ["Union", "Intersection", "Difference"], 
         "answer": "Intersection", "feedback": "The intersection of A and B includes elements in both sets."},
        {"question": "What does A ∪ B mean?", "options": ["All elements in A and B", "Only common elements", "Elements unique to A"], 
         "answer": "All elements in A and B", "feedback": "The union of A and B includes all elements from both sets."},
        {"question": "What is the complement of a universal set?", "options": ["The empty set", "The set itself", "None of these"], 
         "answer": "The empty set", "feedback": "The complement of a universal set is ∅ because there's nothing outside U."},
        {"question": "Is the empty set a subset of every set?", "options": ["Yes", "No"], 
         "answer": "Yes", "feedback": "The empty set is a subset of every set because it contains no elements."}
    ],
    "Operations": [
        {"question": "What is the union of {1, 2} and {2, 3}?", "options": ["{1, 2, 3}", "{2}", "{1, 3}"],
         "answer": "{1, 2, 3}", "feedback": "The union of two sets is a set containing all elements from both sets."},
        {"question": "What is the intersection of {1, 2, 3} and {2, 3, 4}?", "options": ["{2, 3}", "{1, 4}", "{1, 2, 3, 4}"],
         "answer": "{2, 3}", "feedback": "The intersection contains elements present in both sets."},
        {"question": "What is the difference of {1, 2, 3} - {2}?", "options": ["{1, 3}", "{2, 3}", "{1, 2}"],
         "answer": "{1, 3}", "feedback": "The difference removes elements in the second set from the first."},
        {"question": "What is the power set of {1}?", "options": ["∅", "{∅, {1}}", "{1}"],
         "answer": "{∅, {1}}", "feedback": "The power set contains all subsets, including ∅ and the set itself."},
        {"question": "What is the Cartesian product of {1} and {2, 3}?", "options": ["{(1, 2), (1, 3)}", "{1, 2, 3}", "{(2, 1), (3, 1)}"],
         "answer": "{(1, 2), (1, 3)}", "feedback": "The Cartesian product pairs each element of the first set with the second."},
        {"question": "What is A ∩ ∅?", "options": ["∅", "A", "U"],
         "answer": "∅", "feedback": "A set intersected with ∅ is always empty."},
        {"question": "What is A ∪ A?", "options": ["A", "∅", "U"],
         "answer": "A", "feedback": "The union of a set with itself is the set itself."},
        {"question": "What is the cardinality of P({1, 2})?", "options": ["2", "4", "3"],
         "answer": "4", "feedback": "If a set has n elements, its power set has 2^n subsets."},
        {"question": "Which law states A ∪ (A ∩ B) = A?", "options": ["Absorption Law", "De Morgan's Law", "Distributive Law"],
         "answer": "Absorption Law", "feedback": "Absorption Law simplifies expressions using unions and intersections."},
        {"question": "What is (A ∪ B)'?", "options": ["A' ∩ B'", "A' ∪ B'", "∅"],
         "answer": "A' ∩ B'", "feedback": "De Morgan's Law states that the complement of a union is the intersection of complements."}
    ],
    "Set Theoretic Laws": [
    {"question": "What does A ∩ U equal?", "options": ["A", "U", "∅", "A'"], 
     "answer": "A", "feedback": "Identity Law: A set intersected with the universal set remains unchanged."},
    {"question": "What does A ∪ ∅ equal?", "options": ["A", "∅", "U", "A'"], 
     "answer": "A", "feedback": "Identity Law: Adding the empty set to a set doesn’t change the set."},
    {"question": "What does A ∪ U equal?", "options": ["A", "∅", "U", "A'"], 
     "answer": "U", "feedback": "Domination Law: The union of any set with the universal set is the universal set."},
    {"question": "What is the complement of A ∩ B?", "options": ["A' ∪ B'", "A' ∩ B'", "A ∪ B", "U"], 
     "answer": "A' ∪ B'", "feedback": "De Morgan’s Law: The complement of an intersection is the union of the complements."},
    {"question": "What does (A ∪ B)' equal?", "options": ["A' ∩ B'", "A' ∪ B'", "A ∩ B", "∅"], 
     "answer": "A' ∩ B'", "feedback": "De Morgan’s Law: The complement of a union is the intersection of the complements."},
    {"question": "What does A ∪ A' equal?", "options": ["U", "∅", "A", "B"], 
     "answer": "U", "feedback": "Complement Law: A set united with its complement equals the universal set."},
    {"question": "What does A ∩ A' equal?", "options": ["U", "∅", "A", "A'"], 
     "answer": "∅", "feedback": "Complement Law: A set intersected with its complement equals the empty set."},
    {"question": "Which law states A ∪ (A ∩ B) = A?", "options": ["Absorption Law", "Identity Law", "Distributive Law", "De Morgan's Law"], 
     "answer": "Absorption Law", "feedback": "Absorption Law simplifies expressions with intersections and unions."},
    {"question": "What does A ∩ (A ∪ B) equal?", "options": ["A", "B", "A ∪ B", "∅"], 
     "answer": "A", "feedback": "Absorption Law: A set intersected with its union doesn’t change."},
    {"question": "What is (A')' equal to?", "options": ["A", "A'", "∅", "U"], 
     "answer": "A", "feedback": "Complementation Law: The double complement of a set equals the original set."}
     ],
     "Set Relations": [
    {"question": "What does A ⊆ B mean?", "options": ["A is a subset of B", "A is a superset of B", "A and B are equal", "A ∩ B = ∅"], 
     "answer": "A is a subset of B", "feedback": "Subset relation: All elements of A are contained in B."},
    {"question": "What does A ⊇ B mean?", "options": ["A is a superset of B", "A is a subset of B", "A ∩ B = ∅", "A = B"], 
     "answer": "A is a superset of B", "feedback": "Superset relation: All elements of B are contained in A."},
    {"question": "If A and B are disjoint, what is A ∩ B?", "options": ["∅", "U", "A", "B"], 
     "answer": "∅", "feedback": "Disjoint sets have no common elements, so their intersection is ∅."},
    {"question": "Which diagram represents subsets?", "options": ["Venn Diagram", "Bar Chart", "Scatter Plot", "Pie Chart"], 
     "answer": "Venn Diagram", "feedback": "Venn diagrams are used to visually represent subset relationships."},
    {"question": "What does A = B mean?", "options": ["A and B have the same elements", "A is larger than B", "B is a subset of A", "A ∩ B = ∅"], 
     "answer": "A and B have the same elements", "feedback": "Equality means both sets have exactly the same elements."},
    {"question": "What is A - B?", "options": ["Elements in A but not in B", "Elements in B but not in A", "A ∩ B", "A ∪ B"], 
     "answer": "Elements in A but not in B", "feedback": "Set difference removes elements of B from A."},
    {"question": "What does A ∩ B represent?", "options": ["Common elements of A and B", "Union of A and B", "Difference of A and B", "A ⊆ B"], 
     "answer": "Common elements of A and B", "feedback": "Intersection represents elements present in both sets."},
    {"question": "What does A ∪ B represent?", "options": ["All elements in A and B", "Only common elements", "Difference of A and B", "A ⊆ B"], 
     "answer": "All elements in A and B", "feedback": "Union combines all elements from both sets."},
    {"question": "Which of these is a superset of {1, 2}?", "options": ["{1, 2, 3}", "{1}", "{}", "∅"], 
     "answer": "{1, 2, 3}", "feedback": "A superset contains all elements of the smaller set."},
    {"question": "If A ⊂ B, is A equal to B?", "options": ["No", "Yes"], 
     "answer": "No", "feedback": "A proper subset (⊂) means A is smaller than B."}
     ],
     "Special Sets": [
    {"question": "What is the cardinality of the empty set?", "options": ["0", "1", "∞"], 
     "answer": "0", "feedback": "The empty set contains no elements, so its cardinality is 0."},
    {"question": "What is a singleton set?", "options": ["A set with one element", "A set with no elements", "A universal set"], 
     "answer": "A set with one element", "feedback": "A singleton set contains exactly one element."},
    {"question": "What symbol represents the universal set?", "options": ["U", "∅", "{}"], 
     "answer": "U", "feedback": "The universal set is represented by U."},
    {"question": "Which of these is an empty set?", "options": ["{1}", "{}", "{a, b}"], 
     "answer": "{}", "feedback": "An empty set contains no elements and is denoted by {} or ∅."},
    {"question": "Is the empty set a subset of every set?", "options": ["Yes", "No"], 
     "answer": "Yes", "feedback": "The empty set is a subset of every set because it contains no elements."},
    {"question": "Which of these is a universal set for letters?", "options": ["{a, b, c}", "All letters A-Z", "{}"], 
     "answer": "All letters A-Z", "feedback": "The universal set for letters contains every letter from A to Z."},
    {"question": "What is the complement of the universal set?", "options": ["∅", "U", "{}"], 
     "answer": "∅", "feedback": "The complement of the universal set is ∅ because nothing exists outside it."},
    {"question": "What is the cardinality of the singleton set {a}?", "options": ["0", "1", "2"], 
     "answer": "1", "feedback": "The cardinality of a singleton set is always 1."},
    {"question": "Which set is the subset of every set?", "options": ["∅", "U", "{a}"], 
     "answer": "∅", "feedback": "The empty set is a subset of every set."},
    {"question": "Is the universal set finite or infinite?", "options": ["It depends", "Finite", "Infinite"], 
     "answer": "It depends", "feedback": "The universal set can be finite (e.g., numbers 1-10) or infinite (all numbers)."}
     ],
     "Applications of Sets": [
    {
        "question": "How do social media platforms recommend mutual friends?",
        "options": ["Using the union of friend sets", "Using the intersection of friend sets", "Using the difference of friend sets"],
        "answer": "Using the intersection of friend sets",
        "feedback": "Social media platforms recommend mutual friends by finding the intersection of friend sets."
    },
    {
        "question": "What set operation helps identify common availability in schedules?",
        "options": ["Union", "Intersection", "Difference"],
        "answer": "Intersection",
        "feedback": "The intersection of schedules shows the common availability between people."
    },
    {
        "question": "Which set operation is used to recommend items in e-commerce platforms?",
        "options": ["Union", "Difference", "Intersection"],
        "answer": "Union",
        "feedback": "E-commerce platforms use the union of viewed products to recommend similar or complementary items."
    },
    {
        "question": "How do doctors identify common symptoms among patients?",
        "options": ["Using the union of symptom sets", "Using the intersection of symptom sets", "Using the difference of symptom sets"],
        "answer": "Using the intersection of symptom sets",
        "feedback": "Doctors use the intersection of symptoms to narrow down diagnoses."
    },
    {
        "question": "Which of these is an example of using sets in data analysis?",
        "options": ["Merging datasets to combine records","Finding items unique to one dataset","Both of the above"],
        "answer": "Both of the above",
        "feedback": "Set operations like union and difference help merge datasets and filter out unique data points."
    }
    ],
    "Mock Exam": [
    # Basics
    {
        "question": "Is {{1, 2, 3}} a valid representation of a set?",
        "options": ["Yes", "No"],
        "answer": "No",
        "feedback": "Sets are represented with curly braces: {1, 2, 3}, not double curly braces."
    },
    {
        "question": "What is the cardinality of P({a, b})?",
        "options": ["2", "4", "8"],
        "answer": "4",
        "feedback": "The power set contains 2^n subsets, where n is the number of elements in the set."
    },
    {
        "question": "Which of these is NOT a set?",
        "options": ["{a, b, c}", "{1, 2, 2}", "{∅}"],
        "answer": "{1, 2, 2}",
        "feedback": "Sets cannot have duplicate elements. {1, 2, 2} is invalid."
    },
    {
        "question": "Is the empty set a subset of itself?",
        "options": ["Yes", "No"],
        "answer": "Yes",
        "feedback": "Every set, including the empty set, is a subset of itself."
    },

    # Operations
    {
        "question": "What is A ∩ ∅ for any set A?",
        "options": ["A", "U", "∅"],
        "answer": "∅",
        "feedback": "The intersection of any set with ∅ is always ∅ because they share no elements."
    },
    {
        "question": "What is the Cartesian product of {1} and {∅}?",
        "options": ["∅", "{(1, ∅)}", "{∅, 1}"],
        "answer": "{(1, ∅)}",
        "feedback": "The Cartesian product pairs each element of the first set with every element of the second set."
    },
    {
        "question": "What is the difference {1, 2, 3} - {3, 4}?",
        "options": ["{1, 2, 3}", "{1, 2}", "{3}"],
        "answer": "{1, 2}",
        "feedback": "The difference removes elements in the second set from the first."
    },
    {
        "question": "What is the power set of ∅?",
        "options": ["∅", "{∅}", "{{∅}}"],
        "answer": "{∅}",
        "feedback": "The power set of ∅ contains only the empty set: {∅}."
    },

    # Set Theoretic Laws
    {
        "question": "Which law states (A ∪ B)' = A' ∩ B'?",
        "options": ["De Morgan's Law", "Identity Law", "Complement Law"],
        "answer": "De Morgan's Law",
        "feedback": "De Morgan's Law connects the complement of unions and intersections."
    },
    {
        "question": "What does A ∪ A' equal?",
        "options": ["A", "∅", "U"],
        "answer": "U",
        "feedback": "The union of a set with its complement equals the universal set."
    },
    {
        "question": "Which law states A ∩ (A ∪ B) = A?",
        "options": ["Absorption Law", "Domination Law", "Distributive Law"],
        "answer": "Absorption Law",
        "feedback": "The Absorption Law simplifies expressions involving unions and intersections."
    },

    # Set Relations
    {
        "question": "If A ⊆ B and B ⊆ A, what can we conclude?",
        "options": ["A = B", "A ⊂ B", "A ∩ B = ∅"],
        "answer": "A = B",
        "feedback": "If two sets are subsets of each other, they are equal."
    },
    {
        "question": "What is A - (A ∩ B)?",
        "options": ["A ∪ B", "A - B", "B - A"],
        "answer": "A - B",
        "feedback": "The difference removes the intersection elements of B from A."
    },
    {
        "question": "If A and B are disjoint, what is A ∪ B?",
        "options": ["A", "B", "A + B"],
        "answer": "A + B",
        "feedback": "Disjoint sets have no overlap, so their union combines all their elements."
    },

    # Special Sets
    {
        "question": "What is the complement of the universal set?",
        "options": ["∅", "U", "{}"],
        "answer": "∅",
        "feedback": "The complement of the universal set is ∅ because nothing exists outside it."
    },
    {
        "question": "Is the singleton set {∅} the same as ∅?",
        "options": ["Yes", "No"],
        "answer": "No",
        "feedback": "The singleton set {∅} contains one element, the empty set, while ∅ is empty."
    },
    {
        "question": "What is the cardinality of the universal set for all numbers?",
        "options": ["Infinite", "Finite", "Undefined"],
        "answer": "Infinite",
        "feedback": "The universal set for all numbers is infinite because numbers have no end."
    },

    # Applications
    {
        "question": "How are mutual friends suggested in social media platforms?",
        "options": ["Using the union of friend sets", "Using the intersection of friend sets", "Using the difference of friend sets"],
        "answer": "Using the intersection of friend sets",
        "feedback": "The intersection identifies mutual friends between two users."
    },
    {
        "question": "Which set operation helps identify common symptoms among patients?",
        "options": ["Union", "Intersection", "Difference"],
        "answer": "Intersection",
        "feedback": "The intersection of symptoms identifies common traits for diagnosis."
    },
    {
        "question": "What is the result of finding the intersection of two disjoint schedules?",
        "options": ["Empty set", "Universal set", "Schedule union"],
        "answer": "Empty set",
        "feedback": "Disjoint schedules have no common availability, so their intersection is ∅."
    }
]


}

def Quiz_module():
    st.title("🎓Set Theory Quiz Generator!")

    # Step 1: Topic Selection
    topic = st.selectbox("Select a topic", list(questions.keys()))
    
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False

    if st.button("Start Quiz") or st.session_state.quiz_started:
        st.session_state.quiz_started = True

        # Prepare the question pool based on selected topic
        question_pool = questions[topic]

        # Initialize session state variables for quiz
        if "question_pool" not in st.session_state:
            st.session_state.question_pool = question_pool
            st.session_state.score = 0
            st.session_state.answers = [None] * len(question_pool)  # Initialize answers without pre-selection

        # Display all questions on one page
        display_all_questions()

def display_all_questions():
    st.write("Answer all questions below and then submit your answers.")

    # Loop through each question and display it
    for idx, question in enumerate(st.session_state.question_pool):
        st.write(f"**Question {idx + 1}:** {question['question']}")
        selected_option = st.radio("Options:", question["options"], key=f"q{idx}", index=0)  # No default selection
        
        # Store the answer selected by the user
        st.session_state.answers[idx] = selected_option

    # Submit all answers at once
    if st.button("Submit All Answers"):
        evaluate_quiz()

def evaluate_quiz():
    st.session_state.score = 0  # Reset score for each submission

    # Check answers and provide feedback for each question
    for idx, question in enumerate(st.session_state.question_pool):
        user_answer = st.session_state.answers[idx]
        if user_answer == question["answer"]:
            st.session_state.score += 1
            st.success(f"Question {idx + 1}: Correct! {question['feedback']}")
        else:
            st.error(f"Question {idx + 1}: Incorrect! {question['feedback']}")

    # Display final score
    st.write(f"Your final score: {st.session_state.score}/{len(st.session_state.question_pool)}")

    # Streamlit button to reload the page and clear session state
    if st.button("Take Another Quiz"):
        clear_quiz_state()
        st.markdown("<script>window.location.reload();</script>", unsafe_allow_html=True)

def clear_quiz_state():
    # Clear all quiz-related session state variables
    for key in ["quiz_started", "question_pool", "score", "answers"]:
        if key in st.session_state:
            del st.session_state[key]

# Run the app
Quiz_module()
