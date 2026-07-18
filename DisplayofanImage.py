import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
def load_image(file_path):
    return np.array(Image.open(file_path))
def create_binary_negative(image):
    threshold = 128
    return (image < threshold).astype(np.uint8) * 255
def create_grayscale_negative(image):
    return 255 - image
def display_images(original, binary_neg, grayscale_neg):
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].imshow(original, cmap='gray')
    axs[0].set_title('Original Image')
    axs[0].axis('off')
    axs[1].imshow(binary_neg, cmap='gray')
    axs[1].set_title('Binary Negative')
    axs[1].axis('off')
    axs[2].imshow(grayscale_neg, cmap='gray')
    axs[2].set_title('Grayscale Negative')
    axs[2].axis('off')
plt.tight_layout()
plt.show()
# Main program
file_path = 'C:\Users\chari\OneDrive\Pictures\spring-photograph-with-beautiful-flowers.jpg # Replace with your image path'
original_image = load_image(file_path)
# Convert to grayscale if the image is in color
if len(original_image.shape) == 3:
    original_image = np.mean(original_image, axis=2).astype(np.uint8)
binary_negative = create_binary_negative(original_image)
grayscale_negative = create_grayscale_negative(original_image)
display_images(original_image, binary_negative, grayscale_negative)