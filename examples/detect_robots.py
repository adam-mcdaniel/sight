import cv2
from small_vision import *


image = Image(cv2.imread("robots3.jpg", 1)).resize((800, 600))


while True:
    original = image.clone()
    output = image.clone()

    mask = output.get_mask(
        [0, 20, 100],
        [59, 43, 255]
    )

    blobs = output.mask(mask).smooth().blur(0.3).draw_targets(mask).get_blobs(mask)
    
    blobs = sorted(
                blobs,
                key=lambda t: t[2],
                reverse=True
                )[:3]

    for (x, y, radius) in blobs:
        if radius > 20:
            # output.draw_text((x-radius/output.get_width(), y), 'Red Bot')
            original.draw_text(
                (
                    x-radius/output.get_width(),
                    y-radius/output.get_height()
                ), 'Red Bot')
    
    original.show("overlay")

    if escape_key_pressed():
        break

exit()