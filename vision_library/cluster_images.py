from typing import List
import cv2
import numpy as np
from sklearn.cluster import KMeans

def extract_frames(video_path: str) -> List[np.ndarray]:
    cap = cv2.VideoCapture(video_path)
    frames = []

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
    except Exception as e:
        print(f"Error during frame extraction: {e}")
    finally:
        cap.release()

    return frames


def preprocess_image(image: np.ndarray) -> np.ndarray:
    # You may need to resize, convert to grayscale, or apply other preprocessing steps
    # based on your specific use case.
    # For simplicity, let's just flatten the image.
    return image.flatten()

def cluster_images(images: List[np.ndarray], num_clusters: int) -> List[List[np.ndarray]]:
    # Convert each image to a feature vector
    features = [preprocess_image(img) for img in images]

    # Use KMeans clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(features)

    # Organize images into clusters based on labels
    clusters = [[] for _ in range(num_clusters)]
    for i, label in enumerate(labels):
        clusters[label].append(images[i])

    return clusters

# Example usage:
video_path = "Never_Gonna_Give_You_Up.webm"
num_clusters = 3  # Adjust based on your requirements

video_frames = extract_frames(video_path)
image_clusters = cluster_images(video_frames, num_clusters)

# Now image_clusters contains lists of images grouped into clusters.
x=0
