from SimulationFiles.Simulation import Simulation

if __name__ == "__main__":
    print("Starting Simulation")

    # Modify these variables
    num_simulations = 1
    num_points = 4
    human_weight = 190
    ball_weight = 87.5
    points = [[0, 0], [0, 10], [3, 8], [4, 7], [4, 6], [8, 7], [9, 7], [7, 3], [8, 0], [4, 0], [0, 2], [0, 0]]

    # Don't touch this code
    simulation = Simulation(num_simulations, num_points, human_weight, ball_weight, points)
    simulation.run_simulation()
    simulation.save_to_csv('var_test.csv')
    print("Done!")