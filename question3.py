import argparse
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Function for histogram equalization
def histogram_equalization(image):
    # Flatten the image array and calculate histogram
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])

    # Cumulative distribution function (CDF)
    cdf = hist.cumsum()

    # Normalize CDF to avoid division by zero
    cdf_normalized = cdf * hist.max() / cdf.max()

    # Normalize the CDF
    cdf = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
    cdf = cdf.astype('uint8')

    # Use the CDF to map the original image's pixel values to equalized values
    equalized_image = cdf[image]

    return equalized_image, cdf_normalized

# Function to display images and histograms
def plot_image_and_histogram(image, title, equalized_image, equalized_title):
    fig, axes = plt.subplots(2, 2, figsize=(12, 6))

    # Original image and histogram
    axes[0, 0].imshow(image, cmap='gray', vmin=0, vmax=255)
    axes[0, 0].set_title(title)
    axes[0, 0].axis('off')
    axes[1, 0].hist(image.flatten(), bins=256, range=(0, 256), color='gray')
    axes[1, 0].set_title("Original Histogram")

    # Equalized image and histogram
    axes[0, 1].imshow(equalized_image, cmap='gray', vmin=0, vmax=255)
    axes[0, 1].set_title(equalized_title)
    axes[0, 1].axis('off')
    axes[1, 1].hist(equalized_image.flatten(), bins=256, range=(0, 256), color='gray')
    axes[1, 1].set_title("Equalized Histogram")

    plt.tight_layout()
    plt.show()

def holderFunctionName(filename, testValues):
    image_array = []
    if(testValues[0] != 0):
        image_array = np.random.randint(testValues[1], testValues[2], size=(testValues[0], testValues[0]), dtype=np.uint8)
    else:
        image = Image.open(filename).convert('L')
        image_array = np.array(image)

    # Perform histogram equalization
    equalized_image, cdf_normalized = histogram_equalization(image_array)

    # Plot the original and equalized images along with their histograms
    plot_image_and_histogram(image_array, "Original Image", equalized_image, "Equalized Image")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image Converter')
    parser.add_argument('-f','--image_file', type=str, default = "boat.png", help='path to image file')
    parser.add_argument('-t','--test_size', type=int, default = 0, help='set to value to run test')
    parser.add_argument('-min','--test_min', type=int, default = 0, help='the minimum value test will give')
    parser.add_argument('-max','--test_max', type=int, default = 128, help='the maximum value test will give')
    args = parser.parse_args()
    holderFunctionName(args.image_file, [args.test_size, args.test_min, args.test_max])