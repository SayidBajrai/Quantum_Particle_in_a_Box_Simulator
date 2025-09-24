
import numpy as np

def gaussian_wavepacket(x, x0=0.2, sigma=0.05, k0=50.0):
    """Create a Gaussian wavepacket"""
    normalization = (2 * np.pi * sigma**2)**(-0.25)
    return normalization * np.exp(-(x - x0)**2 / (4 * sigma**2)) * np.exp(1j * k0 * x)

def superposition_state(x, n1=1, n2=2, L=1.0):
    """Create a superposition of two energy eigenstates"""
    psi1 = np.sqrt(2/L) * np.sin(n1 * np.pi * x / L)
    psi2 = np.sqrt(2/L) * np.sin(n2 * np.pi * x / L)
    return (psi1 + psi2) / np.sqrt(2)

def energy_eigenstate(x, n=1, L=1.0):
    """Create the nth energy eigenstate"""
    return np.sqrt(2/L) * np.sin(n * np.pi * x / L)