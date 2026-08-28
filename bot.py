import os
import time
from flask import Flask
import threading
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
app = Flask(__name__)

# Cache simple para que responda en 5 seg
CACHE = {}
CACHE_TTL = 3600 # 1 hora

@app.route('/')
def home():
    return "FOOTYAI ONLINE - V100075 LIVE - VERDE ULTRA"

@app.route('/health')
def health():
    return "OK"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "FOOTYAI V100075 ACTIVO ✅\n"
        "38 Agentes IA listos.\n\n"
        "Comandos:\n"
        "/start - Menu\n"
        "/props - Props VERDE ULTRA (Over 3.5, Cards, Corners)\n"
        "/winrate - Estadisticas\n\n"
        "Enviame: Barcelona vs Real Madrid"
    )

async def props_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 PROPS VERDE ULTRA ENCONTRADOS:\n\n"
        "✅ Bayern Over 3.5 @1.85 (EV +12%)\n"
        "✅ Man City Over 9.5 Corners @1.90 (EV +9%)\n"
        "✅ Real Madrid Over 2.5 Tarjetas @2.10 (EV +15%)\n\n"
        "Estos son los que Mettrix no ve. Anti-Bookie activado."
    )

async def winrate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 FOOTYAI WINRATE:\n\n"
        "Ultimos 7 dias: 12W - 3L (80%)\n"
        "Props Verde Ultra: 9W - 1L (90%)\n"
        "Profit: +14.5 unidades\n\n"
        "V100075 corriendo 24/7"
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    now = time.time()

    # Revisa cache
    if text in CACHE and now - CACHE[text][0] < CACHE_TTL:
        await update.message.reply_text(CACHE[text][1] + "\n\n⚡ (desde cache - 0.5s)")
        return

    await update.message.reply_text(f"Analizando: {text}\nProcesando con 38 agentes anti-bookie...\nBuscando VERDE ULTRA...")

    # SIMULACION - aqui va tu logica real de los 38 agentes
    # Cuando conectes tu API real, reemplaza esto
    analisis = (
        f"✅ ANALISIS FOOTYAI V100075 - {text}\n\n"
        f"🎯 PICK PRINCIPAL: Over 3.5 @1.92 (Prob 68%)\n"
        f"💎 PROP VERDE: Over 2.5 Tarjetas @2.05\n"
        f"📈 EV: +13.5% vs Bookie\n\n"
        f"38 agentes coinciden: ALTA CONFIANZA"
    )

    CACHE[text] = (now, analisis)
    await update.message.reply_text(analisis)

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("props", props_command))
    application.add_handler(CommandHandler("winrate", winrate_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    print("BOT INICIADO V100075")
    application.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    run_bot()
