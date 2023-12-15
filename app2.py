import gradio as gr
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

def DefaultColors(inputImg):
    redArray = FromSource(inputImg,0.2,0,0)
    greenArray = FromSource(inputImg,0,1,0)
    blueArray = FromSource(inputImg,0,0,1)
    return (redArray, greenArray, blueArray)

def numpyMagic(rawImg):
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
            with gr.Row():
                input_img = gr.Image(type="pil",width=500)
                output_img = gr.Image(type="pil",width=500)
            btn = gr.Button("Сделай красиво")
            btn.click(fn=numpyMagic, inputs=input_img, outputs=output_img)

            
demo.launch(inbrowser=True, server_port=7860)
