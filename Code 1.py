import numpy as np
import matplotlib.pyplot as plt

# Function to generate unit impulse signal
def unit_impulse(length, position):
    signal = np.zeros(length)
    signal[position] = 1
    return signal

# Parameters
start = -10      # Start value of the x-axis range
stop = 10        # Stop value of the x-axis range
step = 1         # Step size

# Generate x-axis values
x = np.arange(start, stop + step, step)

# Generate unit impulse signal at n = 0
position = abs(start) // step
impulse_signal = unit_impulse(len(x), position)

# Plot the signal
plt.figure(figsize=(8, 4))
plt.stem(x, impulse_signal)
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')
plt.title('Unit Impulse Signal')
plt.grid(True)
plt.show()