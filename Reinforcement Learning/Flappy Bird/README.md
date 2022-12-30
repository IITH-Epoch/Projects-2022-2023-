# Flappy Bird using Reinforcement Learning

![Python versions](https://img.shields.io/pypi/pyversions/flappy-bird-gym)

This project was developed by [Ankit Saha](https://github.com/Ankit-Saha-2003), Core Member of [Epoch](https://github.com/IITH-Epoch) (2022-23)

The objective of the project was to build and train an agent that can play the famous mobile game [Flappy Bird](https://en.wikipedia.org/wiki/Flappy_Bird) using reinforcement learning. The [OpenAI Gym](https://www.gymlibrary.dev/) [environment](https://github.com/Talendar/flappy-bird-gym) used in this project was developed by [@Talendar](https://github.com/Talendar) which in turn uses the Pygame implementation of Flappy Bird [FlapPyBird](https://github.com/sourabhv/FlapPyBird) made by [@sourabhv](https://github.com/sourabhv).

The following two algorithms have been used for training the reinforcement learning agent:
- Deep Q-Learning (DQN)
- Proximal Policy Optimization (PPO)

### Results
| Metric                               | DQN     | PPO       |
|--------------------------------------|---------|-----------|
| Optimal number of training timesteps | 500,000 | 1,000,000 |
| Maximum reward                       | 580     | 16824     |
| Maximum number of pillars crossed    | 14      | 453       |
| Average reward                       | 142.954 | 2246.625  |
| Average number of pillars crossed    | 2       | 59        |

_NOTE_: $\text{Number of pillars} \approx \dfrac{\text{Reward}}{37} + 1$
