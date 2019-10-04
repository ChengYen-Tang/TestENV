import gym
import numpy as np

class TestEnv(gym.Env):
    metadata = {'render.modes': ['human', 'system', 'none']}

    def __init__(self):
        self.action_space = gym.spaces.MultiDiscrete([2])

        self.observation_shape = (1, 100)
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=self.observation_shape, dtype=np.float16)

    def reset(self):
        self.counter = 0
        self.action_state = 2
        self.valid_actions = [[1, 1]]
        print('reset')
        
        return self.state()

    def step(self, action):
        current_actions = None

        if action[0] == 0:
            if self.action_state == 0:
                print('Invalid actions')
                current_actions = [2]


            self.action_state = 0
            self.valid_actions = [[0,1]]

        if action[0] == 1:
            if self.action_state == 1:
                print('Invalid actions')
                current_actions = [2]

            self.action_state = 1
            self.valid_actions = [[1,0]]

        self.counter += 1
        return self.state(), 0, self.finish(), {'action_mask' : self.valid_actions}


    def render(self, mode='human'):
        pass

    def finish(self):
        return self.counter == 10000

    def state(self):
        temp = np.array([*range(100)])
        # print(temp/100)
        obs = temp/100
        return [obs]