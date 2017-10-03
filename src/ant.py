
class Ant(object):
    tour = []

    """docstring for Ant"""
    def __init__(self, name, initial_position):
        super(Ant, self).__init__()

        self.name = name
        self.position = initial_position

    def add_step(self, step):
        self.tour.append(step)

    def clear_tour(self):
        self.tour = []

    def __repr__(self):
        return f'<Ant {self.name}: {self.position}>'
