"""

# Vision Library Use Interface

## Overview of interface

The the sake of simplicity i will be using streamlit

The user should have 2 options

- provide a list of images to have tags be generated from
    - If the user has their own data
        - allow the program to generate the annotated images
        - do not allow more than 10 images
- else use the knowledge base i have provided

There should be a text feild for the user to query the vectordatabase



"""

# vision_interface.py

import streamlit as st
from PIL import Image

# Function to generate annotated images
def generate_annotated_images(images):
    # Your vision library code for generating annotated images goes here
    # This is a placeholder for demonstration purposes
    annotated_images = [f"Annotated_{img}" for img in images]
    return annotated_images

# Function to query vectordatabase
def query_vectordatabase(query):
    # Your code to query the vectordatabase goes here
    # This is a placeholder for demonstration purposes
    results = [f"Result_{i}" for i in range(1, 6)]
    return results

# Streamlit app
def main():
    st.title("Vision Library Interface")

    option = st.radio("Choose an option:", ["Use Own Images", "Use Knowledge Base"])

    if option == "Use Own Images":
        st.write("Upload your images (up to 10)")
        uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

        if uploaded_files:
            st.write("Images to process:")
            st.image(uploaded_files, width=200)

            if len(uploaded_files) <= 10:
                if st.button("Generate Annotated Images"):
                    image_paths = [Image.open(file) for file in uploaded_files]
                    annotated_images = generate_annotated_images(image_paths)
                    st.success("Annotations generated successfully!")
                    st.image(annotated_images, width=200)
            else:
                st.warning("Please upload up to 10 images.")

    else:
        query = st.text_input("Enter your query for the vectordatabase:")
        if query:
            if st.button("Submit Query"):
                results = query_vectordatabase(query)
                st.success("Query results:")
                st.write(results)

if __name__ == "__main__":
    main()
