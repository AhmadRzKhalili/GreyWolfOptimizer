import numpy as np
import time

class Graph(object):

    def __init__(self, adjMatrix):
        self.adjMatrix = adjMatrix

    def calculate_distance(self, v1, v2):
        dist = np.linalg.norm(v1 - v2)
        return dist

    def calculate_tour_distance(self, tour):
        total_dist = 0

        for i in range(len(tour) - 1):
            if self.adjMatrix[tour[i], tour[i + 1]] == -1:
                total_dist = np.inf
            else:
                total_dist += self.adjMatrix[tour[i], tour[i + 1]]

        if self.adjMatrix[tour[-1], tour[0]] == -1:
            total_dist = np.inf
        else:
            total_dist += self.adjMatrix[tour[-1], tour[0]]
        
        return total_dist