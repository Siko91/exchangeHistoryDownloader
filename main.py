import poloniexHandler
import excel
import apiKeyParser

import datetime
import calendar

print

keys = apiKeyParser.parseKeys("apiKeys.xml")

poloniexKeys = filter(lambda k: k["type"] == "poloniex",keys)

results = []
for key in poloniexKeys:
    result = poloniexHandler.parsePoloniex(key["apikey"], key["secret"])
    results.append([key, result])

excel.writeToExcelFile(results)
