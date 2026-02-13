import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("zNl7kkS4Nc8wi25jZkgwhX8YK4ZRLjVq3aA0u2AQOFI6hd2oHFV8J3J2dzl3aRd")
api_secret = os.getenv("vkYwcjL4x1PWShviFG84BeC7d52MssVRJmJItre577iIBRNkgHWOQ3rFibF2j7E")


client = Client(api_key, api_secret)
client.API_URL = "https://testnet.binance.vision/api"

def get_price(symbol="BTCUSDT"):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker["price"])
