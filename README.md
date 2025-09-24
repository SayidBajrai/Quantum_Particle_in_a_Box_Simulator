# Quantum Particle-in-a-Box Simulator

A Python implementation of a quantum mechanics simulator that solves the time-dependent Schrödinger equation for particles in various potential configurations. This project visualizes quantum phenomena including wavefunction evolution, quantum tunneling, and resonance effects.

![Quantum Tunneling Visualization](https://img.shields.io/badge/Quantum-Tunneling-blue) ![Wavefunction Evolution](https://img.shields.io/badge/Wavefunction-Evolution-green)

## Features

- **Time-dependent Schrödinger equation solver** using finite difference methods
- **Multiple potential configurations**:
  - Infinite square well (particle in a box)
  - Potential barriers for tunneling demonstrations
  - Double barrier structures for resonance effects
- **Interactive visualizations** showing:
  - Real and imaginary parts of the wavefunction
  - Probability density |ψ|²
  - Potential energy landscape
- **Initial state options**:
  - Gaussian wavepackets
  - Energy eigenstates
  - Superposition states
- **Performance optimizations**:
  - Sparse matrix operations
  - Optional GPU acceleration with CuPy
- **Animation export** to GIF format

## Installation

### Prerequisites

- Python 3.7 or higher
- NumPy, SciPy, Matplotlib

### Install from source

```bash
git clone https://github.com/SayidBajrai/quantum-particle-in-a-box.git
cd quantum-particle-in-a-box
pip install -e .
```

### Optional GPU support

```bash
pip install cupy
```

## Quick Start

### Basic Simulation

```python
from quantum_simulator import QuantumSimulator, gaussian_wavepacket

# Initialize simulator
sim = QuantumSimulator(L=1.0, N=500, dt=0.0001)

# Set initial wavefunction (Gaussian wavepacket)
sim.set_initial_wavefunction(gaussian_wavepacket(sim.x))

# Run simulation
sim.evolve(total_time=0.5)

# Visualize results
sim.animate()
```

### Quantum Tunneling Demonstration

```python
from quantum_simulator import QuantumSimulator, barrier_potential, gaussian_wavepacket

# Create simulator with potential barrier
sim = QuantumSimulator(L=1.0, N=500, dt=0.0001)
sim.V = barrier_potential(sim.x, barrier_height=50.0, barrier_width=0.05)
sim.update_hamiltonian()

# Initialize wavepacket moving toward barrier
sim.set_initial_wavefunction(gaussian_wavepacket(sim.x, x0=0.2, k0=80.0))

# Run simulation
sim.evolve(total_time=0.4)

# Animate and save results
sim.animate(save_as="tunneling_demo.gif")
```

### Running Example Simulations

```python
from quantum_simulator.examples import (
    run_gaussian_wavepacket,
    run_tunneling_demo,
    run_double_barrier_resonance,
    run_superposition_state
)

# Run all example simulations
run_gaussian_wavepacket()
run_tunneling_demo()
run_double_barrier_resonance()
run_superposition_state()
```

## Examples

### 1. Gaussian Wavepacket in Infinite Well

![Gaussian Wavepacket](https://github.com/SayidBajrai/quantum-particle-in-a-box/raw/main/examples/gaussian_wavepacket.gif)

A Gaussian wavepacket bouncing back and forth in an infinite potential well, demonstrating wave packet dispersion.

### 2. Quantum Tunneling Through Barrier

![Quantum Tunneling](https://github.com/SayidBajrai/quantum-particle-in-a-box/raw/main/examples/tunneling_demo.gif)

Visualization of quantum tunneling where a wavepacket passes through a potential barrier despite having insufficient classical energy.

### 3. Double Barrier Resonance

![Double Barrier](https://github.com/SayidBajrai/quantum-particle-in-a-box/raw/main/examples/double_barrier_resonance.gif)

Demonstration of resonance effects in a double barrier structure, showing transmission peaks at specific energies.

### 4. Superposition State Evolution

![Superposition State](https://github.com/SayidBajrai/quantum-particle-in-a-box/raw/main/examples/superposition_state.gif)

Time evolution of a superposition of energy eigenstates, showing quantum interference patterns.

## Technical Details

### Numerical Methods

- **Spatial discretization**: Finite difference method with second-order accuracy
- **Time evolution**: Crank-Nicolson method for unitary evolution
- **Sparse matrices**: Efficient storage and operations using SciPy's sparse matrix capabilities
- **Boundary conditions**: Hard wall (infinite potential) at boundaries

### Performance

- CPU: Efficient for systems up to ~10,000 grid points
- GPU: Significant speedup with CuPy for larger systems
- Memory: O(N) storage requirements for N grid points

### Physical Parameters

- All simulations use natural units (ℏ = m = 1)
- Spatial domain: [0, L] with customizable length
- Time step: Automatically chosen for stability (Δt < 2m(Δx)²/ℏ)

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by quantum mechanics textbooks and computational physics resources
- Built with NumPy, SciPy, and Matplotlib
- Visualization techniques adapted from scientific computing best practices

## Citation

If you use this simulator in your research or teaching, please cite:

```bibtex
@misc{quantum_simulator,
  author = {Your Name},
  title = {Quantum Particle-in-a-Box Simulator},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/SayidBajrai/quantum-particle-in-a-box}}
}
```

## Support

For questions, bug reports, or feature requests, please:

1. Check the [Issues](https://github.com/SayidBajrai/quantum-particle-in-a-box/issues) page
2. Create a new issue if needed
3. Contact the maintainers at your.email@example.com

---

**Note**: This simulator is intended for educational and research purposes. While we strive for accuracy, users should verify results for critical applications.
