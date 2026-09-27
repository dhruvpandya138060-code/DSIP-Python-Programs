import numpy as np
import matplotlib.pyplot as plt

# Discrete-time signal
signal = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Compute FFT
fft_result = np.fft.fft(signal)

# Compute Magnitude Spectrum
magnitude_spectrum = np.abs(fft_result)

# Compute Phase Spectrum
phase_spectrum = np.angle(fft_result)

# Compute IFFT
reconstructed_signal = np.fft.ifft(fft_result)

# Display results
print("Original Signal:")
print(signal)

print("\nFFT Result:")
print(fft_result)

print("\nMagnitude Spectrum:")
print(magnitude_spectrum)

print("\nPhase Spectrum:")
print(phase_spectrum)

print("\nReconstructed Signal using IFFT:")
print(np.real(reconstructed_signal))

# Plot Original Signal
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.stem(signal)
plt.title("Original Discrete-Time Signal")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid()

# Plot Magnitude Spectrum
plt.subplot(3, 1, 2)
plt.stem(magnitude_spectrum)
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency Index")
plt.ylabel("Magnitude")
plt.grid()

# Plot Reconstructed Signal
plt.subplot(3, 1, 3)
plt.stem(np.real(reconstructed_signal))
plt.title("Reconstructed Signal using IFFT")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
