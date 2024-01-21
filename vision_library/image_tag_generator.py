from datasets import load_dataset
import matplotlib.pyplot as plt
from random import sample
from typing import List

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import requests
from io import BytesIO

from typing import List
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import requests
from io import BytesIO
import tempfile
import os
# Load the "jovianzm/Pexels-400k" dataset
from local_gemini import query_image, bytes_query_image

import requests
from PIL import Image
from io import BytesIO

from prompt import query_image_prompt

def show_images_from_urls_tempdir(image_urls: List[str]) -> None:
    """
    Download images from a list of URLs, save them to a temporary directory, and display using matplotlib.

    Parameters:
    - image_urls (List[str]): A list of URLs pointing to images.

    Returns:
    - None
    """
    # Create a temporary directory to save images
    with tempfile.TemporaryDirectory() as temp_dir:
        for i, image_url in enumerate(image_urls):
            response = requests.get(image_url)
            
            if response.status_code == 200:
                # Save the image to the temporary directory
                image_data = BytesIO(response.content)
                file_name = os.path.basename(image_url)
                image_path = os.path.join(temp_dir, file_name)
                
                with open(image_path, "wb") as image_file:
                    image_file.write(image_data.read())
                    
                # Display the image using matplotlib
                image = mpimg.imread(image_path)
                plt.imshow(image)
                plt.axis("off")  # Turn off axis labels
                # plt.show()
                plt.clf()
                
                # Remove the saved image file after displaying
                os.remove(image_path)
            else:
                print(f"Failed to retrieve image from URL: {image_url}")


def get_random_entries(data_list: List[str], n: int) -> List[str]:
    """
    Get n random entries from a List[str].

    Parameters:
    - data_list (List[str]): The input list of strings.
    - n (int): The number of random entries to retrieve.

    Returns:
    - List[str]: A list containing n random entries from the input list.
    """
    return sample(data_list, min(n, len(data_list)))

def get_image_from_url(url:str) -> bytes:
    """
    get the bytes of an images from a url

    Parameters:
    - url (str) the url of the image

    Returns:
    - bytes: the image represented in bytes
    """

    response = requests.get(url)

    if response.status_code == 200:
        # Open the image using PIL
        image = response.content
        return image
    else:
        raise ValueError("this is wrong")
    # return  image

def create_txt_file(image_link: str, strings: list, output_path: str) -> None:
    """
    Create a text file with the image link on the first line and a series of strings on the following lines.

    Parameters:
    - image_link (str): The link of the image.
    - strings (list): A list of strings to be written to the file.
    - output_path (str): The path to save the text file.

    Returns:
    - None
    """
    with open(output_path, 'w') as file:
        # Write the image link on the first line
        file.write(image_link + '\n')

        # Write strings separated by newline
        file.write('\n'.join(strings))

def change_extension_to_txt(image_path) -> str:
    """
    Change the file extension of an image file to ".txt".

    Parameters:
    - image_path (str): The path to the image file.

    Returns:
    - str: The new path with the ".txt" extension.
    """
    base_name = os.path.basename(image_path)
    file_name, _ = os.path.splitext(base_name)
    txt_file_path = os.path.join(os.path.dirname(image_path), file_name + ".txt")
    return txt_file_path


def generate_images_with_tags(
        output_dir="data",
        dataset="jovianzm/Pexels-400k",
        query_prompt=query_image_prompt
        ) ->None:
    """given a dataset and a output directory generate 
    
    """
    
    dataset_image_urls = dataset['train']['thumbnail']
    random_entries = get_random_entries(dataset_image_urls, 5)
    for i in random_entries:
        image:bytes = get_image_from_url(i)
        generated_tags = bytes_query_image(
            image,
            query_prompt,
            )
        
        # some preprocessing of the results
        generated_tags = generated_tags.split(",")
        generated_tags = [item.strip() for item in generated_tags]

        
        image_base_name = os.path.basename(i)

        tags_save_location = change_extension_to_txt(image_base_name)

        text_file_save_location = os.path.join(output_dir,tags_save_location)

        create_txt_file(
            image_link=i,
            strings=generated_tags,
            output_path=text_file_save_location,
        )        


if __name__ == '__main__':
    # dataset = load_dataset("jovianzm/Pexels-400k")
    # output_dir = "data"
    
    # dataset_image_urls = dataset['train']['thumbnail']
    # random_entries = get_random_entries(dataset_image_urls, 5)

    # for i in random_entries:
    #     image:bytes = get_image_from_url(i)
    #     generated_tags = bytes_query_image(
    #         image,
    #         query_image_prompt
    #         )
        
    #     # some preprocessing of the results
    #     generated_tags = generated_tags.split(",")
    #     generated_tags = [item.strip() for item in generated_tags]

        
    #     image_base_name = os.path.basename(i)

    #     tags_save_location = change_extension_to_txt(image_base_name)

    #     text_file_save_location = os.path.join(output_dir,tags_save_location)

    #     create_txt_file(
    #         image_link=i,
    #         strings=generated_tags,
    #         output_path=text_file_save_location,
    #     )        

    #     x=0
    pass

    x=0
