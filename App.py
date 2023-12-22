import gradio as gr
import Generators as G
temppath = 'temp/'


def interval_functionddChange(interval_function):
    visclength = False
    visLower = False
    visUpper = False
    visInterval_image = False
    if ("random" in interval_function) or ("waves" in interval_function):
        visclength = True
    if ("threshold" in interval_function) or ("edges" in interval_function):
        visLower = True
    if ("threshold" in interval_function):
        visUpper = True
    if ("file" in interval_function) or ("file-edges" in interval_function):
        visInterval_image = True
    print(interval_image)
    return gr.Slider(visible=visclength,interactive=True), gr.Slider(visible=visLower,interactive=True), gr.Slider(visible=visUpper,interactive=True),gr.Image(visible=visInterval_image,interactive=True)


with gr.Blocks(title="Лучшая работа в мире!") as demo:
    with gr.Row():
        with gr.Column(scale=1,variant="panel"):
            with gr.Group():
                sorting_function = gr.Dropdown(
                    ["lightness", "hue", "saturation", "intensity", "minimum"],label="sorting_function", info="Sorting function to use for sorting the pixels.",value = "lightness"
                )
                randomness = gr.Slider(0, 100, step=0.1,label="Randomness", info="Percentage of intervals NOT to sort")
                angle = gr.Slider(0, 360, step=10,label="Angle", info="Angle at which you're pixel sorting in degrees.")                
            with gr.Group():
                interval_function = gr.Dropdown(
                    ["random", "threshold", "edges", "waves", "file", "file-edges", "none"],label="interval_function", info="Controls how the intervals used for sorting are defined.", value = "random"
                )
                clength = gr.Slider(2, 100, step=1, value=14, label="char_length", info="Characteristic length for the random width generator. Used in mode `random` and `waves`.")
                thresholdLower  = gr.Slider(0, 1, step=0.1, value=0.25, label="Threshold (Lower)", info="How dark must a pixel be to be considered as a 'border' for sorting? Used in edges and threshold modes.", visible=False)
                thresholdUpper  = gr.Slider(0, 1, step=0.1, value=0.80, label="Threshold (Upper)", info="HHow bright must a pixel be to be considered as a 'border' for sorting?", visible=False)
                interval_image = gr.Image(type="pil",width=200,visible=False)
                interval_function.change(fn=interval_functionddChange,inputs=[interval_function], outputs=[clength,thresholdLower,thresholdUpper,interval_image])
            with gr.Group():
                mask_image = gr.Image(type="pil", value=None, image_mode='L', label="Sorting mask")                
            with gr.Group():
                ammountOfFrames = gr.Slider(5, 100, step=1, value=20, label="Amount of frames", info="Amount of GIF frames", interactive=True)
                frameDuration = gr.Slider(20, 500, step=10, value=100, label="Frame duration", info="Frame duration i ms", interactive=True)

        with gr.Column(scale=10):
            with gr.Row():
                input_img = gr.Image(type="pil",width=500)
                output_img = gr.Image(type="pil",width=500)
            btn = gr.Button("Сделай красиво")
            btn2 = gr.Button("GIF")
           
            btn.click(fn=G.pixsort, inputs=[input_img,mask_image,sorting_function,interval_function,randomness,angle,clength,interval_image], outputs=output_img)
            btn2.click(fn=G.animateIt, inputs=[input_img,mask_image,sorting_function,interval_function,angle,clength,interval_image,ammountOfFrames, frameDuration,randomness], outputs=output_img)
            
            
demo.launch(inbrowser=True, server_port=7860)