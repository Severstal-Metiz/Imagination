import gradio as gr
from PIL import Image, ImageFilter
import numpy as np
import random
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

def InRed(dest,sours1, sours2=0,sours3=0):
    dest[:,:,0] = sours1 + sours2 + sours3
def InGreen(dest,sours1, sours2=0,sours3=0):
    dest[:,:,1]  = sours1 + sours2 + sours3
def InBlue(dest,sours1, sours2=0,sours3=0):
    dest[:,:,2] = sours1 + sours2 + sours3
def FromSource(imgSourse, redVal, greenVal, blueVal):
    dest = imgSourse[:,:,0]*redVal + imgSourse[:,:,1]*greenVal + imgSourse[:,:,2]*blueVal
    return dest

def DefaultColors(inputImg):
    redArray = FromSource(inputImg,1,0,0)
    greenArray = FromSource(inputImg,0,1,0)
    blueArray = FromSource(inputImg,0,0,1)
    return (redArray, greenArray, blueArray)

def ChanelRedFromOriginalImage(inputImg):
    redArray = FromSource(inputImg,1,0,0)
    return redArray



def numpyMagic(gain):
    global redArray
    global greenArray
    global blueArray
    global width
    global height
    global inputImg
    newImg = np.zeros((height, width, 3),dtype=np.uint8)

    #Функциоанал
    redArray = ChanelRedFromOriginalImage(inputImg)* gain

    #Comprehension
    #redArray = np.array([[fr(xi) for xi in row] for row in redArray])
    #greenArray = np.array([[fg(xi) for xi in row] for row in greenArray])
    #blueArray = np.array([[fb(xi) for xi in row] for row in blueArray])
    
    InRed(newImg,redArray)
    InGreen(newImg,greenArray)
    InBlue(newImg, blueArray)

    rawImgOutput =  Image.fromarray(newImg)
    return rawImgOutput

def ImgLoad(rawImg):
    global redArray
    global greenArray
    global blueArray
    global width
    global height
    global inputImg

    rawImg = rawImg.convert(mode='RGB')
    inputImg = np.asarray(rawImg,dtype=np.uint16) #, dtype=np.int16)

    width=rawImg.width
    height=rawImg.height
    newImg = np.zeros((height, width, 3),dtype=np.uint8)

    #Функциоанал
    redArray,greenArray,blueArray=  DefaultColors(inputImg)

    InRed(newImg,redArray)
    InGreen(newImg,greenArray)
    InBlue(newImg, blueArray)


    rawImgOutput =  Image.fromarray(newImg)
    return rawImgOutput


with gr.Blocks(title="УРА ТОВАРИЩИ!") as demo:
    with gr.Column(scale=10):
            redGain = gr.Slider(0, 3, step=0.1, value=1)
            with gr.Row():
                input_img = gr.Image(type="pil",width=500)
                output_img = gr.Image(type="pil",width=500)
            btn = gr.Button("Сделай красиво")
            btn.click(fn=numpyMagic, outputs=output_img)
            redGain.change(fn=numpyMagic,inputs=redGain, outputs=output_img)
            input_img.upload(fn=ImgLoad,inputs=input_img, outputs=output_img)

            
demo.launch(inbrowser=True, server_port=7860)
