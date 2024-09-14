import matplotlib.pyplot as plt
import numpy as np


def simulate_function(time):
    y = np.zeros_like(time)

    y[time >= 0] = 1  # u(t)
    y[time >= 3] += 1  # u(t-3)
    y[time >= 2] += 6  # 6*u(n-2)
    y[time <= 1] += 8  # 8*u(-n-1)
    
    return y


# Define the time range
time = np.arange(-10, 11)

# Simulate the function
function_values = simulate_function(time)

# Plot and display the function
plt.stem(time, function_values)
plt.title('Function y(t) = u(n) + u(n-3) + 6*u(n-2) + 8*(-n-1)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.ylim([-1, 10])
plt.grid(True)
plt.show()
