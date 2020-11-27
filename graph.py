import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import plotly.graph_objects as go

import pandas as pd
from datetime import datetime


def write_graph(data_path):
    df = pd.read_csv(data_path)

    fig = go.Figure(data=[go.Candlestick(x=df['datetime'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'])])

data_path = "/Users/aaronlee/Documents/python/fifthtutorial/FX_XAUUSD_intraday_60.csv"

write_graph(data_path)