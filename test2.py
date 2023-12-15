from PIL import Image, ImageFilter
import numpy as np
import random

def InRed(dest,sours1, sours2=0,sours3=0):
    dest[:,:,0] = sours1 + sours2 + sours3
def InGreen(dest,sours1, sours2=0,sours3=0):
    dest[:,:,1]  = sours1 + sours2 + sours3
def InBlue(dest,sours1, sours2=0,sours3=0):
    dest[:,:,2] = sours1 + sours2 + sours3
def FromSource(imgSourse, redVal, greenVal, blueVal):
    dest = imgSourse[:,:,0]*redVal + imgSourse[:,:,1]*greenVal + imgSourse[:,:,2]*blueVal
    return dest

    


rawImg = Image.open('E:/РОМАН/!хрень/1_wm.png')
rawImg.load()
rawImg = rawImg.convert(mode='RGB')
inputImg = np.asarray(rawImg,dtype=np.uint16) #, dtype=np.int16)

width=rawImg.width
height=rawImg.height
newImg = np.zeros((height, width, 3),dtype=np.uint8)

redArray = FromSource(inputImg,1,0,0)
greenArray = FromSource(inputImg,0,1,0)
blueArray = FromSource(inputImg,0,0,1)


#эфекты на пиксели
def fr(y):
    y = y #y/2 + random.randint(0,128)
    if y>255: return 255
    else: return y
def fg(y):
    y = y
    if y>255: return 255
    else: return y
def fb(y):
    y = y
    if y>255: return 255
    else: return y


#Comprehension
redArray = np.array([[fr(xi) for xi in row] for row in redArray])
greenArray = np.array([[fg(xi) for xi in row] for row in greenArray])
blueArray = np.array([[fb(xi) for xi in row] for row in blueArray])


#работа с цветом фильр или замена цвета
#newImg[:,:,0] = redArray
InRed(newImg,redArray)
InGreen(newImg,greenArray)
InBlue(newImg, blueArray)


rawImgOutput =  Image.fromarray(newImg)
rawImgOutput.show()