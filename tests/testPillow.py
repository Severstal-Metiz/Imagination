from PIL import Image, ImageFilter, ImageChops, ImageMath
import numpy as np
import math as m

def sinMaskTop(row):
    value = 255
    newRow = np.zeros((row.size))
    for i in range(1,row.size):
        newRow[i] = value * m.sin(i/row.size*m.pi)
    return newRow

def MaskGen(ChanelImg, formula):
    ChanelImg = ChanelImg.convert(mode='L')
    npMask = np.asarray(ChanelImg)
    npMask = np.asarray([sinMaskTop(row) for row in npMask])
    imgMask = Image.fromarray(npMask).convert('L')
    #imgMaskInvers = imgMask.point(lambda x: 255-x)
    #imgBlank = ChanelImg.point(lambda _: 0)
    imgMackRot = imgMask.rotate(90,expand=True)
    imgMackRot = imgMackRot.resize((imgMask.size))
    imgMask = ImageMath.eval(formula,a=imgMask,b=imgMackRot).convert(mode='L') # '(a+b)/2'
    return imgMask

InputImage = Image.open('2_wm.jpg')
InputImage.load()
InputImage = InputImage.convert(mode='RGB')

#maskImg = MaskGen(Red,'(a+b)*5/8-80')
maskImg = MaskGen(InputImage,'(a+b)/2')
#maskImg = MaskGen(Red,'(a+b)-50')
#maskImg = MaskGen(Red,'a+b-127')

BlureImage = InputImage.filter(ImageFilter.GaussianBlur(20))
InputImage = Image.composite(InputImage,BlureImage,maskImg)

Red, Green, Blue = InputImage.split()

RedOffset = ImageChops.offset(Red,5,0)

Red = Image.composite(Red,RedOffset,maskImg)

ImgOutput = Image.merge('RGB',(Red, Green,Blue))
#ImgOutput = maskImg

ImgOutput.show()