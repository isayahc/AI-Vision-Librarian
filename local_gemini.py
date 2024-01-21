"""
Module: clarifai_gpt_conversion

This module provides functions to convert images into SVG format using the OpenAI GPT-4 Vision model through the Clarifai API.

Functions:
- query_image(image_file_location: str, prompt: str, inference_params: Optional[dict] = None) -> str:
    Converts an image into SVG format using the OpenAI GPT-4 Vision model.
    
    Parameters:
    - image_file_location (str): The file location of the image to be converted.
    - prompt (str): The prompt for image conversion.
    - inference_params (Optional[dict]): Optional parameters for model inference.

    Returns:
    - str: The result of converting the image into SVG format.

- bytes_query_image(image: bytes, prompt: str, inference_params: Optional[dict] = None) -> str:
    Converts an image (provided as bytes) into SVG format using the OpenAI GPT-4 Vision model.
    
    Parameters:
    - image (bytes): The image data in bytes.
    - prompt (str): The prompt for image conversion.
    - inference_params (Optional[dict]): Optional parameters for model inference.

    Returns:
    - str: The result of converting the image into SVG format.

Example Usage:
if __name__ == '__main__':
    IMAGE_FILE_LOCATION = "/path/to/your/image.png"
    PROMPT = "Convert this image into a .svg"

    # Example with image file location
    converted_svg = query_image(IMAGE_FILE_LOCATION, PROMPT)
    print(converted_svg)

    # Example with image data provided as bytes
    with open(IMAGE_FILE_LOCATION, "rb") as f:
        image_bytes = f.read()
    converted_svg_bytes = bytes_query_image(image_bytes, PROMPT)
    print(converted_svg_bytes)
"""

from clarifai.client.model import Model
from clarifai.client.input import Inputs
from typing import Optional

def query_image(image_file_location: str, prompt: str, inference_params: Optional[dict] = None) -> str:
    """
    Convert an image into SVG format using the OpenAI GPT-4 Vision model.

    Parameters:
    - image_file_location (str): The file location of the image to be converted.
    - prompt (str): The prompt for image conversion.
    - inference_params (Optional[dict]): Optional parameters for model inference.

    Returns:
    - str: The result of converting the image into SVG format.
    """
    with open(image_file_location, "rb") as f:
        file_bytes = f.read()

    # Set default inference parameters if not provided
    inference_params = inference_params or dict(temperature=0.2, max_tokens=100)

    # Initialize the Clarifai GPT-4 Vision model
    model = Model("https://clarifai.com/openai/chat-completion/models/openai-gpt-4-vision")

    # Make predictions using the model
    model_prediction = model.predict(
        inputs=[
            Inputs.get_multimodal_input(
                input_id="",
                image_bytes=file_bytes,
                raw_text=prompt
            )
        ],
        inference_params=inference_params
    )

    # Extract the result of image conversion
    result = model_prediction.outputs[0].data.text.raw

    return result

def bytes_query_image(image: bytes, prompt: str, inference_params: Optional[dict] = None) -> str:
    """
    Convert an image into SVG format using the OpenAI GPT-4 Vision model.

    Parameters:
    - image_file_location (str): The file location of the image to be converted.
    - prompt (str): The prompt for image conversion.
    - inference_params (Optional[dict]): Optional parameters for model inference.

    Returns:
    - str: The result of converting the image into SVG format.
    """
    # with open(image_file_location, "rb") as f:
        # file_bytes = f.read()

    file_bytes = image

    # Set default inference parameters if not provided
    inference_params = inference_params or dict(temperature=0.2, max_tokens=100)

    # Initialize the Clarifai GPT-4 Vision model
    model = Model("https://clarifai.com/openai/chat-completion/models/openai-gpt-4-vision")

    # Make predictions using the model
    model_prediction = model.predict(
        inputs=[
            Inputs.get_multimodal_input(
                input_id="",
                image_bytes=file_bytes,
                raw_text=prompt
            )
        ],
        inference_params=inference_params
    )

    # Extract the result of image conversion
    result = model_prediction.outputs[0].data.text.raw

    return result

if __name__ == '__main__':
    # Example usage:
    # IMAGE_FILE_LOCATION = "/home/isayahc/projects/Hackathon-Projects/clarify/data/image4_1.png"
    # PROMPT = "convert this image into a .svg"

    
    # converted_svg = query_image(IMAGE_FILE_LOCATION, PROMPT)
    # print(converted_svg)
    pass