import numpy as np
import argparse
from PIL import Image
import matplotlib.pyplot as plt

# Function to display images
def showImages(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(15, 5))
    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img, cmap='gray', vmin=0, vmax=255)
        ax.set_title(title)
        ax.axis('off')
    plt.show()


# Function to perform sub-sampling and resizing
def subSample(image, factor):
    image_array = np.array(image) 
    newSize = 256//factor
    
    resultsArray = np.empty((newSize, newSize), dtype=np.uint8)
    resizedArray = np.empty((256, 256), dtype=np.uint8)
    for i in range(256):
        for j in range(256):
            if i % factor == 0 and j % factor == 0:
                resultsArray[i//factor, j//factor] = image_array[i, j]

                # Will make the new image 256x256 
                for k in range(factor):
                    for l in range(factor):
                        resizedArray[i+k, j+l] = image_array[i, j]

    return resizedArray

def convertImage(filename):
    # Load the image
    if not filename.lower().endswith('.png'):
        filename += '.png'
    image = Image.open(filename).convert('L')

    # Resize to 256x256 if necessary
    original_size = (256, 256)
    image = image.resize(original_size, Image.NEAREST)

    # Sub-sample and resize for factors 2, 4, 8
    factors = [2, 4, 8]
    image_results = []
    titles = [f"Image Original"]

    for factor in factors:
        # Sub-sample and resize image
        image_subsampled= subSample(image, factor)
        image_results.append(image_subsampled)
        titles.append(f"Sub-sampled (Factor {factor})")

    # Display results
    showImages([image] + image_results, titles)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image Converter')
    parser.add_argument('-f','--image_file', type=str, default = "peppers.png", help='path to image file')
    args = parser.parse_args()
    convertImage(args.image_file)