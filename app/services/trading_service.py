from binance.client import Client
import pandas as pd
from config import API_KEY, API_SECRET

# Connexion à Binance Testnet
client = Client(API_KEY, API_SECRET, testnet=True)

def get_data(symbol="BTCUSDT", interval="1h", limit=200):
    """Récupère les bougies du marché."""
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=[
        'time','open','high','low','close','volume',
        'close_time','qav','num_trades','taker_base_vol','taker_quote_vol','ignore'])
    df['close'] = df['close'].astype(float)
    return df[['close']]

#Connexion API Testnet, récupération des prix, transformation DataFrame.