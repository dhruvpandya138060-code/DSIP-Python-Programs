import numpy as np
import matplotlib.pyplot as plt

# Function to generate an impulse train
def simulate_impulse_train(signal_length, period):
    impulse_train = np.zeros(signal_length)

    for n in range(signal_length):
        if n % period == 0:
            impulse_train[n] = 1

    return impulse_train

# Define the parameters
signal_length = 100   # Length of the impulse train
period = 10           # Period of the impulse train

# Generate the impulse train
impulse_train = simulate_impulse_train(signal_length, period)

# Plot the impulse train
plt.figure(figsize=(8, 4))
plt.stem(range(signal_length), impulse_train)
plt.title('Impulse Train')
plt.xlabel('Sample (n)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# Optional: Save the impulse train array
# np.savetxt('impulse_train.txt', impulse_train, delimiter=',')