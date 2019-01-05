import cv2
import numpy as np


class Image:
    def __init__(self, image):
        self.data = image

    def clone(self):
        return type(self)(self.data.copy())

    def show(self, window_name, size=None):
        if size:
            resized_image = cv2.resize(
                self.data,
                (
                    int(size[0]),
                    int(size[1])
                )
            )
            cv2.imshow(window_name, resized_image)
        else:
            cv2.imshow(window_name, self.data)
        return self

    def resize(self, size):
        self.data = cv2.resize(
            self.data,
            (
                int(size[0]),
                int(size[1])
            )
        )
        return self

    # gets rid of specs, and closes holes in image
    def smooth(self):
        # create morph kernel
        morphkernel = np.ones((3, 3), np.uint8)
        # removes specs
        self.data = cv2.morphologyEx(
            self.data, cv2.MORPH_OPEN, morphkernel
        )
        # removes holes
        self.data = cv2.morphologyEx(
            self.data, cv2.MORPH_CLOSE, morphkernel
        )
        return self

    # gaussian blur on image on range 0 to 1
    def blur(self, blur_percentage):
        if blur_percentage > 1:
            raise Exception("Attempted to blur more than 100% blur")
        if blur_percentage < 0:
            raise Exception("Attempted to negatively blur")
        v = blur_percentage
        v *= 100
        v = int(v)
        # make blur value odd
        v = v if v % 2 == 1 else v + 1

        self.data = cv2.GaussianBlur(
            self.data, (v, v), 0
        )
        return self

    # Filter image with mask
    def mask(self, mask):
        self.data = cv2.bitwise_and(
            self.data,
            self.data,
            mask=mask
        )
        return self

    def draw_text(self, bottom_corner, text, color=(0, 255, 255), size=1):
        font                   = cv2.FONT_HERSHEY_SIMPLEX
        fontScale              = size
        lineType               = 2

        bottom_corner = (
            int(bottom_corner[0] * int(self.get_width())),
            int(bottom_corner[1] * int(self.get_height())),
        )

        cv2.putText(self.data, text, 
            bottom_corner,
            font, 
            size,
            color,
            lineType
            )

        return self

    def draw_circle(self, center, radius, color=(0, 255, 255), thickness=10):
        if center[0] > 1:
            raise Exception("X location for draw_circle out of bounds (needs to be between 0 and 1)")
        if center[0] < 0:
            raise Exception("X location for draw_circle out of bounds (needs to be between 0 and 1)")
            
        if center[1] > 1:
            raise Exception("Y location for draw_circle out of bounds (needs to be between 0 and 1)")
        if center[1] < 0:
            raise Exception("Y location for draw_circle out of bounds (needs to be between 0 and 1)")

        center = (
            int(center[0] * int(self.get_width())),
            int(center[1] * int(self.get_height())),
        )
        cv2.circle(self.data, center, radius, color, thickness)
        return self

    def draw_target(self, mask, color=None, thickness=None):
        x, y, radius = self.get_largest_blob(mask)

        if (x or y) and radius > 10:
            args = []
            if color:
                args.append(color)
            if thickness:
                args.append(color)
            self.draw_circle(
                (x, y), radius, *args
            )

        return self

    def draw_targets(self, mask, color=None, thickness=None):
        blobs = self.get_blobs(mask)
        for blob in blobs:
            x, y, radius = blob

            if (x or y) and radius > 10:
                args = []
                if color:
                    args.append(color)
                if thickness:
                    args.append(color)
                self.draw_circle(
                    (x, y), radius, *args
                )
                
        return self

    def get_size(self): return self.data.shape[:2][::-1]
    def get_height(self): return self.data.shape[0]
    def get_width(self): return self.data.shape[1]

    # get mask for values range a to b
    def get_mask(self, a, b):
        mask = cv2.inRange(
            self.data,
            np.array(a),
            np.array(b)
            )
        return mask
    
    def get_blobs(self, mask):
        # find irregular shapes using mask
        contours = cv2.findContours(
            mask,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE
        )[1]

        blobs = []    

        # if there is one or more contours
        if len(contours) > 0:
            for contour in contours:
                (x, y), radius = cv2.minEnclosingCircle(contour)
                x = int(x) / int(self.get_width())
                y = int(y) / int(self.get_height())
                radius = int(radius)

                blobs.append(
                    (x, y, radius)
                    )

        return blobs
    
    def get_largest_blob(self, mask):
        # find irregular shapes using mask
        contours = cv2.findContours(
            mask,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE
        )[1]

        x = y = radius = 0
        # if there is one or more contours
        if len(contours) > 0:
            # get shape with max area
            contour = max(
                contours,
                key=cv2.contourArea
                )
        
            (x, y), radius = cv2.minEnclosingCircle(contour)
            x = int(x) / int(self.get_width())
            y = int(y) / int(self.get_height())
            radius = int(radius)

        return x, y, radius

    def convert_to_hsv(self):
        self.data = cv2.cvtColor(
            self.data,
            cv2.COLOR_BGR2HSV
        )
        return HSV_Image(
            self.data
        )

    def convert_to_gray(self):
        self.data = cv2.cvtColor(
            self.data,
            cv2.COLOR_BGR2GRAY
        )
        return Gray_Image(
            self.data
        )

    def convert_to_bgr(self):
        return self


class HSV_Image(Image):
    def convert_to_hsv(self):
        return self

    def convert_to_gray(self):
        self.data = cv2.cvtColor(
            self.data,
            cv2.COLOR_HSV2BGR
        )
        self.data = cv2.cvtColor(
            self.data,
            cv2.COLOR_BGR2GRAY
        )
        return Gray_Image(
            self.data
        )

    def convert_to_bgr(self):
        self.data = cv2.cvtColor(
            self.data,
            cv2.COLOR_HSV2BGR
        )
        return Image(
            self.data
        )


class Gray_Image(Image):
    pass