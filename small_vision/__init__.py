from .image import *


def wait_for_keypress():
    cv2.waitKey(0)

def exit():
    cv2.destroyAllWindows()