import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io.wavfile import read

fs, audio_signal = read("chillin39-20915.wav")
print('\nSignal shape:', audio_signal.shape)
print('Signal Datatype:', audio_signal.dtype)
print('Signal duration:', round(audio_signal.shape[0] / float(fs), 2), 'seconds')
audio_signal = audio_signal / np.power(2, 15)
audio_signal = audio_signal [:1000]
time_axis = 1000 * np.arange(0, len(audio_signal), 1) / float(fs)
plt.plot(time_axis, audio_signal, color='blue')
plt.xlabel('Time (milliseconds)')
plt.ylabel('Amplitude')
plt.title('Input audio signal')

# Frequency domain
# We involve extracting the :length and half length of the signal
length_signal = len(audio_signal)
half_length = np.ceil((length_signal + 1) / 2.0).astype(np.int)

# Applying mathematics tools for transforming into frequency domain and using the Fourier Transform.
signal_frequency = np.fft.fft(audio_signal)

# Do the normalization of frequency domain signal and square it 
signal_frequency = abs(signal_frequency[0:half_length]) / length_signal
signal_frequency **= 2

# Extract the length and half length of the frequency transformed signal
len_fts = len(signal_frequency)

# Note that the Fourier transformed signal must be adjusted for even as well as odd case
if length_signal % 2:
   signal_frequency[1:len_fts] *= 2
else:
   signal_frequency[1:len_fts-1] *= 2
   
#  Extract the power in decibal(dB)
signal_power = 10 * np.log10(signal_frequency)

# Adjust the frequency in kHz for X-axis
x_axis = np.arange(0, half_length, 1) * (fs / length_signal) / 1000.0

# Visualize the characterization of signal
plt.figure()
plt.plot(x_axis, signal_power)
plt.xlabel('Frequency (kHz)')
plt.ylabel('Signal power (dB)')
plt.title('Frequency domain')
plt.show()
