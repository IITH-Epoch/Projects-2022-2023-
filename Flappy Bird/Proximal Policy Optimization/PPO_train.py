import time
import flappy_bird_gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

# Load the Flappy Bird environment
env = flappy_bird_gym.make('FlappyBird-v0')
env.reset()

# Description of environment
print(f'Action space: {env.action_space}')
print(f'Observation space: {env.observation_space}')

# Examples of actions and states
print(f'Action space sample: {env.action_space.sample()}')
print(f'Observation space sample: {env.observation_space.sample()}')
## obs[0] = horizontal distance between agent and next pipe
## obs[1] = vertical distance between agent and next hole

# Example of result of action on state
print(f'Result sample: {env.step(env.action_space.sample())}')
## res[0] = new observation (hdist, vdist)
## res[1] = reward
## res[2] = whether episode is completed or not
## res[3] = diagnostic information useful for debugging

train_steps = 1_000_000

# Train the PPO model using a multilayer perceptron (MLP) policy
model = PPO('MlpPolicy', env, verbose=1, tensorboard_log='Logs/')
model.learn(total_timesteps=train_steps)
model.save('Models/PPO_flappy_bird_' + str(train_steps)) # Save the trained model

# Evaluate the trained model
print(evaluate_policy(model, env, n_eval_episodes=10, render=True))

# Close the environment (Pygame window)
env.close()