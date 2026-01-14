from fastapi import FastAPI
import threading
import time
import requests
import os
from app import launch_gradio
import gradio as gr

PORT = int(os.environ.get("PORT", 8000))
APP_URL = os.environ.get("APP_URL", "http://localhost:8000")

app = FastAPI()

@app.get("/")
def health():
    return {"status": "DentAssist AI running"}

# 🔁 Self-Ping thread
def self_ping():
    while True:
        try:
            requests.get(APP_URL)
        except:
            pass
        time.sleep(300)  # every 5 minutes

threading.Thread(target=self_ping, daemon=True).start()

# 🎛️ Mount Gradio
gradio_app = launch_gradio()
app = gr.mount_gradio_app(app, gradio_app, path="/app")
