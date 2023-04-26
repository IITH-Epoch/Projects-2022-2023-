# Agent Playing In Frozen Lake Environment

This Project was developed by [M Charan](https://github.com/Charanyash), Core Member of [Epoch](https://github.com/IITH-Epoch) (2022-2023). 

The aim of the project is to develop an agent using RL algorithms to learn policies in the [Frozen Lake environment](https://www.gymlibrary.dev/environments/toy_text/frozen_lake/) from [OpenAI gym](https://www.gymlibrary.dev/).  

## Frozen Lake
Frozen Lake is a toy text environment from OpenAI gym where the agent starts at S and the aim is to reach the goal G in minimum number of steps.

### States
  - Starting State (S) 
  - Slippery State (F) 
  - Hole State (H)
  - Goal State (G)

### Actions
  - Left  
  - Right 
  - Up 
  - Down 

### Reward System
  - Agent recieves a reward of -0.01 on stepping on a Slippery State (F).
  - Agent recieves a reward of -0.2 on stepping on a Hole State (H).
  - Agent recieves a reward of 1.0 on reaching the Goal (G).

### Traversing In Environment
 In general *is_slippery* is set to True to make the actions stochastic. In that case the agent is equally likely to move in intended direction and as well as perpendicular direction on both sides.  
  By setting  *is_slippery* to False will make the agent to move in intended direction all the time.

### Algorithms Used in game-play

  1. When the actions are not stochastic, 
         - I used Q learning and SARSA Algorithms to train the agent.
	 - Then used a custom map to understand the difference in Q learning and SARSA.
  2. When actions are stochastic,
         - I used Q learning and Value Iteration to train the agent.

### Directory
  - **Figs** - Contains plots for agents performance.
  - **FrozenLake.ipynb** - Python notebook for implementing Q learning and SARSA Algorithms when *is_slippery* is set to False and comparing their performance.
  - **Frozenlake_slippy.ipynb** - Python notebook for implementing Q learning and Value Iteration when *is_slippery* is set to True and comparing their performance.
  - **report.pdf** - All the observations and results in the project are discussed.
  - **report.tex** - Tex file to generate **report.pdf**.

### Setup
  - Jupyter Notebook to access .ipynb files.
  - XeLatex software to run the .tex file. 
 
