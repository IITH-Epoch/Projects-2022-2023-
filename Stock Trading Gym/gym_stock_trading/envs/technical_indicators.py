import numpy as np
import pandas as pd

""" Note that in all of the below functions, the arguments used are as follows:

df (pandas.DataFrame): DataFrame of the dataset of share prices
t (int): 1-indexed timestamp at which the technical indicators have to be computed
W (int): Window size considered for certain technical indicators
"""

def rsi(df, t, W):
    """ Relative Strength Index """

    if t > W:
        prices = df['Adj Close'].iloc[t-W-1:t-1]
        delta = prices.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.mean()
        avg_loss = loss.mean()
        if avg_loss == 0:
            return 100.0
        else:
            rs = avg_gain / avg_loss
            rsi_value = 100.0 - (100.0)/(1 + rs)
            return rsi_value
    else:
        return 50.0
          
def sma(df, t, W):
    """ Simple Moving Average """

    if t > W:
        sma_value = df['Adj Close'].iloc[t-W:t].mean()
        return sma_value
    else:
        sma_value = df['Adj Close'].iloc[:t].mean()
        return sma_value

def ema(df, t, W):
    """ Exponential Moving Average """

    global ema_value
    ema_alpha = 2/(1 + W)
    if t == 1:
        ema_value = df.iloc[0]["Adj Close"]
        return ema_value
    elif t <= W:
        ema_value = sma(df, t, W)
        return ema_value
    else:
        current_close = df.iloc[t-1]["Adj Close"]
        ema_value = (ema_alpha * current_close) + ((1 - ema_alpha) * ema_value)
        return ema_value
    
def stochastic_oscillator(df, t, W):
    """Stochastic oscillator """

    if t <= W:
        return 50.0
    
    high = df.iloc[t-W-1:t-1]['High'].max()
    low = df.iloc[t-W-1:t-1]['Low'].min()
    close = df.iloc[t-1]['Adj Close']
    if high - low == 0.0 :
        return 0.0

    K = 100 * (close - low) / (high - low)
    return K


def macd(df, t):
    """ Moving Average Convergence/Divergence """

    ema_12 = df['Adj Close'].ewm(span=12, adjust=True).mean()
    ema_26 = df['Adj Close'].ewm(span=26, adjust=True).mean()
    macd = ema_12 - ema_26
    return macd[t-1]

def ad(df, t):
    """ Accumulation/Distribution Oscillator """

    global ad_value 
    multiplier = ((df['Adj Close'][t-1] - df['Low'][t-1]) - (df['High'][t-1] - df['Adj Close'][t-1])) / (df['High'][t-1] - df['Adj Close'][t-1])
    if t == 1:
        ad_value = multiplier * df['Volume'][0]
        return ad_value
    else:
        ad_value = ad_value + multiplier * df['Volume'][t-1]
        return ad_value

def obv(df, t):
    """ On-Balance Volume """

    global obv_value
    if t == 1:
        obv_value = 0
        return obv_value
    else:
        curr_volume = df['Volume'][t-1]
        money_flow_volume = np.sign(df['Adj Close'][t-1] - df['Adj Close'][t-2]) * curr_volume
        obv_value = obv_value + money_flow_volume
        return obv_value
    
def proc(df, t, W):
    """ Price Rate of Change """
    
    if t <= W:
        proc_value = 0
        return proc_value
    else:
        curr_close = df['Adj Close'][t-1]
        prev_wind_close = df['Adj Close'][t-W-1]
        proc_value = ((curr_close - prev_wind_close)/(prev_wind_close)) * 100
        return proc_value

def williams_r(df, t, W):
    """ Williams %R """

    if t <= W:
        williams_r_percent = -50.0
        return williams_r_percent
    else:
        high_W = df['High'][t-W:t].max()
        low_W =  df['Low'][t-W:t].min()
        williams_r_percent = ((high_W - df['Adj Close'][t-1])/(high_W - low_W)) * -100
        return williams_r_percent

def disparity_index(df, t, W):
    """ Disparity index """
    
    ema_value = df['Adj Close'].ewm(span=W, adjust=True).mean()
    disparity_index = (df['Adj Close'][t-1] - ema_value[t-1]) * 100/(ema_value[t-1])
    return disparity_index



      