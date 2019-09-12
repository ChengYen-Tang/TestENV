from stable_baselines.common.policies import MlpLnLstmPolicy
from stable_baselines.common.vec_env import  DummyVecEnv
from stable_baselines import PPO2

from env import TestEnv

Test_env = DummyVecEnv([lambda: TestEnv()])

model = PPO2(MlpLnLstmPolicy, Test_env, verbose=0, nminibatches=1)
model.learn(total_timesteps = 10000)