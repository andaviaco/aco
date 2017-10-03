
class City(object):
    """docstring for City"""
    def __init__(self, distance, initial_pheromone):
        super(City, self).__init__()
        self.distance = distance
        self.phreromone = initial_pheromone
