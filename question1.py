import numpy as np
import argparse
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

def convertImage(filename):
    # Load the images
    image = Image.open(filename).convert('RGB')

    # Original image size
    original_size = (256, 256)

    # Resize to 256x256 if necessary
    image = image.resize(original_size, Image.NEAREST)

    # Sub-sample and resize for factors 2, 4, 8
    factors = [2, 4, 8]
    image_results = []

    for factor in factors:
        # Sub-sample and resize image
        image_subsampled, image_resized = sub_sample_and_resize(image, factor)
        image_results.append((image_subsampled, image_resized))

    # Display results for Image
    for factor, (subsampled, resized) in zip(factors, image_results):
        show_images([image, subsampled, resized],
                    [f"Image Original", f"Sub-sampled (Factor {factor})", f"Resized Back to 256x256"])
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image Converter')
    parser.add_argument('-f','--image_file', type=str, default = "peppers.png", help='path to image file')
    args = parser.parse_args()
    convertImage(args.image_file)