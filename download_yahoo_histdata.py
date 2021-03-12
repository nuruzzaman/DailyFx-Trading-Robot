import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt


def plotting_data_by_date():
    # Get the data for the FX, start date, and end date
    data = yf.download(['USDJPY=X'],'2020-01-01','2020-12-31')
    print(data)

    # Plot the close prices
    data["Adj Close"].plot()
    plt.show()


def plotting_data_by_period():
    data = yf.download(
        tickers=['BTC-USD'],
        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period="5d",
        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval="1m")
    print(data)
    # Plot the close prices
    data.Close.plot()
    plt.show()

def historical_price_data():
    yahoo_financials = YahooFinancials('USDJPY=X')

    data = yahoo_financials.get_historical_price_data(start_date='2000-01-01',
                                                      end_date='2019-12-31',
                                                      time_interval='daily')

    tsla_df = pd.DataFrame(data['USDJPY=X']['prices'])
    tsla_df = tsla_df.drop('date', axis=1).set_index('formatted_date')
    print(tsla_df)

historical_price_data()
