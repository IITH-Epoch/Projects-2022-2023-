# Environments
Currently, there is only one environment `stock_trading_env.py` which is for single stock trading. Utility functions for computing technical indicators are present in a separate module `technical_indicators.py`

## Unit tests
To test the working of the environment by itself, download a Yahoo finance dataset for share prices of one particular stock ([for example](https://www.kaggle.com/datasets/achintyatripathi/yahoo-finance-apple-inc-aapl)). Import the environment as a class and run the following code:
```py
from stock_trading_env import StockTradingEnv

env = StockTradingEnv(3_000_000, 'csv', 'AAPL_daily_update.csv')

print(env.observation_space)
print(env.action_space)

env.reset()
total_reward = 0
done = False

while not done:
    action = env.action_space.sample()
    observations, reward, terminated, truncated, info = env.step(action)
    total_reward += reward

print(total_reward)
```
