


import cv2, time
from small_vision import *

# Create an instance of camera 0
cap = cv2.VideoCapture(0)


while True:
    # Get the image from camera 0
    _, image = cap.read()
    
    original = Image(image).resize((320, 240)).show("original")



    copy = original.clone()
    mask = copy.convert_to_hsv().get_mask(
        [27, 100, 100],
        [40, 255, 255]
    )

    blobs = copy.mask(mask).blur(1).get_blobs(mask)
    
    for (x, y, radius) in blobs:
        if radius > 10:
            original.draw_circle((x, y), radius)
        
    original.show("output")

    if escape_key_pressed():
        break
        

