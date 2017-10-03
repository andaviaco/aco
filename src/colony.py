cimport random as rand

from ant import Ant
from city import City


class Colony(object):
    """docstring for Colony"""
    def __init__(
        self,
        nodes,
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

        self.nodes = nodes
        self.initial_node = initial_node
        self.end_node = end_node
        self.nants = nants
        self.iterations = iterations
        self.evaporation_rate = evaporation_rate
        self.initial_pheromone = initial_pheromone
        self.influence_pheromone = influence_pheromone
        self.influence_heuristic = influence_heuristic
        self.added_pheromone = added_pheromone

    def initialize_cities(self):
        pass

    def initial_ants(self):
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
        pass
