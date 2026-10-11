
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, bilinear, lfilter, freqz

# Sampling frequency
fs = 16000
duration = 0.01
t = np.arange(0, duration, 1/fs)

# Generate four sine waves
x1 = np.sin(2*np.pi*1000*t)
x2 = np.sin(2*np.pi*2000*t)
x3 = np.sin(2*np.pi*3000*t)
x4 = np.sin(2*np.pi*4000*t)

# Plot individual sine waves
signals = [x1, x2, x3, x4]
freqs = [1000, 2000, 3000, 4000]

plt.figure(figsize=(10, 7))
for i in range(4):
    plt.subplot(4, 1, i+1)
    plt.plot(t, signals[i])
    plt.title(f'{freqs[i]} Hz Sine Wave')
    plt.xlabel('Time (seconds)')
    plt.grid(True)
plt.tight_layout()
plt.show()

# Add all four signals
x = x1 + x2 + x3 + x4

# Function to plot time and frequency domains
def plot_signal(signal, title):
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t, signal)
    plt.title(title + ' - Time Domain')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    n = len(signal)
    X = np.abs(np.fft.rfft(signal)) * 2 / n
    f = np.fft.rfftfreq(n, 1/fs)

    plt.subplot(2, 1, 2)
    plt.stem(f, X, basefmt=' ')
    plt.xlim(0, 6000)
    plt.title(title + ' - Frequency Domain')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Plot combined signal
plot_signal(x, 'Combined Signal')

# Function to design a filter using bilinear transformation
def design_filter(filter_type, cutoff):
    order = 4

    # Prewarp cutoff frequency
    wc = 2 * fs * np.tan(np.pi * cutoff / fs)

    if filter_type == 'butter':
        b, a = butter(order, wc, btype='low', analog=True)
    else:
        b, a = cheby1(order, 0.5, wc, btype='low', analog=True)

    return bilinear(b, a, fs=fs)

# Butterworth filter with 2 kHz cutoff
b1, a1 = design_filter('butter', 2000)
y1 = lfilter(b1, a1, x)
plot_signal(y1, 'Butterworth Output (2 kHz)')

# Chebyshev filter with 3 kHz cutoff
b2, a2 = design_filter('cheby', 3000)
y2 = lfilter(b2, a2, x)
plot_signal(y2, 'Chebyshev Output (3 kHz)')

# Plot filter frequency responses
for b, a, title in [
    (b1, a1, 'Butterworth Filter Response'),
    (b2, a2, 'Chebyshev Filter Response')
]:
    f, h = freqz(b, a, fs=fs)
    plt.figure(figsize=(9, 4))
    plt.plot(f, 20*np.log10(np.maximum(np.abs(h), 1e-8)))
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True)
    plt.show()

print("Butterworth coefficients:")
print("b =", b1)
print("a =", a1)

print("\nChebyshev coefficients:")
print("b =", b2)
print("a =", a2)
