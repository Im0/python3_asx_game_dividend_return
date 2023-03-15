import csv
import yfinance as yf
import pprint

# Disclaimer:
# This script and output is provided for educational purposes only and does not constitute financial
# advice.  Please consult a licensed financial advisor before making any investment decisions outside
# of the ASX game.

# Read in the CSV file
with open('dividend_stocks.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # skip the first line
    rows = list(csv_reader)

# Look up the current share price for each company on the ASX
for row in rows:
    ticker = row[2] + '.AX'
    print(f"Looking up ${ticker}")
    stock = yf.Ticker(ticker)
    # pprint was for debugging
    #pprint.pprint(stock.__dict__)
    current_price = stock.fast_info['lastPrice']
    print(f"lastPrices for {ticker} = {current_price} ")
    row.append("%.2f" % current_price)

for row in rows:
    cost_per_thousand = float(row[5]) * 1000 # Remove the first character ($) of the row and store as a float
    print(f"{row[2]} (row 4 {row[4]} (row 5 {row[5]}) cost per share {cost_per_thousand}")
    row.append("%.2f" % cost_per_thousand)

# Calculate the potential return based on 1000 shares
for row in rows:
    dividend_payout = float(row[4][1:]) # Remove the first character ($) of the row and store as a float
    dividend_return = dividend_payout * 1000
    print(f" {row[2]} payout row 4 {row[4][1:]} dividend return {dividend_return} ")
    # return_percent = (buy_price - 100) / 100 * 1000
    row.append("%.2f" % dividend_return)

for row in rows:
    investment_return = float(row[4][1:]) / float(row[5]) * 100
    row.append("%.2f %%" % (investment_return))

# Write out the updated CSV file
with open('data_with_return.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Ex-date', 'Type', 'Code', 'Company', 'Terms ($)', 'Last buy price ($)', 'Cost to buy 1000 shares ($)', 'Dividend payout ($)', 'Payout %'])
    for row in rows:
        writer.writerow(row)
