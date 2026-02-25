import asyncio
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler
from commands import start, status_all, status_extreme
from alert_logic import get_extreme_funding

load_dotenv(dotenv_path="/root/bybit_alert_bot/.env")

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


async def alert_loop(app):
    while True:
        extreme = get_extreme_funding()
        if extreme:
            msg = "🚨 *Funding Estremi Rilevati*\n\n"
            for f in extreme:
                msg += (
                    f"{f['symbol']}:\n"
                    f"  Rate: `{f['fundingRate']}`\n"
                    f"  Interval: `{f['fundingInterval']}`\n\n"
                )

            await app.bot.send_message(
                chat_id=CHAT_ID,
                text=msg,
                parse_mode="Markdown"
            )

        await asyncio.sleep(60)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status_all", status_all))
    app.add_handler(CommandHandler("status_extreme", status_extreme))

    app.job_queue.run_repeating(lambda *_: asyncio.create_task(alert_loop(app)), interval=60, first=5)

    app.run_polling()


if __name__ == "__main__":
    main()
