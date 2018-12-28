# -*- coding: utf-8 -*-
"""
The picture cutter. 

Segments pictures into specified dimensions for webtoon, ig, etc. 
"""

from os import listdir, mkdir
from os.path import isdir, isfile, join, exists
from time import time


from PIL import Image


from crop import crop

################# CONFIGURATIONS #####################
# output directories
inputdir = join("input", "example-image.jpg") # can be a file or a directory
outputdir = "output"

# cut dimensions
dim = (200, 200) # (width, height), image will be cut from left to right, top to bottom

################ PREPROCESSING #######################
# makes sure input is either file or directory
assert(isdir(inputdir) or isfile(inputdir)) 

#create output directory if not exist
if not exists(outputdir):
    print("Message: Output folder created.")
    mkdir(outputdir)

# list out image files
inputfiles = []
if (isdir(inputdir)):
    inputfiles = [join(inputdir, fname) for fname in listdir(inputdir)]
    print("Input files: ")
    count = 1
    for fname in inputfiles:
        print("%d. %s" % (count, fname))
        count = count + 1
else:
    inputfiles.append(inputdir)
    print("Input file: %s" % inputfiles[0])  
    
# create output folder
outdirname = "SEGMENTS_%.0f" % time()
print("Message: Cuts will be stored in %s." % join(outputdir, outdirname))
mkdir(join(outputdir, outdirname))

# cut the images
cut = 0
for pic in inputfiles:
    im = Image.open(pic)
    width, height = im.size
    cutx1, cutx2 = 0, width if (dim[0] > width) else dim[0]
    cuty1, cuty2 = 0, height if (dim[1] > height) else dim[1]
    while True:
        while True:
            cut = cut + 1
            saved_location = "panel%d.jpg" % cut
            cropped_image = im.crop((cutx1, cuty1, cutx2, cuty2))
            cropped_image.save(join(outputdir, outdirname, saved_location))
            cutx1 = cutx1 + dim[0]
            if (cutx1 >= width):
                cutx1 = 0
                break
            cutx2 = width if (cutx2 + dim[0] > width) else cutx2 + dim[0]
        cuty1 = cuty1 + dim[1]
        if (cuty1 >= height):
            break
        cutx2 = width if (dim[0] > width) else dim[0]
        cuty2 = height if (cuty2 + dim[1] > height) else cuty2 + dim[1]
        