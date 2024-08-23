from SimulationFiles.Simulation import Simulation

if __name__ == "__main__":
    # Modify these variables
    num_simulations = 1
    num_points = 4
    human_weight = 1
    ball_weight = 1
    points = [[0, 0], [1, 2], [3, 5], [6, 1], [8, 3], [0, 0]]

    # Don't touch this code
    print("Starting Simulation")
    simulation = Simulation(num_simulations, num_points, human_weight, ball_weight, points)
    simulation.run_simulation()
    simulation.save_to_csv('var_test.csv')
    print("Done!")