import cv2
from vision_lib import *

# Read image from file
image = cv2.imread("fuel.png", 1)

# Convert to Image
# Show image
# Convert image to HSV
original = Image(image).show("original").convert_to_hsv()

# HSV mask for neon yellow
mask = original.get_mask(
    [27, 100, 100],
    [40, 255, 255]
)

# Mask image
# Smooth image
# Gaussian Blur image
original.mask(mask).smooth().blur(1)


# print the relative location and radius of largest blob
print("largest blob: ({}, {}) radius: {}".format(
    *original.get_largest_blob(mask)
    )
)

# print total number of blobs
print("total number of blobs:",
    len(original.get_blobs(mask))
)


# Draw target around largest contour
# Convert to BGR
# Show output
original.draw_target(mask).convert_to_bgr().show("output")



wait_for_keypress()
exit()