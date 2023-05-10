import gym
from gym import spaces

import numpy as np
import pandas as pd
import technical_indicators as ti

class StockTradingEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, capital, file_type, file_path, render_mode=None):
        """ Gym environment for single stock trading.

        The observation space consists of a discrete value representing the number of
        shares that are currently held (maximum 1,000,000,000) and twelve continuous values as follows:
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

        The action space is the set of real numbers in [-1, 1]. Any action in this space is scaled
        by a fixed constant (100,000 here) which gives us the number of shares to bought 
        (if positive) or sold (if negative).

        The reward at any timestep is simply the difference between the portfolio values at the
        current timestep and the previous timestep. Portfolio value is the net worth of the agent
        at any timestep which is given by the sum of its current balance and the value of all the
        shares currently held.

        Args:
            capital (float): The initial capital that the agent starts with
            file_type (str): Either 'csv' or 'excel' denoting the type of the share price dataset file
            file_path (str): Path to the share price dataset file
            render_mode (Optional[str]): Either None or 'human' 
        """
        
        super(StockTradingEnv, self).__init__()

        # Dataset of share prices
        if file_type == 'csv':
            self.data = pd.read_csv(file_path)
        elif file_type == 'excel':
            self.data = pd.read_excel(file_path)
        else:
            raise TypeError('File type not supported')

        # Maximum number of shares that can be bought or sold at a time
        self.max_shares = 100_000

        # Definition of observation space      
        discrete_space = spaces.Discrete(1_000_000_000)
        continuous_space = spaces.Box(low=-np.inf, high=np.inf, shape=(12,), dtype=np.float32)
        self.observation_space = spaces.Tuple((discrete_space, continuous_space))

        # Definition of action space
        self.action_space = spaces.Box(low=-1, high=1, dtype=np.float32)

        # Check if the current render_mode is supported
        assert render_mode is None or render_mode in self.metadata['render_modes']
        self.render_mode = render_mode

        # Remember inital capital
        self.initial_capital = capital

        # Initialize balance left
        self.balance = capital

        # Current closing price of the share
        self.current_price = 0.0

        # Number of shares owned
        self.num_shares = 0

        # Portfolio value of the agent (balance + share worth)
        self.portfolio_value = capital

        # Current time instant
        self.timestamp = 0

    def asset_price(self):
        """ Return the current closing price of the share. """

        return self.data.iloc[self.timestamp-1]['Adj Close']

    def _get_obs(self, window_size=10):
        """ Retrieve the observation state at any step. """

        obs_state = {
            "Number of shares owned": self.num_shares,
            "Balance left" : self.balance,
            "Current closing price" : self.asset_price(),
            "RSI" : ti.rsi(self.data, self.timestamp, window_size),
            "SMA" : ti.sma(self.data, self.timestamp, window_size),
            "EMA" : ti.ema(self.data, self.timestamp, window_size),
            "Stochastic oscillator" : ti.stochastic_oscillator(self.data, self.timestamp, window_size),
            "MACD": ti.macd(self.data, self.timestamp),
            "AD": ti.ad(self.data, self.timestamp),
            "OBV": ti.obv(self.data, self.timestamp),
            "ROC": ti.proc(self.data, self.timestamp, window_size),
            "Williams %R" : ti.williams_r(self.data, self.timestamp, window_size),
            "Disparity index" : ti.disparity_index(self.data, self.timestamp, window_size)
        }
        return obs_state

    def _get_info(self):
        """ Retrieve auxiliary information about the current state. """

        return {"Portfolio value": self.portfolio_value}

    def _get_reward(self):
        """ Compute the reward at each timestep. """

        new_portfolio_value = self.balance + self.num_shares * self.current_price
        reward = new_portfolio_value - self.portfolio_value
        self.portfolio_value = new_portfolio_value
        return reward

    def _take_action(self, action):
        """ Take an action in the current state. """
        
        # Hold
        if action == 0:
            return

        # Buy
        elif action > 0:
            buy_shares = int(action * self.max_shares) 
            if self.current_price * buy_shares > self.balance:
                buy_shares = self.balance // self.current_price

            self.num_shares += buy_shares
            self.balance -= self.current_price * buy_shares

        # Sell
        else:
            sell_shares = int(-1 * action * self.max_shares)
            if sell_shares > self.num_shares:
                sell_shares = self.num_shares

            self.num_shares -= sell_shares
            self.balance += self.current_price * sell_shares

    def step(self, action):
        """ Execute one time step in the environment and return the updated state, reward, termination and auxiliar information. """
        
        # Check if the action is valid
        if not self.action_space.contains(action):
            raise ValueError('Invalid action')
        
        self.timestamp += 1
        self.current_price = self.asset_price()
        self._take_action(action)

        observation = self._get_obs()
        reward = self._get_reward()
        terminated = True if self.timestamp >= len(self.data) else False
        truncated = False
        info = self._get_info()

        return observation, reward, terminated, truncated, info


    def reset(self):
        """ Reset the environment to its initial state. """

        self.balance = self.initial_capital
        self.current_price = 0.0
        self.num_shares = 0
        self.portfolio_value = self.balance
        self.timestamp = 0

    def render(self):
        """ Visualize the environment. """
        pass

    def close(self):
        """ Close the environment. """
        pass

    def train(self):
        """ Train the agent to maximize reward. """
        pass
