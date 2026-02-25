from alert_logic import get_all_funding, get_extreme_funding


async def start(update, context):
    await update.message.reply_text(
        "Bot attivo!\n"
        "/status_all - Tutti i funding (con intervallo)\n"
        "/status_extreme - Funding estremi\n"
    )


async def status_all(update, context):
    data = get_all_funding()
    if not data:
        await update.message.reply_text("Nessun dato disponibile.")
        return

    msg = ""
    for f in data:
        line = (
            f"{f['symbol']}:\n"
            f"  Rate: `{f['fundingRate']}`\n"
            f"  Interval: `{f['fundingInterval']}`\n\n"
        )

        # Se il messaggio diventa troppo lungo, invia e ricomincia
        if len(msg) + len(line) > 3500:
            await update.message.reply_text(msg, parse_mode="Markdown")
            msg = ""

        msg += line

    # Invia l’ultimo blocco
    if msg:
        await update.message.reply_text(msg, parse_mode="Markdown")


async def status_extreme(update, context):
    extreme = get_extreme_funding()
    if not extreme:
        await update.message.reply_text("Nessun funding estremo trovato.")
        return

    msg = "🚨 *Funding Estremi*\n\n"
    for f in extreme:
        msg += (
            f"{f['symbol']}:\n"
            f"  Rate: `{f['fundingRate']}`\n"
            f"  Interval: `{f['fundingInterval']}`\n\n"
        )

    await update.message.reply_text(msg, parse_mode="Markdown")
