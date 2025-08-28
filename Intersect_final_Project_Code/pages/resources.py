import streamlit as st
from pathlib import Path

# Get the directory of the current script (e.g., '/pages')
pages_dir = Path(__file__).parent

# Get the root directory of the project (go up one level from 'pages')
root_dir = pages_dir.parent

# Page title
st.title("Resource Page for Set Theory")

# Description
st.write("Explore external resources to deepen your understanding of Set Theory. Use the categorized links below for videos, slides, and visuals.")

# YouTube Videos Section
st.header("YouTube Videos")
st.write("Expand your learning with curated videos from trusted sources.")

# Khan Academy
with st.expander("Khan Academy"):
    st.markdown("[Set Operations](https://youtu.be/OCNXS_m1HWU?si=FnEkWvXtXlfxcY9U)")
    st.markdown("[Universal Set and Absolute Complement Set](https://youtu.be/GVZUpOm3XUg?si=ec5gw3vHYfYCU8Fi)")
    st.markdown("[Intersection and Union of Sets](https://youtu.be/jAfNg3ylZAI?si=K-fw95qatP0ueQSx)")
    st.markdown("[Difference Between Sets](https://youtu.be/2B4EBvVvf9w?si=bahKhDiX7v8A7PbS)")
    st.markdown("[Subset and Superset](https://youtu.be/1wsF9GpGd00?si=G4WlVXtVHn9L6CHS)")

# Organic Chemistry Tutor
with st.expander("Organic Chemistry Tutor"):
    st.markdown("[Set Builder Notation](https://youtu.be/FLgiccWl434?si=t5ZrhRuCh_dVvtzp)")
    st.markdown("[Union and Intersection of Sets](https://youtu.be/xZELQc11ACY?si=hf1vYH_w9iUFq_5c)")
    st.markdown("[Venn Diagrams](https://youtu.be/32iNIZJ2dI4?si=nvV4kjQhL6FAJN3b)")

# Free Code Camp
with st.expander("Free Code Camp"):
    st.markdown("[Set Theory Full Course](https://youtu.be/2SpuBqvNjHI?si=76UAdABj_j2ty11D)")

# TrevTutor
with st.expander("TrevTutor"):
    st.markdown("[Introduction to Set Theory](https://youtu.be/tyDKR4FG3Yw?si=gMDrJ4TmB8t2ui2P)")
    st.markdown("[Subsets and Power Sets](https://youtu.be/H5D6EAezsXQ?si=p7NaLpcrd6KbEjS3)")
    st.markdown("[Set Operations](https://youtu.be/4TlCToZZ5gA?si=_bN4YB_l3IM0czsc)")

# Images Section
st.header("Visuals")

st.write("Explore law tables and visuals for better understanding.")
image_path = root_dir / "images" / "setLaws.webp"
st.image(str(image_path), caption="Law Table ")

st.write("A Summary of the set relations.")
image_path = root_dir / "images" / "set_relations.jpg"
st.image(str(image_path), caption="Set Relations ")

st.write("The General format of Venn Diagrams")
image_path = root_dir / "images" / "Venn_diagram.png"
st.image(str(image_path), caption="Venn Diagrams ")