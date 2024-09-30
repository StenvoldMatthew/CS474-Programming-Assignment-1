import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Function to quantize image
def quantize_image(image, num_levels):
    # Calculate the quantization step size
    step = 256 // num_levels
    quantized_image = (image // step) * step
    return quantized_image

# Function to display images
def show_images(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(15, 5))
    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img, cmap='gray', vmin=0, vmax=255)
        ax.set_title(title)
        ax.axis('off')
    plt.show()

# Load the images
lenna_image = Image.open('lenna.png').convert('L')
peppers_image = Image.open('peppers.png').convert('L')

# Convert images to numpy arrays
lenna_array = np.array(lenna_image)
peppers_array = np.array(peppers_image)

# List of quantization levels to test
levels = [128, 32, 8, 2]

# Create quantized images for both Lenna and Peppers
lenna_quantized_images = [quantize_image(lenna_array, L) for L in levels]
peppers_quantized_images = [quantize_image(peppers_array, L) for L in levels]

# Display results for Lenna
titles = [f"Lenna - L={L}" for L in levels]
show_images([lenna_image] + lenna_quantized_images, ["Lenna Original"] + titles)

# Display results for Peppers
titles = [f"Peppers - L={L}" for L in levels]
show_images([peppers_image] + peppers_quantized_images, ["Peppers Original"] + titles)