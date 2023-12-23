import gradio as gr
import KernelGenerator as G

def view():
    with gr.Row():
        with gr.Column(scale=3):
            blureRadius = gr.Slider(0, 20, step=1, value=5, label='Blure')
        with gr.Column(scale=10):
            with gr.Row():
                input_img = gr.Image(type="pil",width=500)
                output_img = gr.Image(type="pil",width=500)
                output_imgInv = gr.Image(type="pil",width=500)
            btn = gr.Button("Сделай красиво")
            btn.click(fn=G.KernIt, inputs=[input_img,blureRadius], outputs=[output_img,output_imgInv])