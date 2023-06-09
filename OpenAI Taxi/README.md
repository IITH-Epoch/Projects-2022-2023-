# OpenAI Gym's Taxi-v3 Task
## Solving the Taxi Problem from OpenAI Gym using Q-Learning
This project was developed by [Donal Loitam](https://github.com/Donal-08), Club member of [Epoch](https://github.com/IITH-Epoch) (2022-2023). <br/>
#### Objective : -
The goal is to use OpenAI Gym's Taxi-v3 environment and implement an algorithm to teach a taxi agent to navigate a small (5x5)gridworld. <br/>

#### Taxi-v3 Environment Description : -
The environment map looks something like the figure below <br/>

<img src="https://user-images.githubusercontent.com/102598808/210063899-901c850b-7e11-444f-98db-d4199a0bd875.png" width="40%" height="40%">

**States**: There are 500 possible states, corresponding to 25 possible grid locations, 5 locations for the passenger, and 4 destinations. <br/>
**Actions**: There are 6 possible actions, corresponding to moving North, East, South, or West, picking up the passenger, and dropping off the passenger. <br/>

The algorithm used for training the reinforcement learning agent:
- Q-learning

### Results : These are our trained model's performance evaluation after 100 episodes(pickup drop-off) 

| Metric        | Q-learning    |
| ------------- | ------------- |
| Average reward  | 8.04  |
| Average Penalties  | 0.00  |
| Average timesteps | 12.96 |

### Possible Improvements :-
- Use DeepQ Learning and compare its performance with Qlearning
- Tune the hyperparameters 
