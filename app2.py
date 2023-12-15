import gradio as gr
from PIL import Image, ImageFilter
import numpy as np
import random

def numpyMagic(img):
  

    return imgexit


with gr.Blocks(title="УРА ТОВАРИЩИ!") as demo:
    with gr.Column(scale=10):
            with gr.Row():
                input_img = gr.Image(type="pil",width=500)
                output_img = gr.Image(type="pil",width=500)
            btn = gr.Button("Сделай красиво")
            btn.click(fn=numpyMagic, inputs=input_img, outputs=output_img)
            
            
demo.launch(inbrowser=True, server_port=7860)
