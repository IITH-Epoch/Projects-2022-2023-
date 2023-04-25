import gym
from gym import spaces

import numpy as np

class StockTradingEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, render_mode=None):
        super(StockTradingEnv, self).__init__()

        # Observation space consisting of all the input parameters in the range [1, 1e6]
        self.observation_space = spaces.Box(low=0, high=1e6, shape=(4,), dtype=np.float32)

        # Action space consisting of two integers: 
        # one for hold/buy/sell, and the other for the number of stocks on which the action has to be taken
        self.action_space = spaces.MultiDiscrete([3, 1_000_000])

        # Check if the current render_mode is supported
        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

    def _get_obs(self):
        # Retrieve the observation space at any step
        pass

    def _get_info(self):
        # Retrieve auxiliary information about the current state
        pass

    def step(self, action):
        # Execute one time step in the environment and return the updated state, reward, termination and auxiliar information
        pass

    def reset(self):
        # Reset the environment to its initial state
        pass

    def render(self):
        # Visualize the environment
        pass

    def close(self):
        # Close the environment
        pass
