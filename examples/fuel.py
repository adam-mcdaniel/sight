import cv2
from small_vision import *

image = cv2.imread("fuel.png", 1)


original = Image(image).show("original").convert_to_hsv()

# HSV mask for neon yellow
mask = original.get_mask(
    [27, 100, 100],
    [40, 255, 255]
)

original.mask(mask).smooth().blur(1).draw_target(mask).convert_to_bgr().show("output")


wait_for_keypress()
exit()