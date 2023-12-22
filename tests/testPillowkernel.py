from PIL import Image, ImageFilter, ImageChops, ImageMath
import numpy as np
import math as m


InputImage = Image.open('2_wm.jpg')
InputImage.load()
InputImage = InputImage.convert(mode='RGB')

kernel1 = (-1,0,1,
          -1,0,1,
          -1,0,1,)
kernel2 = (-1,1,-1,
          1,0,1,
          -1,1,-1,)
kernel3 = (0,-1,0,
          -1,5,-1,
          0,-1,0,)
kernel4 = (-2,-1,0,
          -1,1,1,
          0,-1,2,)
kernel5 = (-2,-1,0,1,2,
            -2,-1,0,1,2,
            -2,-1,0,1,2,
            -2,-1,0,1,2,
            -2,-1,0,1,2,)
kernel6 = (1,2,1,
          2,4,2,
          1,2,1,)
for _ in range(1,10):
    InputImage = InputImage.filter(ImageFilter.Kernel((3,3),kernel6,16,0))
    InputImage = InputImage.filter(ImageFilter.Kernel((3,3),kernel3,1,0))
InputImage = InputImage.filter(ImageFilter.Kernel((5,5),kernel5,1,0))
#ImgOutput = ImgOutput.point(lambda x: x/16)
#ImgOutput = ImgOutput.point(lambda x: x+127)

InputImage.show()