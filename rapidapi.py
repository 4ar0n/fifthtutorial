import json
import requests
from pprint import pprint


###   Input your yahoo finance api key here  ####
rapidapi_key = 'YOUR_YAHOO_FINANCE_API_KEY'



def get_history_rapid(symbol):
    url = "https://yahoo-finance-low-latency.p.rapidapi.com/v8/finance/spark"

    querystring = { "symbols":r"{}".format(symbol),
                    "range": "5d",
                    # "range": "1d",
                    "interval": "15m"
                    }

    headers = {
        'x-rapidapi-key': rapidapi_key,
        'x-rapidapi-host': "yahoo-finance-low-latency.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text

def get_quote_rapid(symbol):
    url = "https://yahoo-finance-low-latency.p.rapidapi.com/v6/finance/quote"

    querystring = {"symbols":r"{}".format(symbol)}

    headers = {
        'x-rapidapi-key': rapidapi_key,
        'x-rapidapi-host': "yahoo-finance-low-latency.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text


data = get_history_rapid("BTC-USD")
pprint(data)

live_quote = json.loads(get_quote_rapid("BTC-USD"))
pprint (live_quote)
print (live_quote["quoteResponse"]["result"][0]["regularMarketPrice"])





