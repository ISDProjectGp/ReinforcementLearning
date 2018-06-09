import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class DeterministicState:

    name = None

    def __init__(self, n,name):
        self.reward_matrix = np.zeros((n, n))
        self.cumulative_reward_matrix = np.zeros((n, n))
        self.policy_matrix = np.zeros(n,dtype=int)
        self.name = name

    def create_default_reward_matrix(self):
        self.reward_matrix = np.matrix([[0, 1, 0, 0, 0], [1, 0, 1, 1, 2], [1, 1, 1, 0, 2], [1, 1, 1, 0, 0], [1, 0, 0, 0, 1]])
        self.cumulative_reward_matrix = np.zeros((self.reward_matrix.shape[0], self.reward_matrix.shape[1]))

    def get_policy_matrix(self):
        return self.policy_matrix

    def get_cumulative_reward_matrix(self):
        return self.cumulative_reward_matrix

    def get_reward_matrix(self):
        return self.reward_matrix

    def print_reward_matrix(self):
        print(self.reward_matrix)

    def get_name(self):
        return "("+self.name+")"

    def print_matrix_dimension(self):
        print(self.get_name()+" Dimension: "+str(self.cumulative_reward_matrix.shape[0])+" * "+str(self.cumulative_reward_matrix.shape[1]))

    def get_n(self):
        return self.cumulative_reward_matrix.shape[0];

    def print_state_machine_diagram(self):
        if self.cumulative_reward_matrix.shape[0] == self.cumulative_reward_matrix.shape[1]:
            g = nx.from_numpy_matrix(self.get_reward_matrix())
            nx.draw_circular(g)
            plt.show()
        else:
            print(self.get_name()+" Print: reward matrix is not a square matrix")


