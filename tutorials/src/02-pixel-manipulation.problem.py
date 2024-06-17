# Exercise #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of the image to some other place,
# count the used colors in the image

import cv2
import numpy as np

# TODO Loading images in grey and color
image_Gray = cv2.imread(r"C:\Users\FCHar\source\tutorials\tutorials\data\images\Bumbu_Rawon.jpg", cv2.IMREAD_GRAYSCALE)
image_Color = cv2.imread(r"C:\Users\FCHar\source\tutorials\tutorials\data\images\Bumbu_Rawon.jpg", cv2.IMREAD_COLOR)

# TODO Do some print out about the loaded data using type, dtype and shape
print(type(image_Gray))  
print(type(image_Color))

print(image_Gray.dtype)
print(image_Color.dtype)

print(image_Gray.shape)
print(image_Color.shape)
# TODO Continue with the grayscale image
img = image_Gray.copy()
# TODO Extract the size or resolution of the image
height = img.shape[0]
width = img.shape[1]
print("Height = " + str(height)) #alternativ: print("Height = ",height)
print("Width = " + str(width))

# TODO Resize image
img.resize(8, 4) #width, height

# Row and column access, see https://numpy.org/doc/stable/reference/arrays.ndarray.html for general access on ndarrays
# TODO Print first row
print(img[0,:])
# TODO Print first column
print(img[:,0])
# TODO Continue with the color image
img = image_Color.copy()
# TODO Set an area of the image to black
#for i in range(150, 160):
    #for j in range(width):
        #img[i,j] = [0,0,0]
img[150:165,:] = (0,0,0) # oder
# TODO Show the image and wait until key pressed

title = "My Image"

cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)
cv2.imshow(title, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO Find all used colors in the image
all_rgb_codes = img.reshape(-1, img.shape[-1])
unique_rgb_codes = np.unique(all_rgb_codes, axis=0, return_counts=False)
print("Those color values are in the image:\n " + str(unique_rgb_codes))

# TODO Copy one part of an image into another one

# TODO Save image to a file

# TODO Show the image again

# TODO Show the original image (copy demo)
