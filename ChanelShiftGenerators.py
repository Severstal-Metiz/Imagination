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
    imgMackRot = imgMask.rotate(90,expand=True)
    imgMackRot = imgMackRot.resize((imgMask.size))
    imgMask = ImageMath.eval(formula,a=imgMask,b=imgMackRot).convert(mode='L') # '(a+b)/2'
    return imgMask

def Glich(InputImage,shift,blureRadius,chBox):
    global maskImg
    InputImage = InputImage.convert(mode='RGB')
    BlureImage = InputImage.filter(ImageFilter.GaussianBlur(int(blureRadius)))
    InputImage = Image.composite(InputImage,BlureImage,maskImg)
    
    Red, Green, Blue = InputImage.split()

    RedOffset = ImageChops.offset(Red,int(shift),0)
    BlueOffset = ImageChops.offset(Blue,-int(shift),0)

    if chBox:
        Red = Image.composite(Red,RedOffset,maskImg)
        Blue = Image.composite(Blue,BlueOffset,maskImg)
    else:
        Red = RedOffset
        Blue = BlueOffset
    
    ImgOutput = Image.merge('RGB',(Red, Green,Blue))
    #ImgOutput = maskImg

    return ImgOutput
def Kern(InputImage):
    kernel = (-1,0,1,
          -1,0,1,
          -1,0,1,)
    ImgOutput = InputImage.filter(ImageFilter.Kernel((3,3),kernel,1,0))
    return ImgOutput

def ImgLoad(InputImage):
    global maskImg
    maskImg = MaskGen(InputImage,'(a+b)/2')