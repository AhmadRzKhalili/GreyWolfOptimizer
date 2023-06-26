import random
import numpy as np
import matplotlib.pyplot as plt

class GW_Optimizer(object):

    def __init__(self, graph, max_num_iteration, num_wolves):
        self.graph = graph
        self.max_num_iteration = max_num_iteration
        self.num_wolves = num_wolves

    def init_population(self):
        population = []

        for i in range(self.num_wolves):
            solution_tour = np.random.permutation(len(self.graph.adjMatrix))
            population.append(solution_tour)

        self.population = population
    
    def optimize(self):
        self.init_population()

        for i in range(self.max_num_iteration):
            alpha_index, beta_index, delta_index = self.get_wolf_indices()

            X_alpha = self.population[alpha_index]
            X_beta = self.population[beta_index]
            X_delta = self.population[delta_index]

            a = 2 - i * (2 / self.max_num_iteration)

            for i in range(self.num_wolves):
                
                if i != alpha_index and i != beta_index and i != delta_index:
                
                    X_p = self.population[i]

                    C_alpha = 2 * np.random.rand(len(self.graph.adjMatrix))
                    D_alpha = np.abs(C_alpha * X_alpha - X_p)
                    A_alpha = 2 * a * np.random.rand(len(self.graph.adjMatrix)) - a
                    X1 = X_alpha - (A_alpha * D_alpha)

                    C_beta = 2 * np.random.rand(len(self.graph.adjMatrix))
                    D_beta = np.abs(C_beta * X_beta - X_p)
                    A_beta = 2 * a * np.random.rand(len(self.graph.adjMatrix)) - a
                    X2 = X_beta - (A_beta * D_beta)

                    C_delta = 2 * np.random.rand(len(self.graph.adjMatrix))
                    D_delta = np.abs(X_delta - X_p)
                    A_delta = 2 * a * np.random.rand(len(self.graph.adjMatrix)) - a
                    X3 = X_delta - (A_delta * D_delta)

                    new_position = (X1 + X2 + X3) / 3

                    self.population[i] = self.repair_position(new_position)
         
            
        
        best_tour = self.population[alpha_index]
        best_distance = self.graph.calculate_tour_distance(best_tour)
        return best_tour, best_distance

    def get_wolf_indices(self):

        fitness = [self.graph.calculate_tour_distance(solution_tour) for solution_tour in self.population]

        index_arr = np.argsort(fitness)
        alpha_index = index_arr[1]
        beta_index = index_arr[2]
        delta_index = index_arr[3]

        return alpha_index, beta_index, delta_index

    def repair_position(self, position):
        sorted_indices = np.argsort(position)
        repaired_pos = np.zeros_like(position, dtype=int)
        visited = np.zeros(len(self.graph.adjMatrix), dtype=bool)

        for i in range(len(self.graph.adjMatrix)):
            city = sorted_indices[i]
            if visited[city]:
                j = 0
                while visited[j]:
                    j += 1
                repaired_pos[i] = j
                visited[j] = True
            else:
                repaired_pos[i] = city
                visited[city] = True

        return repaired_pos
