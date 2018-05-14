import datetime
import calendar

# pip install python-binance

import binance
from binance.client import Client

def parseBinance(apiKey, secret):
    _now =  datetime.datetime.utcnow()
    _2yearsAgo = calendar.timegm(_now.replace(year=_now.year-2).timetuple())
    _now = calendar.timegm(_now.timetuple())

    client = Client(apiKey, secret)

    ticker = client.get_ticker()
    symbols = map(lambda t: t["symbol"], ticker)
    trades = map(lambda s: client.get_my_trades(symbol=s, time=_2yearsAgo), symbols)

    print str(len(trades)) + " pairs found"

    ##########

    return []