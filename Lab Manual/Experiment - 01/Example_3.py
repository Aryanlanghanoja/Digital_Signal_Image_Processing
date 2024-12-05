import matplotlib.pyplot as plt
import numpy as np


def simulate_discrete_unit_step(num_samples):
    unit_step = np.zeros(num_samples)
    unit_step[num_samples // 2:] = 1
    return unit_step


# Define the number of samples for the discrete unit step signal
num_samples = 20  # Number of samples

# Simulate the discrete unit step signal
discrete_unit_step = simulate_discrete_unit_step(num_samples)

# Plot and display the discrete unit step signal
plt.figure(figsize=(10, 6))
plt.stem(range(-num_samples//2, num_samples//2), discrete_unit_step)
plt.title('Discrete Unit Step Function u(n)')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.ylim([-2, 2])
plt.grid(True)
plt.tight_layout()
plt.show()
