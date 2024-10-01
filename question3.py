import argparse
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Function for histogram equalization
def histogramEqualization(image):
    # Flatten the image array and calculate histogram
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])

    # Cumulative distribution function (CDF)
    cdf = hist.cumsum()

    # Normalize the CDF
    cdf = (cdf - cdf.min()) * (255 / (cdf.max() - cdf.min()))
    cdf = cdf.astype('uint8')

    # Use the CDF to map the original image's pixel values to equalized values
    equalized_image = cdf[image]
    return equalized_image 

# Function to display images and histograms
def plotResults(image, title, equalized_image, equalized_title):
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

def equalizeImage(filename, testValues):
    image_array = []
    if(testValues[0] != 0):
        image_array = np.random.normal(loc=testValues[1], scale=testValues[2], size=(testValues[0], testValues[0]))
        image_array = np.clip(image_array, 0, 255).astype(np.uint8)
    else:
        if not filename.lower().endswith('.png'):
            filename += '.png'
        # Converts the png file to PGM
        image = Image.open(filename).convert('L')
        image_array = np.array(image)

    # Perform histogram equalization
    equalized_image = histogramEqualization(image_array)

    # Plot the original and equalized images along with their histograms
    plotResults(image_array, "Original Image", equalized_image, "Equalized Image")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image Converter')
    parser.add_argument('-f','--image_file', type=str, default = "f_16.png", help='path to image file')
    parser.add_argument('-t','--test_size', type=int, default = 0, help='set to value to run test')
    parser.add_argument('-l','--test_loc', type=int, default = 150, help='the value the test distribution will be centered on')
    parser.add_argument('-s','--test_sigma', type=int, default = 30, help='how widely spread the test image will be')
    args = parser.parse_args()
    equalizeImage(args.image_file, [args.test_size, args.test_loc, args.test_sigma])