"""
LeukemiaAI demo application.
"""
import gradio as gr
from transformers import pipeline


model = pipeline("image-classification", model="SuperMaker/vit-base-patch16-224-in21k-leukemia")


def predict(img):
    """a simple wrapper around the model pipeline"""
    predictions = model(img)
    formatted = {}
    for label in predictions:
        formatted[label['label']] = label['score']
    return formatted


with gr.Blocks() as demo:
    
    with gr.Row():
        gr.Markdown('')

    with gr.Row():
        with gr.Column():
            gr.Markdown('')

        with gr.Column():          
            image = gr.Image(label="Upload microscopic cells Image", type="pil")
            btn = gr.Button('Predict')

        with gr.Column():
            gr.Image('demo/LuekemiaAI.png', label="LeukemiaAI")
            label = gr.Label(label="Predicted Label")

        with gr.Column():
            gr.Markdown('')

    btn.click(predict, inputs=[image], outputs=[label])

gr.close_all()
demo.launch()
    



