from alert_logic import get_all_funding, get_extreme_funding


async def start(update, context):
    await update.message.reply_text(
        "Bot attivo!\n"
        "/status_all - Tutti i funding (con intervallo)\n"
        "/status_extreme - Funding estremi\n"
    )


async def status_all(update, context):
    funding = get_all_funding()
    if not funding:
        await update.message.reply_text("Errore nel recupero funding da Bybit.")
        return

    msg = "📊 *Funding Rates*\n\n"
    for f in funding:
        msg += (
            f"{f['symbol']}:\n"
            f"  Rate: `{f['fundingRate']}`\n"
            f"  Predicted: `{f['predictedFundingRate']}`\n"
            f"  Interval: `{f['fundingInterval']}`\n\n"
        )

    await update.message.reply_markdown(msg)


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

    await update.message.reply_markdown(msg)
