import cv2


nothing = lambda *a, **k: None

class Window:
    def __init__(self, name):
        self.name = name
        cv2.namedWindow(self.name, cv2.WINDOW_AUTOSIZE)
        self.slider_names = []

    def add_slider(self, name, default=0, max=255):
        self.slider_names.append(name)
        cv2.createTrackbar(
            name,
            self.name,
            default,
            max,
            nothing
            )
        return self

    def get_slider(self, name):
        return cv2.getTrackbarPos(name, self.name)

    def get_sliders(self):
        return list(map(self.get_slider, self.slider_names))
