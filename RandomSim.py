from SimulationFiles.Simulation import Simulation

if __name__ == "__main__":
    # Change the value below
    NUM_SIMULATIONS = 1

    # Distance matrix for a large UPS facility and five smaller ones
    distance_matrix = [
        [0, 305, 71, 135, 100, 169],  # Distances from Pittsfield, MA (Large Facility)
        [305, 0, 235, 135, 180, 220],  # Distances from Bangor, ME
        [71, 235, 0, 105, 122, 150],  # Distances from Bristol, CT
        [135, 135, 105, 0, 45, 90],  # Distances from Albany, NY
        [100, 180, 122, 45, 0, 120],  # Distances from Worcester, MA
        [169, 220, 150, 90, 120, 0]  # Distances from Manchester, NH
    ]

    # Rough locations of large UPS facility and five smaller ones (approximate, not used in calculation)
    points = [
        [0, 0],  # Large Facility: Pittsfield, MA (origin)
        [0, 305],  # North: Bangor, ME
        [0, -71],  # South: Bristol, CT
        [-135, 0],  # West: Albany, NY
        [100, 0],  # East: Worcester, MA
        [169, 169],  # Northeast: Manchester, NH
        [0, 0]
    ]
    # A UPS truck typically weighs around 10,000 lbs when empty
    # Because the weights in this algorithm are relative, we will scale it down for efficiency
    ups_truck_weight = 10

    # A UPS truck typically weighs around 27,000 lbs when full
    # Because the weights in this algorithm are relative, we will scale it down for efficiency
    payload = 17
    # Five locations to pick up parcels
    payload_per_location = payload/5

    print("Starting Simulations")
    simulation = Simulation(NUM_SIMULATIONS, distance_matrix, points, ups_truck_weight, payload_per_location)
    simulation.run_simulation()
    simulation.save_to_csv('random_sim_output.csv')
    print("Done!")
