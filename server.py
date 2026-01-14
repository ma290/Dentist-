from fastapi import FastAPI
import threading, time, requests, os
import gradio as gr
from app import launch_gradio

PORT = int(os.environ.get("PORT", 8000))
APP_URL = os.environ.get("APP_URL")

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

def self_ping():
    if not APP_URL:
        return
    while True:
        try:
            requests.get(APP_URL, timeout=5)
        except:
            pass
        time.sleep(600)

threading.Thread(target=self_ping, daemon=True).start()

gradio_app = launch_gradio()
app = gr.mount_gradio_app(app, gradio_app, path="/app")
