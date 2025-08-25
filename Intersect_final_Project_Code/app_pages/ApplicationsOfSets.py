import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

# Set up the Streamlit interface
st.title("Applications of Sets")
st.header("Discover Real-Life Applications of Set Theory!")

st.write("""
Set Theory is not just about math—it’s everywhere in our daily lives!  
Explore how sets are applied in fields like technology, business, healthcare, and even your social media feeds.
""")

# Section: Applications
st.subheader("Real-Life Applications")

applications = {
    "Social Media": "Social media platforms use sets to recommend friends or followers by identifying mutual connections (intersection of sets).",
    "E-Commerce": "E-commerce websites use sets to analyze customer preferences (union of products viewed) and recommend items (difference between preferences).",
    "Healthcare": "In healthcare, sets help identify common symptoms among patients to diagnose diseases (intersection of symptoms).",
    "Data Analysis": "Set operations are used to merge datasets, find common data points, or filter out duplicates.",
    "Scheduling": "Set operations help identify common free slots in schedules (intersection) for effective time management.",
    "Networking": "In computer networks, sets model devices, connections, and data sharing pathways."
}

# Display applications in an interactive format
for app, desc in applications.items():
    with st.expander(f"📌 {app}"):
        st.write(desc)

# Section: Visualization Examples
st.subheader("Visualizing Real-Life Examples")

# Example: Social Media Mutual Friends
st.write("### Example: Social Media Mutual Friends")
set_A = {"Alice", "Bob", "Charlie", "Diana"}
set_B = {"Charlie", "Diana", "Edward", "Fiona"}

st.write("**Set A**: Friends of User 1")
st.write(set_A)
st.write("**Set B**: Friends of User 2")
st.write(set_B)

if st.button("Show Venn Diagram"):
    plt.figure(figsize=(5, 5))
    venn = venn2([set_A, set_B], ("User 1's Friends", "User 2's Friends"))
    venn.get_label_by_id('10').set_text(', '.join(set_A - set_B))
    venn.get_label_by_id('01').set_text(', '.join(set_B - set_A))
    venn.get_label_by_id('11').set_text(', '.join(set_A & set_B))
    st.pyplot(plt)

# Example: Scheduling Common Free Slots
st.write("### Example: Scheduling Common Free Slots")
free_slots_A = {"Monday 2 PM", "Tuesday 10 AM", "Wednesday 1 PM"}
free_slots_B = {"Tuesday 10 AM", "Wednesday 1 PM", "Friday 3 PM"}

st.write("**Person A's Free Slots**")
st.write(free_slots_A)
st.write("**Person B's Free Slots**")
st.write(free_slots_B)

if st.button("Show Common Slots"):
    st.write(f"**Common Slots (Intersection):** {free_slots_A & free_slots_B}")

# Section: Interactive Activities
st.subheader("Interactive Activities")

st.write("Now, let’s explore more real-life examples interactively!")

# Dropdown for selecting an application
app_selection = st.selectbox("Choose an application to learn more:", list(applications.keys()))

if app_selection == "Social Media":
    st.write("Social media platforms suggest mutual friends by finding intersections of friend sets.")
    st.write("**Try visualizing your friends' networks using set operations!**")
elif app_selection == "E-Commerce":
    st.write("E-commerce platforms analyze your browsing history to recommend items.")
    st.write("Union and difference of sets help identify complementary products.")
elif app_selection == "Healthcare":
    st.write("Doctors identify common symptoms across patients using intersections of sets.")
    st.write("This helps narrow down potential diagnoses.")
elif app_selection == "Data Analysis":
    st.write("Data analysts use set operations to merge and filter datasets.")
    st.write("For example, the union of two datasets combines their records.")
elif app_selection == "Scheduling":
    st.write("Intersection of schedules helps find common availability.")
    st.write("Efficient scheduling depends on this principle.")
elif app_selection == "Networking":
    st.write("Computer networks model connections using sets.")
    st.write("Set operations help optimize routing and data transfer.")

# Fun Fact Section
st.subheader("Fun Facts About Sets")
st.write("""
- The concept of sets dates back to the 1870s, developed by German mathematician **Georg Cantor**.  
- Set Theory is the foundation of **modern mathematics**, including probability (and statistics), algebra, and computer science.  
- In real life, even your Netflix recommendations are based on analyzing your **viewing history (sets)**!
""")

# Conclusion
st.write("""
Set Theory is a powerful tool that connects mathematics to the real world in surprising ways.  
Keep exploring, and you’ll see sets in action all around you!
""")