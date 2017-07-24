import random

class BernouliArm:
    def __init__(self, s):
        self.s = s

    def pull(self):
        reward = 0

        if random.random() < self.s:
            reward = 1

        return reward
