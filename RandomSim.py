from SimulationFiles.Simulation import Simulation

if __name__ == "__main__":
    # Change the value below
    NUM_SIMULATIONS = 1

    # Sample distance matrix for 5 points (including the origin)
    distance_matrix = [
        [0, 2, 3, 4, 5],  # Distances from point 0 (origin)
        [2, 0, 1, 2, 3],  # Distances from point 1
        [3, 1, 0, 1, 2],  # Distances from point 2
        [4, 2, 1, 0, 1],  # Distances from point 3
        [5, 3, 2, 1, 0]  # Distances from point 4
    ]

    print("Starting Simulations")
    simulation = Simulation(NUM_SIMULATIONS, 3, 10, 50, distance_matrix=distance_matrix)
    simulation.run_simulation()
    simulation.save_to_csv('random_sim_output.csv')
    print("Done!")
