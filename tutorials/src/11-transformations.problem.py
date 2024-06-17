# Tutorial #11
# ------------
#
# Geometric transformations a.k.a. image warping.

import numpy as np
import cv2

# Load image and resize for better display
img = cv2.imread("./tutorials/data/images/nl_clown.jpg", cv2.IMREAD_COLOR)
img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_CUBIC)
rows, cols, dims = img.shape

# TODO Define translation matrix for translation about 100 pixels to the right and 50 up
T_translation = np.float32([[1,0,100], [0,1,50]])

# A pretty print for the matrix:
print("\nTranslation\n", "\n".join(["\t".join(["%03.3f" % cell for cell in row]) for row in T_translation]))

# TODO Apply translation matrix on image using cv2.warpAffine
dst_translation = cv2.warpAffine(img, T_translation, (rows, cols))

# TODO Define anisotropic scaling matrix that stretches to double length horizontally
# and squeezes vertically to the half height
T_anisotropic_scaling = np.float32([[2,0,0], [0,0.5,0]])

print(
    "\nAnisotropic scaling\n",
    "\n".join(["\t".join(["%03.3f" % cell for cell in row]) for row in T_anisotropic_scaling]),
)

# TODO Apply anisotropic scaling matrix on image using cv2.warpAffine
dst_anisotropic_scaling = cv2.warpAffine(img, T_anisotropic_scaling, (int(rows*2), int(cols*0.5)))

# TODO Define rotation matrix for 45° clockwise rotation
radian = (np.pi/180) * 45 
T_rotation = np.float32([[np.cos(radian),np.sin(radian),0], [-np.sin(radian), np.cos(radian),0]])

print("\nRotation\n", "\n".join(["\t".join(["%03.3f" % cell for cell in row]) for row in T_rotation]))

# TODO Apply rotation matrix on image using cv2.warpAffine
dst_rotation = cv2.warpAffine(img, T_rotation, (rows, cols))

# TODO Rotate around image center for 45° counterclockwise using cv2.getRotationMatrix2D
center_row = rows//2
center_col = cols//2
center = center_row, center_col
T_rotation_around_center = cv2.getRotationMatrix2D(center, 45, 1)

print(
    "\nRotation around center\n",
    "\n".join(["\t".join(["%03.3f" % cell for cell in row]) for row in T_rotation_around_center]),
)

# TODO Apply rotatio matrix on image using cv2.warpAffine
dst_rotation_around_center = cv2.warpAffine(img, T_rotation_around_center, (rows, cols))

# Show the original and resulting images
cv2.imshow("Original", img)
cv2.imshow("Translation", dst_translation)
cv2.imshow("Anisotropic scaling", dst_anisotropic_scaling)
cv2.imshow("Rotation", dst_rotation)
cv2.imshow("Rotation around center", dst_rotation_around_center)

# Keep images open until key pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
