import numpy as np
import matplotlib.pyplot as plt

# Function to simulate y(t) = δ(t) + δ(t-1) + 3δ(t+5)
def simulate_function(time):
    y = np.zeros_like(time)

    # δ(t)
    y[time == 0] = 1

    # δ(t-1)
    y[time == 1] += 1

    # 3δ(t+5)
    y[time == -5] += 3

    return y

# Define the discrete time range
time = np.arange(-10, 11)

# Generate the signal
function_values = simulate_function(time)

# Plot the signal
plt.figure(figsize=(8, 4))
plt.stem(time, function_values)
plt.title('y(t) = δ(t) + δ(t-1) + 3δ(t+5)')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.ylim(-0.5, 4.5)
plt.grid(True)
plt.show()