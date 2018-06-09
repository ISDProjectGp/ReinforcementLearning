import numpy as np


class GeoMatrixGenerator:
    def __init__(self):
        self.geo_matrix = np.matrix([[0, 0, 0, 0], [0, -10, 0, -10], [0, 0, 0, 20]])

    def create_matrix(self, np_matrix):
        self.geo_matrix = np_matrix

    def create_connectivity_matrix(self):
        n = self.geo_matrix.shape[0]
        m = self.geo_matrix.shape[1]
        min = 0
        max = n * m - 1
        connectivity_matrix = np.zeros(((n * m), (n * m)))
        for i in range(0, n):
            for j in range(0, m):
                encode = j + i * m
                if encode - 1 >= min and encode % m != 0:
                    connectivity_matrix[encode][encode - 1] = 1
                if encode + 1 <= max and (encode + 1) % m != 0:
                    connectivity_matrix[encode][encode + 1] = 1
                if encode + m <= max:
                    connectivity_matrix[encode][encode + m] = 1
                if encode - m >= min:
                    connectivity_matrix[encode][encode - (m + 1)] = 1
        return connectivity_matrix

    def create_reward_matrix(self):
        n = self.geo_matrix.shape[0]
        m = self.geo_matrix.shape[1]
        min = 0
        max = n * m - 1
        reward_matrix = np.zeros(((n * m), (n * m)))
        for i in range(0, n):
            for j in range(0, m):
                encode = j + i * m
                if encode - 1 >= min and encode % m != 0:
                    reward_matrix[encode][encode - 1] = self.geo_matrix[i, j - 1]
                if encode + 1 <= max and (encode + 1) % m != 0:
                    print(j + 1)
                    reward_matrix[encode][encode + 1] = self.geo_matrix[i, j + 1]
                if encode + m <= max:
                    reward_matrix[encode][encode + m] = self.geo_matrix[i + 1, j]
                if encode - m >= min:
                    reward_matrix[encode][encode - m] = self.geo_matrix[i - 1, j]
        return reward_matrix
