import os

mp3_files = sorted([f for f in os.listdir("/content") if f.endswith(".mp3")])

print(mp3_files)

import librosa
import numpy as np
import matplotlib.pyplot as plt
import os

# Find uploaded MP3 files automatically
files = sorted([f for f in os.listdir("/content") if f.endswith(".mp3")])

print("Files Found:")
for i, f in enumerate(files):
    print(i+1, f)

# Assign files
original_file = files[0]
karaoke_file = files[1]
different_file = files[2]

# Load audio
original, sr = librosa.load(original_file, sr=None)
karaoke, sr = librosa.load(karaoke_file, sr=None)
different, sr = librosa.load(different_file, sr=None)

# Make equal length
length = min(len(original), len(karaoke), len(different))

original = original[:length]
karaoke = karaoke[:length]
different = different[:length]

# Correlation values
corr1 = np.corrcoef(original, karaoke)[0,1]
corr2 = np.corrcoef(original, different)[0,1]
corr3 = np.corrcoef(karaoke, different)[0,1]

print("\nCorrelation Results")
print("----------------------")
print("Original vs Karaoke :", corr1)
print("Original vs Different :", corr2)
print("Karaoke vs Different :", corr3)

# Waveforms
plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(original)
plt.title("Original Song")

plt.subplot(3,1,2)
plt.plot(karaoke)
plt.title("Karaoke Version")

plt.subplot(3,1,3)
plt.plot(different)
plt.title("Different Song")

plt.tight_layout()
plt.show()

# Cross Correlation Graphs
pairs = [
    ("Original vs Karaoke", original, karaoke),
    ("Original vs Different", original, different),
    ("Karaoke vs Different", karaoke, different)
]

for title, s1, s2 in pairs:
    corr = np.correlate(s1, s2, mode='full')
    corr = corr / np.max(np.abs(corr))

    plt.figure(figsize=(10,4))
    plt.plot(corr)
    plt.title(title)
    plt.grid(True)
    plt.show()