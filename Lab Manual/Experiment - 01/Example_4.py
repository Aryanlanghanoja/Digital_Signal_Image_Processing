import matplotlib.pyplot as plt
import numpy as np


def simulate_discrete_unit_step(num_samples, delay):
    unit_step = np.zeros(num_samples)
    unit_step[delay:] = 1
    return unit_step


# Define the number of samples for the discrete unit step signal
num_samples = 20  # Number of samples
delay = 7  # Delay by 7 samples

# Simulate the discrete unit step signal
discrete_unit_step = simulate_discrete_unit_step(num_samples, delay)

# Plot and display the discrete unit step signal
plt.figure(figsize=(10, 6))
plt.stem(range(num_samples), discrete_unit_step)
plt.title('y(n) = u(n-7)')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()
