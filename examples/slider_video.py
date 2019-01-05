import cv2, time
from small_vision import *

window = Window("output").add_slider("Hue Low", 30, 255).add_slider("Hue High", 65, 255).add_slider("Sat Low", 120, 255).add_slider("Sat High", 255, 255).add_slider("Val Low", 100, 255).add_slider("Val High", 255, 255).add_slider("Blur", 0, 100)

cap = cv2.VideoCapture("video.mp4")

while True:
    _, image = cap.read()
    image = Image(image).resize((480, 320))


    output = image.clone().convert_to_hsv()
    hl, hh, sl, sh, vl, vh, blur = window.get_sliders()

    mask = output.get_mask(
        [hl, sl, vl],
        [hh, sh, vh]
    )

    image.show("original")
    output.mask(mask).smooth().blur(blur/100).show("output")

    time.sleep(0.05)

    if escape_key_pressed():
        break

exit()