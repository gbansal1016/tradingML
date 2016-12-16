# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:48:09 2016

@author: gbans6
"""

##%
import pandas as pd
import numpy as py
import math

def cum_daily_ret(df_price):
    df_returns = df_price.copy()
    df_returns.rename(columns={"Adj Close":"cum_returns"}, inplace=True)
    df_returns[1:]=(df_returns[1:]/df_returns[:-1].values)-1
    df_returns.ix[0,:]=0
    return df_returns
    


def risk(df_returns):
    #print(df_returns.std())
    #sample standard deviation
    return df_returns[1:].std(axis=0)
        
def sharpe_ratio(df_price, daily_price=True):
    rfree=0
    df_ret = cum_daily_ret(df_price)
    p_std = py.std(df_ret)
    sharpe = math.sqrt(252)*(py.average(df_ret)-rfree)/p_std
    
    return sharpe.ix[0]

    
    
def test_run():
    dates = pd.date_range('2016-12-07', '2016-12-12')
    df = pd.DataFrame(index=dates)
    # Choose stock symbols to read
    symbol = 'AAPL'
    
    # Get stock data
    df=pd.read_csv("data\\"+symbol+".csv",index_col="Date",parse_dates=True,usecols=["Date", "Adj Close"],na_values=['nan'])
    
    df = df.sort_index()
    #df_ret= cum_daily_ret(df)
    #df_risk=risk(df_ret)
    
    print(sharpe_ratio(df))

    
##%