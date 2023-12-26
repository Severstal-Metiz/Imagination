import gradio as gr
import UIpixelSort, UIChanelShift, UiKernel
import multiprocessing as mp


if mp.current_process().name == 'MainProcess':
    with gr.Blocks(title="Лучшая работа в мире!") as demo:
        with gr.Tab("Pixelshift"):
            UIpixelSort.view()
        with gr.Tab("Channels shift"):
            UIChanelShift.view()
        with gr.Tab("Kernel"):
            UiKernel.view()

    demo.launch(inbrowser=True, server_port=7860)