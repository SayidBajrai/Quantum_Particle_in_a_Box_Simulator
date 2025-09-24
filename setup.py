
from setuptools import setup, find_packages

setup(
    name="quantum_simulator",
    version="0.1.0",
    author="Quantum Simulation Team",
    description="Quantum Particle-in-a-Box Simulator with Tunneling Visualization",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20.0",
        "matplotlib>=3.3.0",
        "scipy>=1.7.0",
    ],
    extras_require={
        "gpu": ["cupy>=9.0.0"],
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)