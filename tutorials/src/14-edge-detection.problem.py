# Tutorial #14
# ------------
#
# Compute the edges of an image with the Canny edge detection. Adjust the parameters using sliders.

import numpy as np
import cv2

thresh01 = 10
thresh02 = 100

def show_images_side_by_side(img_A, img_B):
    """Helper function to draw two images side by side"""
    cv2.imshow(window_name, np.concatenate((img_A, img_B), axis=1))
    return


# TODO: Define callback function
def updateCannyT1(value):
    """callback function for the sliders"""
    global thresh01
# Read slider positions
    thresh01 = value
# Blur the image

    updateAndShow()

def updateCannyT2(value):
    """callback function for the sliders"""
    global thresh02
# Read slider positions
    thresh02 = value
# Blur the image

    updateAndShow()

def updateAndShow():
    img_blurred = cv2.blur(img, (5,5))
    # Run Canny edge detection with thresholds set by sliders
    result = cv2.Canny(img_blurred, thresh01, thresh02)
    # Show the resulting images in one window using the show_images_side_by_side function
    show_images_side_by_side(img_blurred, result)

# TODO Load example image as grayscale
img = cv2.imread("./tutorials/data/images/nl_clown.jpg", cv2.IMREAD_GRAYSCALE)
# Resize if needed
img = cv2.resize(img, (400, 400))
# Clone if needed
img_clone = np.copy(img)
# TODO Initial Canny edge detection result creation

result = cv2.Canny(img_clone, thresh01, thresh02)

# Define a window name
window_name = "Canny edge detection demo"

# TODO Create window with sliders
cv2.namedWindow(window_name)
# TODO Show the resulting images in one window
show_images_side_by_side(img, result)
# TODO Create trackbars (sliders) for the window and define one callback function
cv2.createTrackbar("T1:", window_name, 0, 255, updateCannyT1)
cv2.createTrackbar("T2:", window_name, 0, 255, updateCannyT2)

# Wait until a key is pressed and end the application
cv2.waitKey(0)
cv2.destroyAllWindows()
