
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply
import scipy.sparse.linalg as sla

class QuantumSimulator:
    def __init__(self, L=1.0, N=500, m=1.0, hbar=1.0, dt=0.001, potential=None):
        """
        Initialize quantum particle-in-a-box simulator
        
        Parameters:
        L (float): Length of the box
        N (int): Number of spatial grid points
        m (float): Particle mass
        hbar (float): Reduced Planck's constant
        dt (float): Time step
        potential (callable): Potential function V(x)
        """
        self.L = L
        self.N = N
        self.m = m
        self.hbar = hbar
        self.dt = dt
        self.dx = L / (N - 1)
        self.x = np.linspace(0, L, N)
        
        # Default potential (infinite well)
        self.V = np.zeros(N) if potential is None else potential(self.x)
        
        # Kinetic energy operator (finite difference)
        kinetic_coeff = -hbar**2 / (2 * m * self.dx**2)
        diagonals = [np.ones(N-1), -2*np.ones(N), np.ones(N-1)]
        offsets = [-1, 0, 1]
        self.T = kinetic_coeff * diags(diagonals, offsets, shape=(N, N))
        
        # Hamiltonian
        self.H = self.T + diags(self.V, shape=(N, N))
        
        # Time evolution operator (we'll compute this on-the-fly)
        self.U_matrix = None
        
        # Wavefunction storage
        self.psi = None
        self.time = 0.0
        self.history = []
        
    def set_initial_wavefunction(self, psi0):
        """Set initial wavefunction (normalized)"""
        self.psi = psi0 / np.sqrt(np.sum(np.abs(psi0)**2) * self.dx)
        self.time = 0.0
        self.history = [self.psi.copy()]
        
    def step(self):
        """Evolve system by one time step"""
        if self.psi is None:
            raise ValueError("Initial wavefunction not set")
            
        # Compute time evolution operator action on current wavefunction
        self.psi = expm_multiply(-1j * self.H * self.dt / self.hbar, self.psi)
        self.time += self.dt
        self.history.append(self.psi.copy())
        
    def evolve(self, total_time):
        """Evolve system for a given total time"""
        steps = int(total_time / self.dt)
        for _ in range(steps):
            self.step()
            
    def probability_density(self):
        """Calculate probability density |ψ|²"""
        return np.abs(self.psi)**2
    
    def expectation_position(self):
        """Calculate expectation value of position"""
        return np.sum(self.x * self.probability_density()) * self.dx
    
    def update_potential(self, new_potential):
        """Update the potential and recalculate Hamiltonian"""
        self.V = new_potential(self.x) if callable(new_potential) else new_potential
        self.H = self.T + diags(self.V, shape=(self.N, self.N))
        self.U_matrix = None  # Reset time evolution operator
    
    def animate(self, interval=50, save_as=None):
        """Create animation of wavefunction evolution"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Setup plots
        line_real, = ax1.plot([], [], 'b-', label='Real part')
        line_imag, = ax1.plot([], [], 'r-', label='Imaginary part')
        line_prob, = ax2.plot([], [], 'k-', label='Probability density')
        potential_line, = ax2.plot([], [], 'g--', alpha=0.7, label='Potential')
        
        ax1.set_xlim(0, self.L)
        ax1.set_ylim(-1.1, 1.1)
        ax1.set_ylabel('Wavefunction')
        ax1.legend()
        ax1.grid(True)
        
        ax2.set_xlim(0, self.L)
        ax2.set_ylim(0, max(5, np.max(self.probability_density())*1.1))
        ax2.set_xlabel('Position')
        ax2.set_ylabel('Probability Density')
        ax2.legend()
        ax2.grid(True)
        
        time_text = ax1.text(0.02, 0.95, '', transform=ax1.transAxes)
        
        def init():
            line_real.set_data([], [])
            line_imag.set_data([], [])
            line_prob.set_data([], [])
            potential_line.set_data(self.x, self.V)
            time_text.set_text('')
            return line_real, line_imag, line_prob, potential_line, time_text
        
        def update(frame):
            psi = self.history[frame]
            line_real.set_data(self.x, np.real(psi))
            line_imag.set_data(self.x, np.imag(psi))
            line_prob.set_data(self.x, np.abs(psi)**2)
            time_text.set_text(f'Time = {frame*self.dt:.3f}')
            return line_real, line_imag, line_prob, potential_line, time_text
        
        frames = len(self.history)
        ani = FuncAnimation(fig, update, frames=frames, init_func=init,
                            interval=interval, blit=True)
        
        if save_as:
            ani.save(save_as, writer='pillow', fps=30)
            
        plt.tight_layout()
        plt.show()
        return ani

# Example potential functions
def infinite_well(x):
    """Infinite potential well (particle in a box)"""
    return np.zeros_like(x)

def barrier_potential(x, barrier_height=10.0, barrier_width=0.1, barrier_center=0.5):
    """Potential barrier for tunneling demonstration"""
    V = np.zeros_like(x)
    mask = (x > barrier_center - barrier_width/2) & (x < barrier_center + barrier_width/2)
    V[mask] = barrier_height
    return V

def double_barrier(x, height=10.0, width=0.05, separation=0.2):
    """Double barrier potential for resonance demonstration"""
    V = np.zeros_like(x)
    center1 = 0.4
    center2 = center1 + separation
    mask1 = (x > center1 - width/2) & (x < center1 + width/2)
    mask2 = (x > center2 - width/2) & (x < center2 + width/2)
    V[mask1] = height
    V[mask2] = height
    return V