import cv2
from sight import *

image = cv2.imread("more_fuel.jpg", 1)


original = Image(image).show("original").convert_to_hsv()

mask = original.get_mask(
    [27, 100, 100],
    [40, 255, 255]
)

original.mask(mask).draw_targets(mask).convert_to_bgr().show("output")


wait_for_keypress()
exit()