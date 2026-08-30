#1.	Smoothening and Sharpening using Spatial Filters

import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow

# Upload image
uploaded = files.upload()

# Get uploaded image filename
filename = next(iter(uploaded))

# Load the image
image = cv2.imread(filename)

# Define the Gaussian kernel for smoothing
kernel_size = (5, 5)
sigma = 1.5

gaussian_kernel = cv2.getGaussianKernel(kernel_size[0], sigma)
gaussian_kernel = np.outer(gaussian_kernel, gaussian_kernel)

# Apply Gaussian smoothing
smoothed_image = cv2.filter2D(image, -1, gaussian_kernel)

# Define a sharpening kernel
sharpening_kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])

# Apply sharpening
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

# Display images
print("Original Image:")
cv2_imshow(image)

print("Smoothed Image:")
cv2_imshow(smoothed_image)

print("Sharpened Image:")
cv2_imshow(sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#2.	Smoothening using Averaging Linear Filter
import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow

# Upload image
uploaded = files.upload()

# Get uploaded image filename
filename = next(iter(uploaded))

# Load the image
image = cv2.imread(filename)

# Define the size of the averaging filter kernel
kernel_size = (5, 5)

# Create the averaging filter kernel
kernel = np.ones(kernel_size, dtype=np.float32) / (
    kernel_size[0] * kernel_size[1]
)

# Apply the averaging filter
smoothed_image = cv2.filter2D(image, -1, kernel)

# Display images
print("Original Image:")
cv2_imshow(image)

print("Averaging Filter Smoothed Image:")
cv2_imshow(smoothed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#3.	Smoothening using Median Filter
import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow

# Upload image
uploaded = files.upload()

# Get uploaded image filename
filename = next(iter(uploaded))

# Load the image
image = cv2.imread(filename)

# Define the size of the median filter kernel
# It must be an odd number
kernel_size = 5

# Apply the median filter
smoothed_image = cv2.medianBlur(image, kernel_size)

# Display images
print("Original Image:")
cv2_imshow(image)

print("Median Filter Smoothed Image:")
cv2_imshow(smoothed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#4: Sharpening using Spatial High-Pass Filter
import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow
	
# Upload image
uploaded = files.upload()
	
# Get uploaded image filename
filename = next(iter(uploaded))
	
# Load the image
image = cv2.imread(filename)
	
# Apply Gaussian smoothing to reduce noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
	
# Create a Laplacian high-pass sharpening kernel
laplacian_kernel = np.array([
	    [0, -1,  0],
	    [-1, 5, -1],
	    [0, -1,  0]
], dtype=np.float32)
	
# Apply the Laplacian filter
sharpened_image = cv2.filter2D(
blurred_image,
-1,
laplacian_kernel
)
	
# Display images
print("Original Image:")
cv2_imshow(image)
	
print("Blurred Image:")
cv2_imshow(blurred_image)
	
print("Sharpened Image:")
cv2_imshow(sharpened_image)
	
cv2.waitKey(0)
cv2.destroyAllWindows()
