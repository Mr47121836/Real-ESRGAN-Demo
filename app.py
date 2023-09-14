import gradio as gr
from inference_realesrgan import main as main_img


def generate_text(par,par2):
    pass

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Hello World!
    Start typing below to see the output.
    """)
    with gr.Row():
        with gr.Column():
            seed = gr.Text(label="Input Phrase")
            img = gr.Image(type="pil",label = "需要修复的图片")
        with gr.Column():

            english = gr.Text(label="Generated English Text")
            german = gr.Text(label="Generated German Text")
            img_out = gr.Image(type="pil",label = "修复完成的图片")

    btn = gr.Button("Generate")
    btn.click(main_img, inputs=[seed], outputs=[english, german])
    gr.Examples(["My name is Clara and I am"], inputs=[seed])


if __name__ == "__main__":
    demo.launch()