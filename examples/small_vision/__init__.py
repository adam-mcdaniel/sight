import cv2
from .image import *
from .window import *


def wait_for_keypress():
    cv2.waitKey(0)

def escape_key_pressed():
    return cv2.waitKey(1) & 0xFF == 27

def exit():
    cv2.destroyAllWindows()