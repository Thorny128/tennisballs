from SimulationFiles.Simulation import Simulation

if __name__ == "__main__":
    num_simulations = 1
    num_points = 4
    human_weight = 5
    ball_weight = 1
    points = [[1, 2], [3, 5], [6, 1], [8, 3]]

    simulation = Simulation(1, 4, 1, 1, points)
    simulation.run_simulation()
    print("Done!")