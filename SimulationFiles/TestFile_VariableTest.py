from SimulationFiles.Simulation import Simulation

if __name__ == "__main__":
    num_simulations = 1
    num_points = 4
    human_weight = 1
    ball_weight = 1
    points = [[1, 2], [3, 5], [6, 1], [8, 3]]

    simulation = Simulation(num_simulations, num_points, human_weight, ball_weight, points)
    simulation.run_simulation()
    simulation.save_to_csv('vartest.csv')
    print("Done!")