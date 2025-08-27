import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
from matplotlib.colors import to_rgba
import pandas as pd

def blend_colors(color1, color2):
    """Blend two colors using their RGBA values."""
    rgba1 = to_rgba(color1)
    rgba2 = to_rgba(color2)
    blended = [(c1 + c2) / 2 for c1, c2 in zip(rgba1, rgba2)]
    return blended

def blend_three_colors(color1, color2, color3):
    """Blend three colors using their RGBA values."""
    rgba1 = to_rgba(color1)
    rgba2 = to_rgba(color2)
    rgba3 = to_rgba(color3)
    blended = [(c1 + c2 + c3) / 3 for c1, c2, c3 in zip(rgba1, rgba2, rgba3)]
    return blended

def display_set_relations_table_2_sets(sets):
    """Create a table summarizing set relations for 2 sets."""
    relations = {
        "Relation": [
            "A ∪ B (Union)", 
            "A ∩ B (Intersection)", 
            "A - B (Difference)", 
            "B - A (Difference)", 
            "A ⊕ B (Symmetric Difference)", 
            "Aᶜ (Complement)", 
            "Bᶜ (Complement)"
        ],
        "Result": [
            ', '.join(map(str, sets['A'] | sets['B'])),  # Union
            ', '.join(map(str, sets['A'] & sets['B'])),  # Intersection
            ', '.join(map(str, sets['A'] - sets['B'])),  # A - B
            ', '.join(map(str, sets['B'] - sets['A'])),  # B - A
            ', '.join(map(str, sets['A'] ^ sets['B'])),  # Symmetric Difference
            'N/A (requires universal set)',  # Complement of A
            'N/A (requires universal set)'   # Complement of B
        ]
    }
    df = pd.DataFrame(relations)
    st.subheader("Set Relations Summary (2 Sets)")
    st.table(df)

def display_set_relations_table_3_sets(sets):
    """Create a table summarizing set relations for 3 sets."""
    relations = {
        "Relation": [
            "A ∪ B ∪ C (Union)", 
            "A ∩ B ∩ C (Intersection)", 
            "A - (B ∪ C) (Difference)", 
            "B - (A ∪ C) (Difference)", 
            "C - (A ∪ B) (Difference)", 
            "(A ∩ B) - C", 
            "(A ∩ C) - B", 
            "(B ∩ C) - A", 
            "A ⊕ B ⊕ C (Symmetric Difference)"
        ],
        "Result": [
            ', '.join(map(str, sets['A'] | sets['B'] | sets['C'])),  # Union
            ', '.join(map(str, sets['A'] & sets['B'] & sets['C'])),  # Intersection
            ', '.join(map(str, sets['A'] - (sets['B'] | sets['C']))),  # A - (B ∪ C)
            ', '.join(map(str, sets['B'] - (sets['A'] | sets['C']))),  # B - (A ∪ C)
            ', '.join(map(str, sets['C'] - (sets['A'] | sets['B']))),  # C - (A ∪ B)
            ', '.join(map(str, (sets['A'] & sets['B']) - sets['C'])),  # (A ∩ B) - C
            ', '.join(map(str, (sets['A'] & sets['C']) - sets['B'])),  # (A ∩ C) - B
            ', '.join(map(str, (sets['B'] & sets['C']) - sets['A'])),  # (B ∩ C) - A
            ', '.join(map(str, sets['A'] ^ sets['B'] ^ sets['C']))     # Symmetric Difference
        ]
    }
    df = pd.DataFrame(relations)
    st.subheader("Set Relations Summary (3 Sets)")
    st.table(df)

