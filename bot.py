import os, time, requests
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID","6778322625")
def send(text):
    url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url,json={"chat_id":CHAT_ID,"text":text,"parse_mode":"Markdown"})
send("✅ FOOTYAI V100074 ONLINE\n38 Agentes activados\nID 8802103582\nListo para picks diarios")
while True:
    time.sleep(3600)
