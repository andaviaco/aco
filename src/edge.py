
class Edge(object):
    """docstring for Edge"""
    def __init__(self, name, distance, initial_pheromone):
        super(Edge, self).__init__()
        self.name = name
        self.distance = distance
        self.pheromone = initial_pheromone

    def __repr__(self):
        return f'<Edge {self.name}: {self.pheromone}>'
