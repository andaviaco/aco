
class City(object):
    """docstring for City"""
    def __init__(self, name, initial_pheromone):
        super(City, self).__init__()
        self.name = name
        self.pheromone = initial_pheromone

    def __repr__(self):
        return f'<City {self.name}: {self.pheromone}>'
