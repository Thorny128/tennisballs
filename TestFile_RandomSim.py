from SimulationFiles.Simulation import Simulation

if __name__ == "__main__":
    simulation = Simulation(10, 5)
    simulation.run_simulation()
    simulation.save_to_csv('test.csv')
    print("Done!")