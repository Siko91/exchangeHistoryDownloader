import fbkheaRb

import datetime
import calendar

def parsePoloniex(apiKey, secret):
    pnx = fbkheaRb.poloniex(apiKey, secret)

    _now =  datetime.datetime.utcnow()
    _2yearsAgo = calendar.timegm(_now.replace(year=_now.year-2).timetuple())
    _now = calendar.timegm(_now.timetuple())

    trades = pnx.api_query("returnTradeHistory", {"currencyPair":"all", "start":str(_2yearsAgo)})

    pairs = trades.keys()
    trades = map(lambda k: trades[k], pairs)
    result = []
    for p in range(len(pairs)):
        for t in range(len(trades[p])):
            _trade = trades[p][t]
            result.append({
                "category": _trade["category"],
                "fee": _trade["fee"],
                "tradeID": _trade["tradeID"],
                "orderNumber": _trade["orderNumber"],
                "amount": _trade["amount"],
                "rate": _trade["rate"],
                "date": _trade["date"],
                "total": _trade["total"],
                "type": _trade["type"],
                "globalTradeID": _trade["globalTradeID"],
                "pair": pairs[p]
            })
    return result