import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

audio_file = 'record.wav'

# Read the audio file
sample_rate, data = wavfile.read(audio_file)

# Read the audio file
sample_rate, data = wavfile.read(audio_file)

# if Stero, select only one channel 
if data.ndim > 1:
  data = data[:, 0]

# Fourier Transform
frequencies = np.fft.fftfreq(len(data), 1/sample_rate)
magnitude = np.abs(np.fft.fft(data))                           

# Plotting the audio data
plt.figure(figsize=(12,6))

# Plotting the signal 
plt.subplot(2,1,1)
plt.plot(data)
plt.title("Audio Waveform")

plt.xlabel("Sample")
plt.ylabel("Amplitude")

# Plotting the frequency spectrum 

plt.subplot(2,1,2)
plt.plot(frequencies, magnitude)
plt.title("Frequency Spectrum")
plt.xlabel("Frequency(Hz)")
plt.ylabel("Magnitude")
plt.xlim(0,sample_rate / 2) #Limit x-axis to half the sampling rate 

plt.tight_layout()
plt.show()