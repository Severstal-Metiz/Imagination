import gradio as gr
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

def Glich(InputImage,shift,blureRadius,chBox):
    global maskImg
    BlureImage = InputImage.filter(ImageFilter.GaussianBlur(int(blureRadius)))
    InputImage = Image.composite(InputImage,BlureImage,maskImg)
    
    Red, Green, Blue = InputImage.split()

    RedOffset = ImageChops.offset(Red,int(shift),0)

    if chBox:
        Red = Image.composite(Red,RedOffset,maskImg)
    else:
        Red = RedOffset
    
    ImgOutput = Image.merge('RGB',(Red, Green,Blue))
    #ImgOutput = maskImg

    return ImgOutput

def ImgLoad(InputImage,shift,blureRadius,chBox):
    global maskImg
    InputImage = InputImage.convert(mode='RGB')
    maskImg = MaskGen(InputImage,'(a+b)/2')
    ImgOutput = Glich(InputImage,shift,blureRadius,chBox)
    return ImgOutput


with gr.Blocks(title="УРА ТОВАРИЩИ!") as demo:
    with gr.Row():
        with gr.Column(scale=3):
            shift = gr.Slider(0, 10, step=1, value=5,label='Shift')
            blureRadius = gr.Slider(0, 20, step=1, value=5, label='Blure')
            chBox = gr.Checkbox(value=True,label='Add mask')       
        with gr.Column(scale=10):
            with gr.Row():
                input_img = gr.Image(type="pil",width=500)
                output_img = gr.Image(type="pil",width=500)
            btn = gr.Button("Сделай красиво")
            btn.click(fn=Glich, inputs=[input_img,shift,blureRadius,chBox], outputs=output_img)
            input_img.upload(fn=ImgLoad,inputs=[input_img,shift,blureRadius,chBox], outputs=output_img)

            
demo.launch(inbrowser=True, server_port=7860)
