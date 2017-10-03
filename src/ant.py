
class Ant(object):
    tour = []

    """docstring for Ant"""
    def __init__(self, initial_position):
        super(Ant, self).__init__()

        self.position = initial_position

    def add_step(self, step):
        self.tour.append(step)

    def clear_tour(self):
        self.tour = []
