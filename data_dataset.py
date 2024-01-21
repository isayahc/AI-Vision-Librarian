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



if __name__ == '__main__':
    dataset = load_dataset("jovianzm/Pexels-400k")
    
    dataset_image_urls = dataset['train']['thumbnail']
    random_entries = get_random_entries(dataset_image_urls, 5)

    random_sample = sample(random_entries,1)[0]

    response = requests.get(random_sample)

    if response.status_code == 200:
        # Open the image using PIL
        image = BytesIO(response.content)
    
    image:bytes = response.content

    x = bytes_query_image(image,"given the image provided you must generate a list of tags in such that if a user was searching for this image they would be able to find it")
    


    # show_images_from_urls_matplotlib(random_entries)
    # show_images_from_urls_tempdir(random_entries)



x=0
