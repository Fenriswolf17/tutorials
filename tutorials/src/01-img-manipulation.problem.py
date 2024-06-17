# Exercise #1
# -----------
#
# Load, resize and rotate an image. And display it to the screen.

# TODO First step is to import the opencv module which is called 'cv2'
import cv2
# TODO Check the opencv version
print(cv2.__version__)
# TODO Load an image with image reading modes using 'imread'
# cv2.IMREAD_UNCHANGED  - If set, return the loaded image as is (with alpha
#                         channel, otherwise it gets cropped). Ignore EXIF
#                         orientation.
# cv2.IMREAD_GRAYSCALE  - If set, always convert image to the single channel
#                         grayscale image (codec internal conversion).
# cv2.IMREAD_COLOR      - If set, always convert image to the 3 channel BGR
#                         color image.

image = cv2.imread(r"C:\Users\FCHar\source\tutorials\tutorials\data\images\Bumbu_Rawon.jpg", cv2.IMREAD_COLOR)
# TODO Resize image with 'resize'
width = 600
height = 400
size = (width, height)
image = cv2.resize(image, size)

# TODO Rotate image (but keep it rectangular) with 'rotate'
image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# TODO Save image with 'imwrite'
cv2.imwrite("img_tutorial01.jpg", image)

# TODO Show the image with 'imshow'
title = "OpenCV Python Tutorial"

cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

