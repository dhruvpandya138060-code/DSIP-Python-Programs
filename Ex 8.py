import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Upload the image
uploaded = files.upload()

# Get the uploaded image name
image_path = next(iter(uploaded))

# Load the image in grayscale
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Image could not be loaded.")
else:
    # Calculate the histogram
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Plot the original histogram
    plt.figure(figsize=(8, 6))
    plt.title('Original Image Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.plot(histogram)
    plt.xlim([0, 256])
    plt.grid(True)
    plt.show()

    # Perform histogram equalization
    equalized_image = cv2.equalizeHist(image)

    # Display original and equalized images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Equalized Image')
    plt.imshow(equalized_image, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    # Calculate histogram of equalized image
    equalized_histogram = cv2.calcHist(
        [equalized_image], [0], None, [256], [0, 256]
    )

    # Plot equalized histogram
    plt.figure(figsize=(8, 6))
    plt.title('Equalized Image Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.plot(equalized_histogram)
    plt.xlim([0, 256])
    plt.grid(True)
    plt.show()
