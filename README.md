# python3_asx_game_dividend_return

## What

This python program reads a CSV file taken from the ASX game website which lists the ASX listed companies that have dividends released during the game period: March 16 till May 25.

It outputs:
* Last buy price of the stock
* Cost to buy 1000 shares of the stock
* The expected dividend payout based on 1000 shares
* The dividend return if % based on the payout amount divided by the last buy price

The program:

1. Loads in the CSV file into memory
2. Looks up the current stock ticker price via Yahoo Finance API's
3. Based on 1000 shares purchased, calculate potential dividend payout.
4. Create a CSV file with the results (data_with_return.csv)

## Why

There is an opportunity to make a return based on company dividends.  Caution and consideration must be taken as typically ticker prices rise pre-dividend date and drop after dividend date sometimes negating the benefit of taking a dividend.

The script and output is provided to act as a talking point.

## Consider

* This script does not account for dividends being franked or not.  We are assuming that stocks are fully franked as part of the game.
* This is a basic script and there is VAST potential for creating much more complex and intricate scripts to harness the vast amounts of stock data available.
* For the companies listed in the outputted csv file:
** Historically what happens to their share prices after dividend?  Do they go down/up?  If they go down,  is the dividend payout typically the same amount?
** Is it better to receive the dividend, or, to buy the shares post dividend?

## How to run

You must have the following installed:

* Python 3 - https://www.python.org/downloads/
* The python 3 yahoo finance ( https://pypi.org/project/yfinance/ ) package installed via pip. `pip3 install yfinance`
* Once downloaded onto your computer, the script can then be ran via the command line with: `python predict.py`

### Files

* `predict.py` - The main python program to run
* `data_with_return.csv` - The file that is created by `predict.py`.  The provided file in this repository was generated 15/03/2023 and the values will change
* `dividend_stocks.csv` - This file was created from data on https://game.asx.com.au/game/play/school/2023-1/dividends
* `README.md` - This file

## Disclaimer

This script and output is provided for educational purposes only and does not constitute financial
advice.  Please consult a licensed financial advisor before making any investment decisions outside
of the ASX game.

By using this script, you acknowledge and accept that you are using it at your own risk, and the author
and any contributors to this script will not be held liable for any losses or damages that may arise 
from your use of this script.