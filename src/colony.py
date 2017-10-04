import random as rand
import pprint as pp

from ant import Ant
from edge import Edge


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

        self.edges = edges
        self.initial_node = initial_node
        self.end_node = end_node
        self.nants = nants
        self.iterations = iterations
        self.evaporation_rate = evaporation_rate
        self.influence_pheromone = influence_pheromone
        self.influence_heuristic = influence_heuristic
        self.added_pheromone = added_pheromone

        self.edges = self.initialize_edges(edges, initial_pheromone)
        self.ants = self.initialize_ants(nants, initial_node)

    def initialize_edges(self, edges, initial_pheromone):
        return {key: Edge(key, d, initial_pheromone) for key, d in edges.items()}

    def initialize_ants(self, nants, node):
        return [Ant(i, node) for i in range(1, nants + 1)]

    def optimize(self):
        for niteration in range(self.iterations):
            for ant in self.ants:
                ant.position = self.initial_node
                ant.clear_tour()

                while ant.position != self.end_node:
                    posible_edges = self.get_possible_edges(ant.position, ant.last_position)

                    probabilities = [self.get_probability(edge, posible_edges) for edge in posible_edges]
                    selected_index = self.roulette_selection(probabilities)
                    pp.pprint(f'Current pos: {ant.position} [{selected_index}] - {posible_edges}')
                    _, to_city = posible_edges[selected_index]
                    ant.position = to_city

    def get_possible_edges(self, position, last_position):
        posibles = list(self.edges.keys())[:]

        try:
            posibles.remove((position, last_position))
        finally:
            return [edge for edge in posibles if edge[0] == position]

    def get_probability(self, edge, allowed_edges):
        edges_sum = sum([self.edge_rel(aedge) for aedge in allowed_edges])
        probability = self.edge_rel(edge) / edges_sum

        return probability

    def edge_rel(self, edge):
        pheromone = self.edges[edge].pheromone ** self.influence_pheromone
        distance = self.edges[edge].distance ** self.influence_heuristic

        return pheromone / distance

    def get_pheromone(self):
        pass

    def get_pheromone_delta(self):
        pass

    def get_tour_len(self):
        pass

    def roulette_selection(self, fs):
        p = rand.uniform(0, sum(fs))

        for i, f in enumerate(fs):
            p -= f

            if p <= 0:
                break

        return i
