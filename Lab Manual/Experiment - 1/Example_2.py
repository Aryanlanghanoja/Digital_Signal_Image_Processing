import matplotlib.pyplot as plt
import numpy as np


def simulate_function(time):
    y = np.zeros_like(time)
    y[time == 0] = 3
    y[time == 5] += 5
    y[time == 7] += 8
    return y


# Define the time range
time = np.arange(-10, 11)

# Simulate the function
function_values = simulate_function(time)

# Plot and display the function
plt.stem(time, function_values)
plt.title('Function y(t) = 3 * delta(n) + 5 * delta(-n-5) + 8 * delta(n-7)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.ylim([0, 10])
plt.grid(True)
plt.show()
