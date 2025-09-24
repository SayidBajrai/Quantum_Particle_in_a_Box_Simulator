from examples import run_gaussian_wavepacket, run_tunneling_demo, run_double_barrier_resonance, run_superposition_state

if __name__ == "__main__":
    print("Running Gaussian Wavepacket Simulation...")
    sim1 = run_gaussian_wavepacket()
    
    print("\nRunning Tunneling Demonstration...")
    sim2 = run_tunneling_demo()
    
    print("\nRunning Double Barrier Resonance...")
    sim3 = run_double_barrier_resonance()
    
    print("\nRunning Superposition State Simulation...")
    sim4 = run_superposition_state()