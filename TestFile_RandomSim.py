from SimulationFiles.Simulation import Simulation

if __name__ == "__main__":
    simulation = Simulation(10)
    simulation.run_simulation()
    simulation.save_to_csv('random_sim_test.csv')
    print("Done!")