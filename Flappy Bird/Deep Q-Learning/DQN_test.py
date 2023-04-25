import time
import numpy as np
import flappy_bird_gym
from stable_baselines3 import DQN
import matplotlib.pyplot as plt

# Load the Flappy Bird environment
env = flappy_bird_gym.make('FlappyBird-v0')
env.reset()

train_steps = 500_000
episodes = 1000

reward_per_episode = []
timesteps_per_episode = []

# Load the trained Deep Q-Network
model = DQN.load('Models/DQN_flappy_bird_' + str(train_steps), env)

for episode in range(episodes):
    # Reset the observation state after the end of each episode
    obs = env.reset()
    done = False
    score = 0
    timesteps = 0

    while not done:
        action, states = model.predict(obs) # Predict the best action given obs using the trained model
        obs, reward, done, info = env.step(action) # Perform the action and record new observations and the reward
        score += reward
        timesteps += 1
        env.render() # Render the game using Pygame
        time.sleep(1/30) # Regulate the speed (FPS) at which the game is played 

    reward_per_episode.append(score)
    timesteps_per_episode.append(timesteps)
env.close()

print(f'Maximum reward = {np.max(reward_per_episode)}')
print(f'Average reward = {np.mean(reward_per_episode)}')
print(f'Standard deviation of reward = {np.std(reward_per_episode)}')

plt.plot(range(1, episodes + 1), reward_per_episode)
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.title('Reward at each episode')
plt.savefig('Plots/DQN_rewards_' + str(train_steps) + '.png')
plt.show()