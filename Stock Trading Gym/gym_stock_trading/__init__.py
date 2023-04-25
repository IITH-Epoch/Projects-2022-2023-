from gym.envs.registration import register

register(
    id='StockTrading-v0',
    entry_point='stock_trading_env.envs:StockTradingEnv'
)