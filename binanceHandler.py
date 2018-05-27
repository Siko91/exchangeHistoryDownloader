import datetime
import calendar

# pip install python-binance

import binance
from binance.client import Client

_now =  datetime.datetime.utcnow()
_1yearAgo = calendar.timegm(_now.replace(year=_now.year-2).timetuple())
_now = calendar.timegm(_now.timetuple())

def getClient(apiKey, secret):
    client = Client(apiKey, secret)
    return client


def getOpenPositions(client):
    openPositions = client.get_open_orders(timestamp=_1yearAgo)
    return openPositions

def getBalances(client):
    balances = client.get_account(timestamp=_now)["balances"]
    return balances

def getWithdraws(client):
    withdraws = client.get_withdraw_history(timestamp=_1yearAgo)
    return withdraws["withdrawList"]

def getDeposits(client):
    deposits = client.get_deposit_history(timestamp=_1yearAgo)
    return deposits["depositList"]

def getAllPairs(client):
    ticker = client.get_ticker()
    symbols = map(lambda t: t["symbol"], ticker)
    return symbols

def getTrades(client, pairSymbol):
    trades = client.get_my_trades(symbol=pairSymbol, timestamp=_1yearAgo)
    return trades