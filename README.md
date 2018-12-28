# Picture Cutter

Picture cutter is a small python program that takes an image file or a directory to a set of image files, and segment them according to a specified dimension. Useful for making webtoon panels out of a long strip of image or making tiles for instagram etc. 

## Usage

1. Specify the input file

```
################# CONFIGURATIONS #####################
# output directories
inputdir = join("input", "example-image.jpg") # can be a file or a directory
```

2. Specify the size of segments

```
# cut dimensions
dim = (200, 200) # (width, height), image will be cut from left to right, top to bottom
```

3. Run the script. Output will be stored in output/folderName_timestamp. 

folderName can be customized at line 49:

```
# create output folder
outdirname = "SEGMENTS_%.0f" % time()
```

and individual segment image file name can be customized at line 63:

```
saved_location = "panel%d.jpg" % cut
```

## Dependencies

This program requires [PIL](https://pillow.readthedocs.io/en/5.3.x/). I installed it in a [conda](https://conda.io/docs/) environment, which you can get from the [Anaconda distribution](https://www.anaconda.com/download/).
