# Tutorial #18
# ------------
#
# A demonstration of SIFT Detector and Descriptor for object recognition. Inspired by
# https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html and
# https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html

import cv2
import numpy as np
# Initialize images
# Load object image as color image
img_object = cv2.imread('./tutorials/data/images/sift_object01.jpg', cv2.IMREAD_COLOR)

# Extract shape of the image
rows_obj, cols_obj, dims_obj = img_object.shape

# Create a greyscale image for the corner detection
img_obj_gray = cv2.cvtColor(img_object, cv2.COLOR_BGR2GRAY)

# Create a window and show loaded image
window_object = 'Object image'
cv2.namedWindow(window_object, cv2.WINDOW_GUI_NORMAL)
cv2.resizeWindow(window_object, cols_obj, rows_obj)
cv2.imshow(window_object, img_object)

# Load table image as color image
img_table = cv2.imread('./tutorials/data/images/sift_table01.jpg', cv2.IMREAD_COLOR)

# Extract shape of the image
rows_table, cols_table, dims_table = img_object.shape

# Create a greyscale image for the corner detection
img_table_gray = cv2.cvtColor(img_table, cv2.COLOR_BGR2GRAY)

# Create a window and show loaded image
window_table = 'Table image'
cv2.namedWindow(window_table, cv2.WINDOW_GUI_NORMAL)
cv2.resizeWindow(window_object, cols_table, rows_table)
cv2.imshow(window_table, img_table)

print('Loading images done.')
# wait until key pressed
cv2.waitKey(0)

# Do the feature detection with SIFT
# TODO Create a SIFT detector for 500 features (see https://docs.opencv.org/4.x/d7/d60/classcv_1_1SIFT.html)

detector = cv2.SIFT_create(nfeatures=500)

# TODO Detect features and compute descriptors in both images with detectAndCompute
keypoints_obj, descriptors_obj = detector.detectAndCompute(img_obj_gray, None)
keypoints_table, descriptors_table = detector.detectAndCompute(img_table_gray, None)

# TODO Draw detected feature points in both images and show them
img_object = cv2.drawKeypoints(img_obj_gray,
                               keypoints_obj,
                               img_object,
                               flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

img_table = cv2.drawKeypoints(img_table_gray,
                              keypoints_table,
                              img_table,
                              flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.imshow(window_object, img_object)
cv2.imshow(window_table, img_table)

print('Feature detection done.')
cv2.waitKey(0)

# Do the feature matching with a brute force matcher
bf = cv2.BFMatcher()
matches = bf.knnMatch(descriptors_obj, descriptors_table, k=2)

# Store all the good matches as per Lowe's ratio test.
good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])

# TODO Draw matches with cv2.drawMatchesKnn
img_matching = cv2.drawMatchesKnn(img_object,
                                  keypoints_obj,
                                  img_table,
                                  keypoints_table,
                                  good,
                                  None,
                                  flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
window_matching = 'Matching'

cv2.namedWindow(window_matching)
cv2.resizeWindow(window_matching, img_matching.shape[0], img_matching.shape[1])
cv2.imshow(window_matching, img_matching)

print('Matching images done.')
cv2.waitKey(0)

# Compute and visualize the homography based on the matching
# Check if there are enough good matches
MIN_MATCH_COUNT = 10
RANSAC_REPROJECTION_THRESHOLD = 3.0

if len(good) > MIN_MATCH_COUNT:
    # Extract coordinates from the keypoints
    src_pts = np.float32([keypoints_obj[m[0].queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([keypoints_table[m[0].trainIdx].pt for m in good]).reshape(-1, 1, 2)
    # TODO Find the homography with RANSAC
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, RANSAC_REPROJECTION_THRESHOLD)
    print("\nTransformation matrix\n", "\n".join(["\t".join(["%03.3f" % cell for cell in row]) for row in M]))
    # TODO Draw the outline of the object into the table image
    h, w, d = img_object.shape
    # Step 1: take the image corners of the object image
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    # Step 2: transform the corners with the found homography
    dst = cv2.perspectiveTransform(pts, M)
    # Step 3: draw the outline with polylines
    img_table = cv2.polylines(img_table, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
else:
    print("Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))
    mask = None

draw_params = dict(
    matchColor=(0, 255, 0),  # Draw matches in green color
    singlePointColor=None,
    matchesMask=mask,  # Draw only inliers
    flags=2,
)

# TODO Draw only the good matches in green using drawMatchesKnn with matchColor and matchesMask
img_matching = cv2.drawMatchesKnn(img_object, keypoints_obj, img_table, keypoints_table, good, None, **draw_params)


cv2.imshow(window_matching, img_matching)
print('Homography computation done.')
cv2.waitKey(0)
cv2.destroyAllWindows()
