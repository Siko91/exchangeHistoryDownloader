import datetime
import calendar

# pip install python-binance

import binance
from binance.client import Client

_now =  datetime.datetime.utcnow()
_2yearAgo = calendar.timegm(_now.replace(year=_now.year-2).timetuple())
_now = calendar.timegm(_now.timetuple())

def getClient(apiKey, secret):
    client = Client(apiKey, secret)
    return client


def getOpenPositions(client):
    openPositions = client.get_open_orders(timestamp=_2yearAgo)
    return openPositions

def getBalances(client):
    balances = client.get_account(timestamp=_now)["balances"]
    return balances

def getWithdraws(client):
    withdraws = client.get_withdraw_history(timestamp=_2yearAgo)
    return withdraws["withdrawList"]

def getDeposits(client):
    deposits = client.get_deposit_history(timestamp=_2yearAgo)
    return deposits["depositList"]

def getAllPairs(client):
    ticker = client.get_ticker()
    symbols = map(lambda t: t["symbol"], ticker)
    return symbols

def getTrades(client, pairSymbol, fromId = 0):
    limit = 15
    trades = client.get_my_trades(
        symbol=pairSymbol, 
        timestamp=_2yearAgo, 
        limit=limit, 
        fromId = fromId)

    length = len(trades)
    if (length > 0):
        print "========>\t\t\t\t\t" + str(pairSymbol) + " : " + str(length)

    if(length == limit):
        trades = trades + getTrades(client, pairSymbol, trades[limit-1]["id"]+1)

    return trades