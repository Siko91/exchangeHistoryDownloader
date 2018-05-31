import binanceHandler
import excel
import apiKeyParser

import time
import datetime
import calendar

print datetime.datetime.now()

key = apiKeyParser.parseKeys("apiKeys.xml")

client = binanceHandler.getClient(key["apikey"], key["secret"])

balances = binanceHandler.getBalances(client)
openPositions = binanceHandler.getOpenPositions(client)

withdraws = binanceHandler.getWithdraws(client)
deposits = binanceHandler.getDeposits(client)

pairs = binanceHandler.getAllPairs(client)

trades = []
i = 0
for pair in pairs:
    i = i + 1
    print str(datetime.datetime.now()) + ' : (' + str(i) + '/' + str(len(pairs)) + ') Getting trades for ' + pair + '.'
    tradesOnThisPair = binanceHandler.getTrades(client, pair)
    trades = trades + tradesOnThisPair
    time.sleep(0.1)

results = [
    { "name" : "Balances", "data" : balances },
    { "name" : "Open Orders", "data" : openPositions },
    { "name" : "Withdraws", "data" : withdraws },
    { "name" : "Deposits", "data" : deposits },
    { "name" : "Trades", "data" : trades }
]

excel.writeToExcelFile(results)
