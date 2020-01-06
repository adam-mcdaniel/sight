import cv2
from sight import *

window = Window("output").add_slider("Hue Low", 15, 255).add_slider("Hue High", 59, 255).add_slider("Sat Low", 30, 255).add_slider("Sat High", 250, 255).add_slider("Val Low", 120, 255).add_slider("Val High", 250, 255).add_slider("Blur", 0, 100)

image = Image(cv2.imread("robots4.png", 1)).resize((320, 240))


while True:

    output = image.clone()
    hl, hh, sl, sh, vl, vh, blur = window.get_sliders()

    mask = output.get_mask(
        [hl, sl, vl],
        [hh, sh, vh]
    )

    output.mask(mask).smooth().blur(blur/100).show("output")

    if escape_key_pressed():
        break

exit()