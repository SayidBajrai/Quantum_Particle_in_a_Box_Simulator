 
import numpy as np
from simulator import QuantumSimulator, barrier_potential, double_barrier
from utils import gaussian_wavepacket, superposition_state

def run_gaussian_wavepacket():
    """Simulate Gaussian wavepacket in infinite well"""
    sim = QuantumSimulator(L=1.0, N=500, dt=0.0001)
    sim.set_initial_wavefunction(gaussian_wavepacket(sim.x))
    sim.evolve(total_time=0.5)
    sim.animate(interval=20, save_as="gaussian_wavepacket.gif")
    return sim

def run_tunneling_demo():
    """Simulate quantum tunneling through a barrier"""
    sim = QuantumSimulator(L=1.0, N=500, dt=0.0001)
    sim.V = barrier_potential(sim.x, barrier_height=50.0, barrier_width=0.05)
    sim.H = sim.T + sim.U.__class__(sim.V)  # Update Hamiltonian
    sim.U = sim.U.__class__(-1j * sim.H * sim.dt / sim.hbar)  # Update time evolution operator
    
    sim.set_initial_wavefunction(gaussian_wavepacket(sim.x, x0=0.2, k0=80.0))
    sim.evolve(total_time=0.4)
    sim.animate(interval=20, save_as="tunneling_demo.gif")
    return sim

def run_double_barrier_resonance():
    """Simulate resonance in double barrier structure"""
    sim = QuantumSimulator(L=1.0, N=500, dt=0.0001)
    sim.V = double_barrier(sim.x, height=30.0, width=0.03, separation=0.15)
    sim.H = sim.T + sim.U.__class__(sim.V)
    sim.U = sim.U.__class__(-1j * sim.H * sim.dt / sim.hbar)
    
    sim.set_initial_wavefunction(gaussian_wavepacket(sim.x, x0=0.1, k0=60.0))
    sim.evolve(total_time=0.6)
    sim.animate(interval=20, save_as="double_barrier_resonance.gif")
    return sim

def run_superposition_state():
    """Simulate superposition of energy eigenstates"""
    sim = QuantumSimulator(L=1.0, N=500, dt=0.0001)
    sim.set_initial_wavefunction(superposition_state(sim.x, n1=1, n2=3))
    sim.evolve(total_time=1.0)
    sim.animate(interval=20, save_as="superposition_state.gif")
    return sim