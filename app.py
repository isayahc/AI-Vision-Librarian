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
import os
import streamlit as st
from vision_library.local_gemini import bytes_query_image
from vision_library.prompt import query_image_prompt
from vision_library.clarifai_llama_index import query_engine

# Function to generate annotated images from user-provided data
def generate_annotated_images(image_list):
    # Add your implementation to generate annotated images
    images_list_as_bytes = [i.getvalue() for i in image_list]

    i = images_list_as_bytes[0]

    # st.write(i)

    # for i in images_list_as_bytes:
    #     AI_gnerated_tags = bytes_query_image(i,query_image_prompt)
    AI_gnerated_tags = bytes_query_image(i,query_image_prompt)
    st.write(AI_gnerated_tags)
    
# def save_uploaded_images(image_list):
#     # Create 'data' directory if it doesn't exist
#     data_directory = 'data'
#     os.makedirs(data_directory, exist_ok=True)

#     # Save uploaded images to the 'data' directory
#     for i, image_file in enumerate(image_list):
#         image_path = os.path.join(data_directory, f"uploaded_image_{i}.png")
#         image_file.save(image_path)
    
#     st.success(f"{len(image_list)} images saved successfully in the 'data' directory!")


# Function to search and return results from the vectorized data
def search_vectorized_data(query):
    # Add your implementation to search vectorized data
    return query_engine.query(query)
    # return "Hi"



# Streamlit App
def main():
    st.title("Vision Library User Interface")

    # User options
    option = st.radio("Choose an option:", ["Provide Images", "Use Knowledge Base"])

    if option == "Provide Images":
        st.subheader("Option 1: Provide a list of images")

        st.write("currently unavialable")

        # User input for image list
        # uploaded_files = st.file_uploader("Upload up to 10 images", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="images")

        

        # if uploaded_files and len(uploaded_files) <= 10:
        #     st.write(uploaded_files)
        #     # st.write(os.getcwd())
        #     # save_uploaded_images(uploaded_files)
            
        #     # generate_annotated_images(uploaded_files)

        #     # User input for query
        #     query = st.text_input("Enter your query for the Vector Database:")

        #     # Submit button
        #     if st.button("Submit"):
        #         # Search and return results
        #         results = search_vectorized_data(query)
    
        #         # Display results
        #         st.write("Search Results:")
        #         st.write(results)

    elif option == "Use Knowledge Base":
        st.subheader("Option 2: Use the Knowledge Base")
        st.write("for context i am using the Pexels-400k dataset location at")
        st.write("https://huggingface.co/datasets/jovianzm/Pexels-400k")
        # User input for query
        query = st.text_input("Enter your query for the Vector Database:")

        # Submit button
        if st.button("Submit"):
            # Search and return results
            results = search_vectorized_data(query)

            # Display results
            st.write("Search Results:")
            st.markdown(results)

if __name__ == "__main__":
    main()
