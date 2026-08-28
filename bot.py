import os
import time
import requests
from flask import Flask
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

app = Flask(__name__)
@app.route('/')
def home():
    return "FOOTYAI ONLINE"

def run_web():
    app.run(host='0.0.0.0', port=10000)

threading.Thread(target=run_web, daemon=True).start()

def enviar(texto):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": texto, "parse_mode": "HTML"})
    except:
        pass

enviar("✅ FOOTYAI V100074 ONLINE\nBot conectado correctamente a Render")

while True:
    time.sleep(3600)
    enviar("💓 FOOTYAI sigue activo")
