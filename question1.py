import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Function to display images
def show_images(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(15, 5))
    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img)
        ax.set_title(title)
        ax.axis('off')
    plt.show()

# Function to perform sub-sampling and resizing
def sub_sample_and_resize(image, factor):
    # Sub-sample the image
    sub_sampled = image.resize((image.width // factor, image.height // factor), Image.NEAREST)
    
    # Resize back to original size
    resized_back = sub_sampled.resize((image.width, image.height), Image.NEAREST)
    
    return sub_sampled, resized_back

# Load the images
lenna_image = Image.open('lenna.png').convert('RGB')
peppers_image = Image.open('peppers.png').convert('RGB')

# Original image size
original_size = (256, 256)

# Resize to 256x256 if necessary
lenna_image = lenna_image.resize(original_size, Image.NEAREST)
peppers_image = peppers_image.resize(original_size, Image.NEAREST)

# Sub-sample and resize for factors 2, 4, 8
factors = [2, 4, 8]
lenna_results = []
peppers_results = []

for factor in factors:
    # Sub-sample and resize Lenna
    lenna_subsampled, lenna_resized = sub_sample_and_resize(lenna_image, factor)
    lenna_results.append((lenna_subsampled, lenna_resized))

    # Sub-sample and resize Peppers
    peppers_subsampled, peppers_resized = sub_sample_and_resize(peppers_image, factor)
    peppers_results.append((peppers_subsampled, peppers_resized))

# Display results for Lenna
for factor, (subsampled, resized) in zip(factors, lenna_results):
    show_images([lenna_image, subsampled, resized],
                [f"Lenna Original", f"Sub-sampled (Factor {factor})", f"Resized Back to 256x256"])

# Display results for Peppers
for factor, (subsampled, resized) in zip(factors, peppers_results):
    show_images([peppers_image, subsampled, resized],
                [f"Peppers Original", f"Sub-sampled (Factor {factor})", f"Resized Back to 256x256"])