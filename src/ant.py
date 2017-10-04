
class Ant(object):
    last_position = None
    tour = []

    """docstring for Ant"""
    def __init__(self, name, initial_position):
        super(Ant, self).__init__()

        self.name = name
        self.__position = initial_position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.last_position = self.__position
        self.__position = position

    def add_step(self, step):
        self.tour.append(step)

    def clear_tour(self):
        self.tour = []

    def __repr__(self):
        return f'<Ant {self.name}: {self.position}>'
