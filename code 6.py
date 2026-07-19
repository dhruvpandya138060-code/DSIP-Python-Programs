import numpy as np
import matplotlib.pyplot as plt

# Function to generate a continuous sine wave
def simulate_continuous_sine_wave(time, amplitude, frequency, phase):
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * time + phase)
    return sine_wave

# Function to generate a discrete sine wave
def simulate_discrete_sine_wave(num_samples, sampling_frequency, amplitude, frequency, phase):
    time = np.arange(num_samples) / sampling_frequency
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * time + phase)
    return time, sine_wave

# Define the time range for the continuous sine wave
time = np.linspace(0, 1, 1000)  # 0 to 1 second

# Define the parameters
num_samples = 100          # Number of samples
sampling_frequency = 100   # Sampling frequency (Hz)
amplitude = 1              # Amplitude
frequency = 5              # Frequency (Hz)
phase = 0                  # Phase (radians)

# Generate the continuous sine wave
continuous_sine_wave = simulate_continuous_sine_wave(
    time, amplitude, frequency, phase
)

# Generate the discrete sine wave
discrete_time, discrete_sine_wave = simulate_discrete_sine_wave(
    num_samples, sampling_frequency, amplitude, frequency, phase
)

# Plot the signals
plt.figure(figsize=(10, 6))

# Continuous Sine Wave
plt.subplot(2, 1, 1)
plt.plot(time, continuous_sine_wave)
plt.title("Continuous Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Discrete Sine Wave
plt.subplot(2, 1, 2)
plt.stem(discrete_time, discrete_sine_wave)
plt.title("Discrete Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()

# Optional: Save the signals
# np.savetxt('continuous_sine_wave.txt', continuous_sine_wave, delimiter=',')
# np.savetxt('discrete_sine_wave.txt', discrete_sine_wave, delimiter=',')