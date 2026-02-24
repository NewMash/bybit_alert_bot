from bybit_client import get_symbols, get_ticker


def get_all_funding():
    symbols = get_symbols()
    results = []

    for sym in symbols:
        t = get_ticker(sym)
        if not t:
            continue

        try:
            funding_rate = float(t.get("fundingRate", 0.0))
            predicted = float(t.get("predictedFundingRate", 0.0))
        except ValueError:
            continue

        results.append({
            "symbol": sym,
            "fundingRate": funding_rate,
            "predictedFundingRate": predicted,
            "fundingInterval": t.get("fundingRateInterval", "N/A")
        })

    return results


def get_extreme_funding(threshold=0.01):
    all_funding = get_all_funding()
    return [f for f in all_funding if abs(f["fundingRate"]) >= threshold]
