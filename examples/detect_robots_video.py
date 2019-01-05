import cv2
from small_vision import *


cap = cv2.VideoCapture("video.mp4")


def get_closest_red_bot(image):
    mask = image.get_mask(
        [0, 20, 100],
        [59, 43, 255]
    )

    return image.mask(mask).smooth().blur(0.5).get_largest_blob(mask)
    

def get_cubes(image):
    mask = image.convert_to_hsv().get_mask(
        [25, 142, 191],
        [35, 255, 255]
    )
    
    return filter(lambda t: t[2] > 10, image.mask(mask).smooth().blur(0.5).convert_to_bgr().get_blobs(mask))
    


while True:
    # Get the image from camera 0
    _, image = cap.read()
    image = Image(image).resize((480, 320))

    original = image.clone()


    x, y, radius = get_closest_red_bot(image.clone())
    if radius > 8:
        original.draw_text(
            (
                x-radius/original.get_width(),
                y-radius/original.get_height()
            ), 'Red Bot', color=(255, 0, 0))


    cubes = get_cubes(image.clone())
    for x, y, radius in cubes:
        original.draw_text(
            (
                x-radius/original.get_width(),
                y-radius/original.get_height()
            ), 'Cube', color=(0, 0, 255))
    
    original.show("overlay")

    if escape_key_pressed():
        break

exit()