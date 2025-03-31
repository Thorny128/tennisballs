from SimulationFiles.Simulation import Simulation

if __name__ == "__main__":
    # Change the value below
    NUM_SIMULATIONS = 1

    # Sample distance matrix for 5 points (including the origin)
    distance_matrix = [
        [0, 2.24, 5.83, 6.08, 8.54],  # Distances from point 0 (origin)
        [2.24, 0, 3.61, 5.19, 7.07],  # Distances from point 1
        [5.83, 3.61, 0, 5, 5.39],  # Distances from point 2
        [6.08, 5.19, 5, 0, 2.83],  # Distances from point 3
        [8.54, 7.07, 5.39, 2.83, 0]  # Distances from point 4
    ]

    print("Starting Simulations")
    points = [[0, 0], [1, 2], [3, 5], [6, 1], [8, 3], [0, 0]]
    simulation = Simulation(NUM_SIMULATIONS, distance_matrix, points, 4, 1)
    simulation.run_simulation()
    simulation.save_to_csv('random_sim_output.csv')
    print("Done!")
