#gray scale 

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# --------------------------------------------
# 1. Upload Image
# --------------------------------------------

uploaded = files.upload()

# Get the uploaded file name
file_name = list(uploaded.keys())[0]

print("Image uploaded successfully!")
print("File name:", file_name)

# --------------------------------------------
# 2. Read Image in Grayscale
# --------------------------------------------

src_image = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if src_image is None:
    print("Error: Image could not be loaded.")
else:
    print("Image loaded successfully!")
    print("Image size:", src_image.shape)

# --------------------------------------------
# 3. Image Negation
# --------------------------------------------

negative_image = 255 - src_image

# --------------------------------------------
# 4. Thresholding
# --------------------------------------------

_, thresholded_image = cv2.threshold(
    src_image,
    128,
    255,
    cv2.THRESH_BINARY
)

# --------------------------------------------
# 5. Gamma Correction
# --------------------------------------------

gamma = 2.0

# Normalize image to range [0, 1]
normalized_image = src_image / 255.0

# Apply gamma correction
gamma_corrected_image = np.power(
    normalized_image,
    1 / gamma
)

# Convert back to range [0, 255]
gamma_corrected_image = np.uint8(
    gamma_corrected_image * 255
)

# --------------------------------------------
# 6. Display All Images
# --------------------------------------------

plt.figure(figsize=(16, 5))

# Original Image
plt.subplot(1, 4, 1)
plt.imshow(src_image, cmap='gray')
plt.title("Original")
plt.axis('off')

# Negative Image
plt.subplot(1, 4, 2)
plt.imshow(negative_image, cmap='gray')
plt.title("Negative")
plt.axis('off')

# Threshold Image
plt.subplot(1, 4, 3)
plt.imshow(thresholded_image, cmap='gray')
plt.title("Threshold")
plt.axis('off')

# Gamma Corrected Image
plt.subplot(1, 4, 4)
plt.imshow(gamma_corrected_image, cmap='gray')
plt.title("Gamma")
plt.axis('off')

plt.tight_layout()
plt.show()

#color scale 

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# -----------------------------------------
# 1. Upload Image
# -----------------------------------------

uploaded = files.upload()

file_name = list(uploaded.keys())[0]

# Read image in grayscale
src_image = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

if src_image is None:
    print("Error: Image could not be loaded!")
else:
    print("Image loaded successfully!")

# -----------------------------------------
# 2. Image Negation
# -----------------------------------------

negative_image = 255 - src_image

# -----------------------------------------
# 3. Thresholding
# -----------------------------------------

_, thresholded_image = cv2.threshold(
    src_image,
    128,
    255,
    cv2.THRESH_BINARY
)

# -----------------------------------------
# 4. Gamma Correction
# -----------------------------------------

gamma = 2.0

normalized_image = src_image / 255.0

gamma_corrected_image = np.power(
    normalized_image,
    1 / gamma
)

gamma_corrected_image = np.uint8(
    gamma_corrected_image * 255
)

# -----------------------------------------
# 5. Apply COLORMAP_HOT
# -----------------------------------------

original_hot = cv2.applyColorMap(src_image, cv2.COLORMAP_HOT)

negative_hot = cv2.applyColorMap(
    negative_image,
    cv2.COLORMAP_HOT
)

threshold_hot = cv2.applyColorMap(
    thresholded_image,
    cv2.COLORMAP_HOT
)

gamma_hot = cv2.applyColorMap(
    gamma_corrected_image,
    cv2.COLORMAP_HOT
)

# Convert BGR to RGB for Matplotlib
original_hot = cv2.cvtColor(original_hot, cv2.COLOR_BGR2RGB)
negative_hot = cv2.cvtColor(negative_hot, cv2.COLOR_BGR2RGB)
threshold_hot = cv2.cvtColor(threshold_hot, cv2.COLOR_BGR2RGB)
gamma_hot = cv2.cvtColor(gamma_hot, cv2.COLOR_BGR2RGB)

# -----------------------------------------
# 6. Display Results
# -----------------------------------------

plt.figure(figsize=(16, 5))

plt.subplot(1, 4, 1)
plt.imshow(original_hot)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(negative_hot)
plt.title("Negative")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(threshold_hot)
plt.title("Threshold")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(gamma_hot)
plt.title("Gamma")
plt.axis("off")

plt.tight_layout()
plt.show()
