import argparse
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Function to quantize image
def quantizeImage(image, num_levels):
    # Calculate the quantization step size
    step = 256 // num_levels
    quantized_image = (image // step) * step
    return quantized_image

# Function to display images
def showImages(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(15, 5))
    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img, cmap='gray', vmin=0, vmax=255)
        ax.set_title(title)
        ax.axis('off')
    plt.show()

def convertImage(filename):
    # Load the image
    if not filename.lower().endswith('.png'):
        filename += '.png'
    # Converts the png file to PGM
    image = Image.open(filename).convert('L')

    # Convert images to numpy arrays
    image_array = np.array(image)    

    # List of quantization levels to test
    levels = [128, 32, 8, 2]

    # Create quantized image
    quantized_images = [quantizeImage(image_array, L) for L in levels]

    # Display results for image
    titles = [f"image - L={L}" for L in levels]
    showImages([image] + quantized_images, ["Image Original"] + titles)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image Converter')
    parser.add_argument('-f','--image_file', type=str, default = "peppers.png", help='path to image file')
    args = parser.parse_args()
    convertImage(args.image_file)