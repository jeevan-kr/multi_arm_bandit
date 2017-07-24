"""
    The Epsilon-Greedy algorithm implementation of the Multi-Armed Bandit.
"""
import random
class EpsilonGreedy:
    def __init__(self, arms, epsilon):
        self.epsilon = epsilon
        self.initialize(arms)

    def initialize(self, arms):
        self.arms = arms
        self.trials = [0] * self.arms
        self.perf = [0] * self.arms

    def choose_arm(self):
        ret_index = None
        if random.random() > self.epsilon:
            # TODO: if list.index does a sequetial look-up then this is not truly uniform if there are identical max values
            ret_index = self.perf.index(max(self.perf))
        else:
            ret_index = random.randrange(self.arms)
        return ret_index

    def update_performance(self, arm_idx, reward):
        t = self.trials[arm_idx] + 1
        cur_perf = self.perf[arm_idx]

        new_pref = cur_perf * (t-1 / float(t)) + reward * (1 / float(t))
        self.trials[arm_idx] = t
        self.perf[arm_idx] = new_pref

    def print_performance(self):
        print("Arms:", range(0,self.arms))
        print("Trials:", ep_greed.trials)
        print("Performance:", ep_greed.perf)


if __name__ == "__main__":
    ep_greed = EpsilonGreedy(2, 0.5)
    ep_greed.print_performance()