import cv2
from sight import *

image = cv2.imread("fuel.png", 1)


# show untouched image
# convert to HSV
original = Image(image).show("original").convert_to_hsv()

# HSV mask for neon yellow
mask = original.get_mask(
    [27, 100, 100],
    [40, 255, 255]
)

# apply mask
# blur 100%
# draw circle around the largest blob
# convert back to BGR
# show image
original.mask(mask).blur(1).draw_target(mask).convert_to_bgr().show("output")


wait_for_keypress()
exit()