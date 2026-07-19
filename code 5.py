import numpy as np
import matplotlib.pyplot as plt

# Function to generate a continuous parabolic signal
def simulate_continuous_parabolic(time, coefficients):
    parabolic_signal = np.polyval(coefficients, time)
    return parabolic_signal

# Function to generate a discrete parabolic signal
def simulate_discrete_parabolic(num_samples, coefficients):
    parabolic_signal = np.polyval(coefficients, np.arange(num_samples))
    return parabolic_signal

# Define the time range for the continuous parabolic signal
time = np.linspace(-5, 5, 1000)

# Define the number of samples and coefficients
num_samples = 20
coefficients = [1, 2, 1]   # Represents y = x² + 2x + 1

# Generate the signals
continuous_parabolic = simulate_continuous_parabolic(time, coefficients)
discrete_parabolic = simulate_discrete_parabolic(num_samples, coefficients)

# Plot the signals
plt.figure(figsize=(10, 6))

# Continuous Parabolic Signal
plt.subplot(2, 1, 1)
plt.plot(time, continuous_parabolic)
plt.title('Continuous Parabolic Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

# Discrete Parabolic Signal
plt.subplot(2, 1, 2)
plt.stem(range(num_samples), discrete_parabolic)
plt.title('Discrete Parabolic Signal')
plt.xlabel('Sample (n)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# Optional: Save the signal arrays
# np.savetxt('continuous_parabolic.txt', continuous_parabolic, delimiter=',')
# np.savetxt('discrete_parabolic.txt', discrete_parabolic, delimiter=',')