# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 18:48:59 2016

@author: gbans6
"""

##%

import pandas as pd
import matplotlib.pyplot as plt
import os


def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir,"{}.csv".format(str(symbol)))
    
def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    
    if 'SPY' not in symbols:
        symbols.insert(0,'SPY')
    
    for symbol in symbols:
        print(symbol)
        df_sym=pd.read_csv(symbol_to_path(symbol),
                           index_col="Date",
                           parse_dates=True,
                           usecols=["Date", "Adj Close"],na_values=['nan'])
        
        df_sym=df_sym.rename(columns={"Adj Close":symbol})
        df=df.join(df_sym,how="inner")
        if symbol == "SPY":
            df =df.dropna(subset=["SPY"])        
    return df

def plot_data(df):
    grph = df.plot(title="Stock Prices", fontsize=10)
    grph.set_xlabel("Date")
    grph.set_ylabel("Price")
    plt.show()

def normalize_data(df):
    return df / df.ix[0,:]
      

def test_run():
    # Define a date range
    dates = pd.date_range('2016-12-07', '2016-12-12')

    # Choose stock symbols to read
    symbols = ['AAPL', 'IBM']
    
    # Get stock data
    df = get_data(symbols, dates)
    df = df.sort_index()
    #df = normalize_data(df)
#   print(df)
#    plot_data(normalize_data(df))
    df_aapl= df.ix[:,'AAPL']
    print(df_aapl)
##%