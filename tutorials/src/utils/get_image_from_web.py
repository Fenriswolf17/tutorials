# hint about reading image data came from here:
# https://stackoverflow.com/questions/17170752/python-opencv-load-image-from-byte-string

import cv2
import numpy as np
import os
from duckduckgo_search import DDGS
from fastcore.all import *
from fastdownload import download_url

ddgs = DDGS()
max_images = 30
dest = 'temp.jpg'


# grab some image from the web and optionally save it
def grab_image(query, save_image=False, filename="image.jpg"):
    # using DDG
    urls = L(ddgs.images(keywords=query, max_results=max_images)).itemgot('image')
    #response = requests.get("https://source.unsplash.com/random{0}".format(html.escape(query)))
    # TODO: Check if url ends with jpg
    print("Downloading image:",urls[0])
    input("Press Enter to continue...")
    download_url(urls[0], dest, show_progress=True)
    img = cv2.imread(dest, cv2.IMREAD_COLOR)
    cv2.imshow("result", img)
    if save_image:
        print("saving image to " + filename)
        # check if folder exists otherwise create it
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        cv2.imwrite(filename, img)
    cv2.waitKey(0)
    return img
