import cv2, time
from small_vision import *

# Create an instance of camera 0
cap = cv2.VideoCapture(0)


while True:
    # Get the image from camera 0
    _, image = cap.read()
    
    original = Image(image).resize((640, 480)).show("original")



    copy = original.clone()
    mask = copy.convert_to_hsv().get_mask(
        [27, 100, 100],
        [40, 255, 255]
    )

    # x, y, radius = copy.mask(mask).blur(1).get_largest_blob(mask)
    # if radius > 10:
    #     original.draw_circle((x, y), radius)

    blobs = copy.mask(mask).blur(1).get_blobs(mask)
    for (x, y, radius) in blobs:
        if radius > 20:
            original.draw_circle((x, y), radius, color=(255, 0, 0))
        
    original.show("output")

    if escape_key_pressed():
        break
        

