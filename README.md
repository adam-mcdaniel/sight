# small-vision
A tool for Vision Processing

## What is small-vision?
---

Small-vision is really just a library built on top of OpenCV. It abstracts away all of the awful C-like garbage, and makes it look more rust-like. Here's what I mean.

If I want to read an image from a file, show the original image, convert it to HSV, apply a mask, apply a gaussian blur, draw a circle around the largest blob, convert it back to BGR, and output the image, that can be done very concisely, like this:
```python
import cv2
from small_vision import *

image = cv2.imread("fuel.png", 1)


# show untouched image
# convert to HSV
original = Image(image).show("original").convert_to_hsv()

# HSV mask for neon yellow
mask = original.get_mask(
    [27, 100, 100],
    [40, 255, 255]
)

# apply mask
# blur 100%
# draw circle on the largest blob
# convert to HSV
# convert back to BGR
# show image
original.mask(mask).blur(1).draw_target(mask).convert_to_bgr().show("output")


wait_for_keypress()
exit()
```

See how easy that was?


You might be thinking that it's too high level to be useful. This is not so.

You can use methods like `get_blobs`, `get_largest_blob`, and several others to get the data you're looking for.

## Documentation
---

```python
# returns whether or not escape key pressed (True or False)
def escape_key_pressed()

# waits for keypress
def wait_for_keypress()

# destroys windows
def exit()

class Image:    
    # Takes an opencv image (a numpy ndarray)
    def __init__(self, image)

    # Shows this image under a given window name and a size
    def show(self, window_name, size=None)

    # Resizes the image to a given size
    def resize(self, size)

    # gets rid of specs and closes holes in image
    def smooth(self)

    # gaussian blur on image using a percentage
    def blur(self, blur_percentage)

    # filter image with mask
    def mask(self, mask)

    # draw circle with center location and radius on image
    def draw_circle(self, center, radius)

    # draws circle around the largest blob using a mask
    def draw_target(self, mask)

    # draws circles around each blob using a mask
    def draw_targets(self, mask)

    # returns image width
    def get_width(self)

    # returns image height
    def get_height(self)

    # returns image (width, height)
    def get_size(self)

    # get mask for values range a to b
    # a and b are both lists 3 values long
    # a is the lower limit for each channel in the image
    # b is the upper limit for each channel in the image
    def get_mask(self, a, b)

    # returns a list of (x, y, radius) for each blob using a mask
    def get_blobs(self, mask)

    # returns a (x, y, radius) for the largest blob using a mask
    def get_largest_blob(self, mask)

    # converts image to HSV image
    def convert_to_hsv(self)

    # converts image to Gray image
    def convert_to_gray(self)

    # converts image to BGR image
    def convert_to_bgr(self)
```

## Install Dependencies
---
```bash
python3 -m pip install opencv-python
python3 -m pip install numpy
```


## Future
---
I plan to develop this further to add features such as multithreaded, multiscaling template matching, and haarcascades.

Other than that there's not much else to add, the base code is super small yet powerful, and flexible to change.