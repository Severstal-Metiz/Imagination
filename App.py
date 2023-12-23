import gradio as gr
import UIpixelSort, UIChanelShift

with gr.Blocks(title="Лучшая работа в мире!") as demo:
    with gr.Tab("Pixelshift"):
        UIpixelSort.view()
    with gr.Tab("Jopa"):
        UIChanelShift.view()
            
demo.launch(inbrowser=True, server_port=7860)