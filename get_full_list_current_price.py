import csv
import yfinance as yf
import pprint
import time

# Disclaimer:
# This script and output is provided for educational purposes only and does not constitute financial
# advice.  Please consult a licensed financial advisor before making any investment decisions outside
# of the ASX game.
#
# This script is to check the current price of all tickers in the ASX game file: full-companies-2023-1-1679359455821.csv

# Read in the CSV file
with open('full-companies-2023-1-1679359455821.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # skip the first line
    rows = list(csv_reader)

# Look up the current share price for each company on the ASX
for row in rows:
    ticker = row[1] + '.AX'
    print(f"Looking up ${ticker}")
    stock = yf.Ticker(ticker)
    # pprint was for debugging
    #pprint.pprint(stock.__dict__)
    current_price = stock.fast_info['lastPrice']
    print(f"lastPrices for {ticker} = {current_price} ")
    row.append("%.2f" % current_price)
    # Delay 1 second between queries.  We don't want to smash the server.
    time.sleep(2)

# Write out the updated CSV file
with open('full_company_list_with_current_prices.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Company', 'Code', 'Last Price'])
    for row in rows:
        writer.writerow(row)
