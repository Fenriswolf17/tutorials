# Exercise #8
# -----------
#
# Demonstrating how to do template matching in OpenCV.

# Template matching, originally with objects from the image. Typical example
# is counting blood cells
import cv2
import numpy as np

use_color = True

if use_color:
    """"""
    # TODO Load image and template image, note that the template has been
    # manually cut out of the image

    img_color = cv2.imread("./tutorials/data/images/chewing_gum_balls05.jpg", cv2.IMREAD_COLOR)
    template = cv2.imread("./tutorials/data/images/cgb_yelllow.jpg", cv2.IMREAD_COLOR)

    # TODO Read shape of the template and original image
    h, w, c = template.shape
    H, W, C = img_color.shape

else:
    # TODO Load image and template image, note that the template has been
    # manually cut out of the image

    # TODO Read shape of the template and original image

    # TODO Define template matching methods,
    # See https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d for the
    # math behind each method
    pass
methods = [
    cv2.TM_CCORR_NORMED]

    # TODO Loop over all methods in order to compare them
for method in methods:
    
    img = img_color.copy()

    # TODO (In loop) do the template matching
    match_img = cv2.matchTemplate(img, template, method)

    # TODO (in loop) get all matching locations

    match_bin = cv2.threshold(match_img, 0.935, 1.0, cv2.THRESH_BINARY)[1]

    match_bin = np.uint8(match_bin * 255)

    # TODO (In loop) draw rectangle at found location
    connectivity = 8
    (numLabels, labels, stats, centroids) = cv2.connectedComponentsWithStats(match_bin, connectivity, cv2.CV_16F)
    print(numLabels)
    for i in range(1, numLabels):
        pos_x = stats[i, cv2.CC_STAT_LEFT]
        pos_y = stats[i, cv2.CC_STAT_TOP]
        size_x = stats[i, cv2.CC_STAT_WIDTH]
        size_y = stats[i, cv2.CC_STAT_HEIGHT]

        cv2.rectangle(img,(pos_x, pos_y), (pos_x + w, pos_y + h), [0, 255, 0])
    # TODO (In loop) show original image with found location

    # TODO (In loop) show image with the template matching result for all pixels
    cv2.imshow('Template matching result', match_bin)
    cv2.imshow('Original Image', img)

    # (in loop) just press any key to show the next image
    cv2.waitKey(0)

cv2.destroyAllWindows()