def set_visualizer():
    st.title("Interactive Set Visualizer")
    st.write("Explore set operations visually and view summarized results.")

    # Specify the number of sets
    num_sets = st.selectbox("Select the number of sets (2 or 3 only):", [2, 3])
    st.write(f"Enter elements for each of the {num_sets} sets below:")

    # Initialize sets based on the number of sets chosen
    sets = {}
    for i in range(num_sets):
        elements = st.text_area(f"Enter elements for Set {chr(65 + i)} (comma-separated):", key=f"set_{chr(65 + i)}")
        
        # Validate input to ensure all elements are integers
        try:
            sets[chr(65 + i)] = set(map(int, map(str.strip, elements.split(',')))) if elements else set()
        except ValueError:
            st.error(f"Please ensure all elements in Set {chr(65 + i)} are integers.")
            return

    # Customize colors for each set
    st.write("Customize the colors for each set:")
    set_colors = {}
    for i in range(num_sets):
        color = st.color_picker(
            f"Pick a color for Set {chr(65 + i)}",
            "#ff9999" if i == 0 else "#66b3ff" if i == 1 else "#99ff99",
            key=f"color_{chr(65 + i)}",
        )
        set_colors[chr(65 + i)] = color

    # Generate Venn Diagram
    if st.button("Generate Venn Diagram"):
        plt.figure(figsize=(5, 5))
        if num_sets == 2:
            venn = venn2([sets['A'], sets['B']], ('Set A', 'Set B'))

            # Blend colors for intersections
            blended_ab = blend_colors(set_colors['A'], set_colors['B'])

            # Apply colors and labels
            venn.get_patch_by_id('10').set_color(set_colors['A'])
            venn.get_patch_by_id('01').set_color(set_colors['B'])
            venn.get_label_by_id('10').set_text(', '.join(map(str, sets['A'] - sets['B'])))
            venn.get_label_by_id('01').set_text(', '.join(map(str, sets['B'] - sets['A'])))
            if venn.get_patch_by_id('11'):
                venn.get_patch_by_id('11').set_color(blended_ab)
                venn.get_label_by_id('11').set_text(', '.join(map(str, sets['A'] & sets['B'])))

            # Display relations table for 2 sets
            display_set_relations_table_2_sets(sets)

        elif num_sets == 3:
            venn = venn3([sets['A'], sets['B'], sets['C']], ('Set A', 'Set B', 'Set C'))

            # Blend colors for intersections
            blended_ab = blend_colors(set_colors['A'], set_colors['B'])
            blended_ac = blend_colors(set_colors['A'], set_colors['C'])
            blended_bc = blend_colors(set_colors['B'], set_colors['C'])
            blended_abc = blend_three_colors(set_colors['A'], set_colors['B'], set_colors['C'])

            # Apply colors and labels
            venn.get_patch_by_id('100').set_color(set_colors['A'])
            venn.get_patch_by_id('010').set_color(set_colors['B'])
            venn.get_patch_by_id('001').set_color(set_colors['C'])
            venn.get_label_by_id('100').set_text(', '.join(map(str, sets['A'] - sets['B'] - sets['C'])))
            venn.get_label_by_id('010').set_text(', '.join(map(str, sets['B'] - sets['A'] - sets['C'])))
            venn.get_label_by_id('001').set_text(', '.join(map(str, sets['C'] - sets['A'] - sets['B'])))
            if venn.get_patch_by_id('110'):
                venn.get_patch_by_id('110').set_color(blended_ab)
                venn.get_label_by_id('110').set_text(', '.join(map(str, sets['A'] & sets['B'] - sets['C'])))
            if venn.get_patch_by_id('101'):
                venn.get_patch_by_id('101').set_color(blended_ac)
                venn.get_label_by_id('101').set_text(', '.join(map(str, sets['A'] & sets['C'] - sets['B'])))
            if venn.get_patch_by_id('011'):
                venn.get_patch_by_id('011').set_color(blended_bc)
                venn.get_label_by_id('011').set_text(', '.join(map(str, sets['B'] & sets['C'] - sets['A'])))
            if venn.get_patch_by_id('111'):
                venn.get_patch_by_id('111').set_color(blended_abc)
                venn.get_label_by_id('111').set_text(', '.join(map(str, sets['A'] & sets['B'] & sets['C'])))

            # Display relations table for 3 sets
            display_set_relations_table_3_sets(sets)

        st.pyplot(plt)

set_visualizer()
