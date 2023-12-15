from PIL import Image, ImageFilter, ImageChops, ImageMath
import numpy as np
import math as m


InputImage = Image.open('2_wm.jpg')
InputImage.load()
InputImage = InputImage.convert(mode='RGB')

kernel = (-1,0,1,
          -1,0,1,
          -1,0,1,)

ImgOutput = InputImage.filter(ImageFilter.Kernel((3,3),kernel,1,0))

ImgOutput.show()