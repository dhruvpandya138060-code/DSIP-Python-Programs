import numpy as np
import matplotlib.pyplot as plt

# Function to generate a continuous unit step signal
def simulate_continuous_unit_step(time):
    unit_step = np.zeros_like(time)
    unit_step[time >= 0] = 1
    return unit_step

# Function to generate a discrete unit step signal
def simulate_discrete_unit_step(num_samples):
    unit_step = np.zeros(num_samples)
    unit_step[num_samples // 2:] = 1
    return unit_step

# Define the time range for the continuous unit step signal
time = np.linspace(-5, 5, 1000)

# Generate the continuous unit step signal
continuous_unit_step = simulate_continuous_unit_step(time)

# Define the number of samples for the discrete unit step signal
num_samples = 20

# Generate the discrete unit step signal
discrete_unit_step = simulate_discrete_unit_step(num_samples)

# Plot the signals
plt.figure(figsize=(10, 6))

# Continuous Unit Step
plt.subplot(2, 1, 1)
plt.plot(time, continuous_unit_step)
plt.title('Continuous Unit Step Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

# Discrete Unit Step
plt.subplot(2, 1, 2)
plt.stem(range(num_samples), discrete_unit_step)
plt.title('Discrete Unit Step Signal')
plt.xlabel('Sample (n)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# Optional: Save the signals
# np.savetxt('continuous_unit_step.txt', continuous_unit_step, delimiter=',')
# np.savetxt('discrete_unit_step.txt', discrete_unit_step, delimiter=',')