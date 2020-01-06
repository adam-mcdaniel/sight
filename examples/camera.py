import cv2, time
from sight import *

# Create an instance of camera 0
cap = cv2.VideoCapture(0)


while True:
    # Get the image from camera 0
    _, image = cap.read()
    
    # show untouched image
    # convert to HSV
    original = Image(image).resize((320, 240)).show("original").convert_to_hsv()

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
    original.mask(mask).smooth().blur(0.1).draw_target(mask).convert_to_bgr().show("output")

    if escape_key_pressed():
        break
        
exit()