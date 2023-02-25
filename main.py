from text_to_speech import text_to_speech
from visualization import plot_signal, plot_spectrum, plot_spectrogram, plot_filter, read_audio_file
import numpy as np

text = "Hello, how are you doing today?"
filename = "hello.wav"

b, a = text_to_speech(text, filename)

signal, sample_rate = read_audio_file(filename)


plot_signal(signal, sample_rate)
plot_spectrum(signal, sample_rate)
plot_spectrogram(signal, sample_rate)
plot_filter(b, a, sample_rate)
