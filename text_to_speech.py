import wave
from pydub import AudioSegment
from pydub.generators import Sine
from scipy import signal
import numpy as np


def text_to_speech(text, filename):
    # Define the parameters for the audio file
    sample_rate = 44100
    bit_depth = 16
    duration = 2

    # Generate a sine wave with a frequency of 440 Hz to use as the carrier signal
    frequency = 440
    sine_wave = Sine(frequency).to_audio_segment(duration * 1000)

    # Define the text to be spoken and the speech rate
    text = text
    speech_rate = 200

    # Convert the text to binary using ASCII encoding
    binary_text = ' '.join(format(ord(char), '08b') for char in text)

    # Create a binary amplitude modulation (BAM) signal using the binary representation of the text
    t = np.linspace(0, duration, duration * sample_rate, endpoint=False)
    message_signal = np.zeros_like(t)
    for i, bit in enumerate(binary_text):
        if bit == '1':
            message_signal[i * sample_rate // speech_rate:(i + 1) * sample_rate // speech_rate] = 1

    # Modulate the sine wave with the BAM signal to produce the speech signal
    speech_signal = sine_wave._spawn((sine_wave.get_array_of_samples() * message_signal).astype(np.int16))

    # Apply a bandpass filter to the speech signal to remove any frequency components outside the range of human hearing
    b, a = signal.butter(6, [20, 20000], 'bandpass', fs=sample_rate)
    filtered_signal = signal.filtfilt(b, a, speech_signal.get_array_of_samples())

    # Normalize the signal and save it to a WAV file
    normalized_signal = np.int16(filtered_signal / np.max(np.abs(filtered_signal)) * (2 ** (bit_depth - 1) - 1))
    wav_file = wave.open(filename, 'wb')
    wav_file.setnchannels(1)
    wav_file.setsampwidth(bit_depth // 8)
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(normalized_signal.tobytes())
    wav_file.close()
    
    return b, a
