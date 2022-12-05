import gym
import pandas as pd


class CustomEnv(gym.Env):
    def __init__(self, model):
        print("init")
        print("??")
        self.model = model
        print(pd.read_csv("../gamedata/start.csv"))

    def step(self, action):
        print("step")

    def reset(self):
        print("reset")
#%%
