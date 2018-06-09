import numpy as np
from random import randint


class PolicyImprovement:

    def __init__(self, deterministic_state):
        self.deterministic_state = deterministic_state

    def max(self, i, j):
        if i > j:
            return i
        else:
            return j

    def print_policy(self, policy_matrix):
        for i in range(0, policy_matrix.shape[0]):
            print(policy_matrix[i])

    def print_cumulative_reward_matrix(self, cumulative_reward_matrix):
        for i in range(0, cumulative_reward_matrix.shape[0]):
            for j in range(0, cumulative_reward_matrix.shape[0]):
                print(cumulative_reward_matrix[i][j])

    def execute(self):
        convergence_threshold = 2
        reward_matrix = self.deterministic_state.get_reward_matrix()
        policy_matrix = self.deterministic_state.get_policy_matrix()
        cumulative_reward_matrix = self.deterministic_state.get_cumulative_reward_matrix()
        # randomly pick a policy
        for i in range(0, self.deterministic_state.get_n()):
            # randomly pick a action for each state
            # calculate out degree
            out_degree = np.where(reward_matrix[i, :] != 0)[0].shape[0]
            # if no out degree , no action
            if out_degree == 0:
                policy_matrix[i] = -1
                break
            # otherwise , randomly pick a action
            a = randint(0, out_degree - 1)
            for j in range(0, self.deterministic_state.get_n()):
                if a == 0:
                    policy_matrix[i] = j
                    break
                if reward_matrix[i, j] != 0:
                    a = a - 1
        self.print_policy(policy_matrix)
        # policy iteration
        max_diff = 99999
        discount = 0.6
        # if the absolute difference is bigger than  convergence threshold
        while max_diff > convergence_threshold:
            max_diff = 0
            # run bellmen equation in each state
            for i in range(0, self.deterministic_state.get_n()):
                original_v = reward_matrix[i, policy_matrix[i]]
                if policy_matrix[i] != -1:
                    if policy_matrix[policy_matrix[i]] == -1:
                        cumulative_reward_matrix[i, policy_matrix[i]] = reward_matrix[i, policy_matrix[i]]
                    else:
                        cumulative_reward_matrix[i, policy_matrix[i]] = reward_matrix[i, policy_matrix[i]] + \
                                                                        discount*cumulative_reward_matrix[
                                                                            policy_matrix[i], policy_matrix[
                                                                                policy_matrix[i]]]
                max_diff = self.max(max_diff, abs(original_v - cumulative_reward_matrix[i, policy_matrix[i]]))
        self.print_cumulative_reward_matrix(cumulative_reward_matrix)

