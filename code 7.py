import numpy as np
import matplotlib.pyplot as plt

# Function to simulate y(t) = u(t) + u(t-1) + 3u(t+5)
def simulate_function(time):
    y = np.zeros_like(time)

    # u(t)
    y[time >= 0] += 1

    # u(t-1)
    y[time >= 1] += 1

    # 3u(t+5)
    y[time >= -5] += 3

    return y

# Define the time range
time = np.linspace(-10, 10, 1000)

# Generate the signal
function_values = simulate_function(time)

# Plot the signal
plt.figure(figsize=(8, 4))
plt.plot(time, function_values, linewidth=2)
plt.title('y(t) = u(t) + u(t-1) + 3u(t+5)')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.ylim(-0.5, 5.5)
plt.grid(True)
plt.show()