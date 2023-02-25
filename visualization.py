import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import wave

def read_audio_file(filename):
    # Open the audio file
    with wave.open(filename, 'rb') as wav_file:
        # Get the sample rate and number of audio frames
        sample_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()

        # Read the audio data
        audio_data = wav_file.readframes(num_frames)

    # Convert the audio data to a numpy array
    audio_signal = np.frombuffer(audio_data, dtype=np.int16)

    return audio_signal, sample_rate

def fourier_transform(signal, sample_rate):
    """Compute the one-sided Fourier transform of a signal.
    
    Args:
        signal (numpy.ndarray): Input signal.
        sample_rate (int): Sampling rate of the signal.
    
    Returns:
        freqs (numpy.ndarray): Frequencies in Hz.
        spectrum (numpy.ndarray): One-sided spectrum in dB.
    """
    # Compute the one-sided Fourier transform
    spectrum = np.abs(np.fft.rfft(signal))
    
    # Convert to dB scale
    spectrum = 20 * np.log10(spectrum)
    
    # Compute the corresponding frequency axis
    freqs = np.fft.rfftfreq(len(signal), 1/sample_rate)
    
    return freqs, spectrum



def plot_signal(signal, sample_rate):
    """Plots the given signal in the time domain."""
    time_axis = np.linspace(0, len(signal) / sample_rate, len(signal))
    plt.plot(time_axis, signal)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Signal in the Time Domain')
    plt.show()


def plot_spectrum(signal, sample_rate, window=None):
    """Plot the spectrum of a signal.
    
    Args:
        signal (numpy.ndarray): Input signal.
        sample_rate (int): Sampling rate of the signal.
        window (callable): Window function to apply to the signal.
    """
    # Apply the window function if specified
    if window:
        signal = signal * window(len(signal))
        
    # Compute the one-sided Fourier transform
    freqs, spectrum = fourier_transform(signal, sample_rate)
    
    # Plot the spectrum
    plt.plot(freqs, spectrum)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude (dB)')
    plt.title("Spectrum of Audio Signal")
    plt.show()

def plot_spectrogram(signal, sample_rate):
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_title('Spectrogram')
    ax.set_xlabel('Time')
    ax.set_ylabel('Frequency')
    ax.specgram(signal, Fs=sample_rate)
    plt.show()


def plot_filter(b, a, sample_rate):
    """Plots the frequency response of the given filter."""
    w, h = signal.freqz(b, a)
    freq_axis = w / (2 * np.pi) * sample_rate
    magnitude = 20 * np.log10(abs(h))
    phase = np.unwrap(np.angle(h)) * 180 / np.pi
    plt.plot(freq_axis, magnitude)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.title('Frequency Response of the Filter')
    plt.show()
    
    plt.plot(freq_axis, phase)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (degrees)')
    plt.title('Phase Response of the Filter')
    plt.show()
