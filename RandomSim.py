from SimulationFiles.Simulation import Simulation

if __name__ == "__main__":
    # Modify this
    NUM_SIMULATIONS = 10

    print("Starting Simulations")
    simulation = Simulation(NUM_SIMULATIONS)
    simulation.run_simulation()
    simulation.save_to_csv('random_sim_output.csv')
    print("Done!")
