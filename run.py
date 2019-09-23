from stable_baselines.common.policies import MlpLnLstmPolicy
from stable_baselines.common.vec_env import  SubprocVecEnv
from stable_baselines import PPO2

from env import TestEnv


if __name__ == '__main__':
    Test_env = SubprocVecEnv([lambda: TestEnv() for i in range(4)])

    model = PPO2(MlpLnLstmPolicy, Test_env, verbose=0, nminibatches=4)
    model.learn(total_timesteps = 10000)