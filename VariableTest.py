from SimulationFiles.Simulation import Simulation

if __name__ == "__main__":
    # Modify these variables
    num_simulations = 1
    num_points = 4
    human_weight = 190
    ball_weight = 87.5
    points = [[0, 0], [6, 3], [3, 4], [0, 8], [0, 4], [0, 0]]

    # Don't touch this code
    print("Starting Simulation")
    simulation = Simulation(num_simulations, num_points, human_weight, ball_weight, points)
    simulation.run_simulation()
    simulation.save_to_csv('var_test.csv')
    print("Done!")