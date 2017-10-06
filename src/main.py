from colony import Colony


def main():
    edges = {
        (1, 2): 5,
        (1, 3): 3.1,
        (1, 6): 5.2,
        (2, 1): 5,
        (2, 3): 4.9,
        (2, 7): 5.2,
        (3, 1): 3.1,
        (3, 2): 4.9,
        (3, 5): 6,
        (3, 6): 3.2,
        (3, 7): 3,
        (4, 5): 5.5,
        (4, 7): 4.8,
        (5, 3): 6,
        (5, 4): 5.5,
        (5, 6): 4.7,
        (6, 1): 5.2,
        (6, 3): 3.2,
        (6, 5): 4.7,
        (7, 2): 5.2,
        (7, 3): 3,
        (7, 4): 4.8,
    }

    initial_node = 1
    end_node = 4
    ants = 5
    iterations = 10

    colony = Colony(edges, initial_node, end_node, ants, iterations)
    best_path = colony.optimize()
    print(f'Mejor Camino: {best_path}')

if __name__ == '__main__':
    main()
