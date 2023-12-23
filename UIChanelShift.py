import gradio as gr
import ChanelShiftGenerators as G

def view():
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
            btnk = gr.Button("Сделай красиво KERN")
            btn.click(fn=G.Glich, inputs=[input_img,shift,blureRadius,chBox], outputs=output_img)
            btnk.click(fn=G.Kern, inputs=[input_img], outputs=output_img)
            input_img.upload(fn=G.ImgLoad,inputs=[input_img])         

