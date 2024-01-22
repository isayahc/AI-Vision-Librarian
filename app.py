"""

# Vision Library Use Interface

## Overview of interface

The the sake of simplicity i will be using streamlit

The user should have 2 options:

## Option 1
- provide a list of images to have tags be generated from
    - If the user has their own data
        - allow the program to generate the annotated images
        - do not allow more than 10 images

## Option 2
-  use the knowledge base i have provided

There should be a text field for the user to query the vectordatabase

Next to or below this text field there should be a submit button

when the submit button is clicked there datat is vectorized and it should be search.

Then return the results

"""

# vision_interface.py

import streamlit as st

# Function to generate annotated images from user-provided data
def generate_annotated_images(image_list):
    # Add your implementation to generate annotated images
    pass

# Function to search and return results from the vectorized data
def search_vectorized_data(query):
    # Add your implementation to search vectorized data
    return "Hi"

# Streamlit App
def main():
    st.title("Vision Library Use Interface")

    # User options
    option = st.radio("Choose an option:", ["Provide Images", "Use Knowledge Base"])

    if option == "Provide Images":
        st.subheader("Option 1: Provide a list of images")

        # User input for image list
        uploaded_files = st.file_uploader("Upload up to 10 images", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="images")
        

        if uploaded_files and len(uploaded_files) <= 10:
            generate_annotated_images(uploaded_files)

            # User input for query
            query = st.text_input("Enter your query for the Vector Database:")

            # Submit button
            if st.button("Submit"):
                # Search and return results
                results = search_vectorized_data(query)
    
                # Display results
                st.write("Search Results:")
                st.write(results)

    elif option == "Use Knowledge Base":
        st.subheader("Option 2: Use the Knowledge Base")

        # User input for query
        query = st.text_input("Enter your query for the Vector Database:")

        # Submit button
        if st.button("Submit"):
            # Search and return results
            results = search_vectorized_data(query)

            # Display results
            st.write("Search Results:")
            st.write(results)

if __name__ == "__main__":
    main()
