import random as rand
import pprint as pp

from ant import Ant
from city import City


class Colony(object):
    """docstring for Colony"""
    def __init__(
        self,
        edges,
        initial_node,
        end_node,
        nants,
        iterations,
        *,
        evaporation_rate=0.5,
        initial_pheromone=0.00001,
        influence_pheromone=1,
        influence_heuristic=5,
        added_pheromone=1
    ):
        super(Colony, self).__init__()

        self.initial_node = initial_node
        self.end_node = end_node
        self.nants = nants
        self.iterations = iterations
        self.evaporation_rate = evaporation_rate
        self.influence_pheromone = influence_pheromone
        self.influence_heuristic = influence_heuristic
        self.added_pheromone = added_pheromone

        self.cities = self.initialize_cities(edges, initial_pheromone)
        self.ants = self.initialize_ants(nants, initial_node)

    def initialize_cities(self, edges, initial_pheromone):
        keys = set(sum(edges, ())) # flat list and unique values

        return {key: City(key, initial_pheromone) for key in keys}

    def initialize_ants(self, nants, node):
        return [Ant(i, node) for i in range(1, nants + 1)]

    def reset_ants(self, ants):
        pass

    def optimize(self):
        pass

    def get_pheromone(self):
        pass

    def get_possible_cities(self):
        pass

    def get_tour_len(self):
        pass

    def get_probability(self):
        pass

    def roulette_selection(self, fs):
        p = rd.uniform(0, sum(fs))

        for i, f in enumerate(fs):
            if p <= 0:
                break
            p -= f
        return i
