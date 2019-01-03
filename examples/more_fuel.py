import cv2
from vision_lib import Image

image = cv2.imread("more_fuel.jpg", 1)


original = Image(image).show("original").convert_to_hsv()

mask = original.get_mask(
    [27, 100, 100],
    [40, 255, 255]
)

original.mask(mask).draw_targets(mask).convert_to_bgr().show("output")


cv2.waitKey(0)

cv2.destroyAllWindows()