import requests

BASE_URL = "https://api.bybit.com"


def get_symbols():
    url = f"{BASE_URL}/v5/market/instruments-info?category=linear"
    r = requests.get(url, timeout=10)

    try:
        data = r.json()
    except Exception:
        print("ERRORE BYBIT (symbols):", r.text)
        return []

    if data.get("retCode") != 0:
        print("Errore API symbols:", data)
        return []

    symbols = []
    for item in data["result"]["list"]:
        sym = item["symbol"]
        if sym.endswith("USDT"):
            symbols.append(sym)

    return symbols


def get_ticker(symbol):
    url = f"{BASE_URL}/v5/market/tickers?category=linear&symbol={symbol}"
    r = requests.get(url, timeout=10)

    try:
        data = r.json()
    except Exception:
        print("ERRORE BYBIT (ticker):", r.text)
        return None

    if data.get("retCode") != 0:
        print("Errore API ticker:", data)
        return None

    lst = data.get("result", {}).get("list", [])
    if not lst:
        return None

    return lst[0]
