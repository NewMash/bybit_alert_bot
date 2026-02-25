async def alert_loop(app):
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
