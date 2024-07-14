import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# Number of server requests
N = 500

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        return None
    return price_a / price_b

# Main
if __name__ == "__main__":
    for _ in range(N):
        try:
            response = urllib.request.urlopen(QUERY.format(random.random()))
            quotes = json.loads(response.read())

            prices = {}
            for quote in quotes:
                stock, bid_price, ask_price, price = getDataPoint(quote)
                prices[stock] = price
                print("Quoted %s at (bid: %s, ask: %s, price: %s)" % (stock, bid_price, ask_price, price))

            if 'ABC' in prices and 'DEF' in prices:
                ratio = getRatio(prices['ABC'], prices['DEF'])
                if ratio is not None:
                    print("Ratio %s" % ratio)
                else:
                    print("Ratio could not be calculated due to division by zero.")
            else:
                print("Prices for both 'ABC' and 'DEF' were not found.")
        except Exception as e:
            print("Error: ", e)
