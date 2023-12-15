from PIL import Image, ImageFilter, ImageChops
import numpy as np
import math as m

def sinMaskTop(row):
    value = 200
    newRow = np.zeros((row.size))
    for i in range(1,row.size):
        newRow[i] = value * m.sin(i/row.size*m.pi)
    return newRow

InputImage = Image.open('2_wm.jpg')
InputImage.load()
InputImage = InputImage.convert(mode='RGB')
#print(InputImage.width)

Red, Green, Blue = InputImage.split()

RedOffset = ImageChops.offset(Red,5,0)

npMask = np.asarray(Red)
npMask = np.asarray([sinMaskTop(row) for row in npMask])
imgMask = Image.fromarray(npMask).convert('L')
imgMaskInvers = imgMask.point(lambda x: 255-x)
imgBlank = Red.point(lambda _: 0)

#imgMask = imgMask.filter(ImageFilter.MinFilter(size=5))

Red = Image.composite(Red,RedOffset,imgMask)
#Red = Image.composite(Red,imgBlank,imgMask)
#Red = imgMaskInvers

ImgOutput = Image.merge('RGB',(Red, Green,Blue))
#ImgOutput = imgMask

ImgOutput.show()