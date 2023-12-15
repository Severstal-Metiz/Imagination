from PIL import Image, ImageFilter, ImageChops, ImageMath
import numpy as np
import math as m

def sinMaskTop(row):
    value = 200
    newRow = np.zeros((row.size))
    for i in range(1,row.size):
        newRow[i] = value * m.sin(i/row.size*m.pi)
    return newRow

def MaskGen(ChanelImg):
    npMask = np.asarray(ChanelImg)
    npMask = np.asarray([sinMaskTop(row) for row in npMask])
    imgMask = Image.fromarray(npMask).convert('L')
    imgMaskInvers = imgMask.point(lambda x: 255-x)
    imgBlank = ChanelImg.point(lambda _: 0)
    imgMackRot = imgMask.rotate(90,expand=True)
    imgMackRot = imgMackRot.resize((imgMask.size))
    imgMask = ImageMath.eval('(a+b)/2',a=imgMask,b=imgMackRot).convert(mode='L')
    return imgMask

InputImage = Image.open('2_wm.jpg')
InputImage.load()
InputImage = InputImage.convert(mode='RGB')

Red, Green, Blue = InputImage.split()

RedOffset = ImageChops.offset(Red,5,0)

maskImg = MaskGen(Red)

Red = Image.composite(Red,RedOffset,maskImg)

ImgOutput = Image.merge('RGB',(Red, Green,Blue))
#ImgOutput = maskImg

ImgOutput.show()