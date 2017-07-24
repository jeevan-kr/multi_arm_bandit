import unittest
from multi_arm_bandit.arms import BernouliArm
from multi_arm_bandit.epsilon_greedy import EpsilonGreedy
import random
import codecs

class TestEpsilonGreedy(unittest.TestCase):
    def setUp(self):
        pass

    def test_arithmetic(self):
        self.assertEquals(1, 1)

    def test_epsilon_greedy_simulation(self):
        # For repeatability
        random.seed(2)

        # Success rate for the arms
        means = [0.1, 0.1, 0.1, 0.1, 0.9]
        # Shuffle the arm means to test if the algorithm picks the right arm
        random.shuffle(means)

        # Arms are initialized as Bernouli Arm (to represent marketing success rate for ex: CTI)
        arms = []
        for mean in means:
            arms.append(BernouliArm(mean))

        for arm in arms:
            print(arm, arm.s, arm.pull())

        print("Best Arm is " + str(means.index(max(means))))
        opt_file = codecs.open("./output_files/opt_file.txt", "w", "utf-8")

        for epsilon in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
            # Initialize the the algo
            algo = EpsilonGreedy(len(arms), epsilon)

            # Run the tester for a given set of epsilon values
            results = self.epsilon_greedy_tester(algo, arms, 5000, 250)
            # Results are expected to have [trial_nums, ticks, chosen_arms, rewards, cumulative_rewards]
            trials = results[0]
            for i in range(len(trials)):
                write_string = str(epsilon) + "\t"
                # opt_file.write()
                write_string += "\t".join([str(results[j][i]) for j in range(len(results))]) + "\n"
                opt_file.write(write_string)
                # print(write_string, end="")
                # columns [ 'epsilon', 'sim index',  'tick index', 'chosen arm', 'reward', 'cum reward']

        opt_file.close()
    def epsilon_greedy_tester(self, algo, arms, simulation_count, tick_horizon):
        chosen_arms = [0.0] * (simulation_count * tick_horizon)
        rewards = [0.0] *  (simulation_count * tick_horizon)
        cumulative_rewards = [0.0] * (simulation_count * tick_horizon)
        simulation_number = [0.0] *(simulation_count * tick_horizon)
        ticks = [0.0] * (simulation_count * tick_horizon)

        for sim in range(simulation_count):
            sim += 1
            algo.initialize(len(arms))

            for t in range(tick_horizon):
                t += 1
                index = (sim - 1) * tick_horizon + t - 1
                simulation_number[index] = sim
                ticks[index] = t
                chosen_arm = algo.choose_arm()
                chosen_arms[index] = chosen_arm

                reward = arms[chosen_arms[index]].pull()
                rewards[index] = reward

                if t == 1:
                    cumulative_rewards[index] = reward
                else:
                    cumulative_rewards[index] = cumulative_rewards[index - 1] + reward
                algo.update_performance(chosen_arm, reward)
        return[simulation_number, ticks, chosen_arms, rewards, cumulative_rewards]


if __name__ == "__main__":
    unittest.main()