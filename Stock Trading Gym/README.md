# Stock Trading Gym

This repository contains an implementation of an OpenAI Gym environment for single stock trading. The project was developed by the following members of [Epoch](https://github.com/IITH-Epoch) (2022-23)
- [Ankit Saha](https://github.com/Ankit-Saha-2003)
- [Mannem Charan](https://github.com/Charanyash)
- [Donal Loitam](https://github.com/Donal-08)

This project is based on the paper [T. Kabbani and E. Duman (2022), "Deep Reinforcement Learning Approach for Trading Automation in The Stock Market"](https://arxiv.org/abs/2208.07165)

## Observation Space
The observation space consists of a discrete value representing the number of shares that are currently held (maximum $10^9$) and twelve continuous values as follows:
- Balance
- Closing price

along with the following ten technical indicators:
- Relative Strength Index (RSI)
- Simple Moving Average (SMA) 
- Exponential Moving Average (EMA)
- Stochastic oscillator
- Moving Average Convergence/Divergence (MACD)
- Accumulation/Distribution Oscillator (AD)
- On-Balance Volume (OBV)
- Price Rate of Change (ROC)
- Williams %R
- Disparity index

## Action Space
The action space is the set of real numbers in [-1, 1]. Any action in this space is scaled by a fixed constant ($10^5$ here) which gives us the number of shares to bought (if positive) or sold (if negative).

## Reward Function
The reward at any timestep is simply the difference between the portfolio values at the current timestep and the previous timestep. Portfolio value is the net worth of the agent at any timestep which is given by the sum of its current balance and the value of all the shares currently held.