# Text To Speech

This project implements a modular framework for converting text into audio signals and visualizing their characteristics. It combines signal processing techniques with audio generation and provides tools for analyzing speech signals in both time and frequency domains.

## Table of Contents
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Dependencies](#dependencies)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [Visualization Examples](#visualization-examples)

## Features
- **Text-to-Speech Conversion:** Converts input text into an audio signal using binary amplitude modulation (BAM).
- **Audio Signal Processing:** Applies bandpass filtering to enhance audio quality.
- **Visualization:**
  - Time-domain plots
  - Spectrograms
  - Frequency-domain analysis
  - Filter response graphs
- Modular design for easy extension and reuse.

## Project Structure
```
├── main.py                  # Main script to execute the framework
├── text_to_speech.py        # Handles text-to-speech conversion
├── visualization.py         # Functions for audio visualization
```

## Dependencies
- Python 3.8+
- Libraries:
  - NumPy
  - SciPy
  - Matplotlib
  - PyDub

Install the required libraries using:
```bash
pip install numpy scipy matplotlib pydub
```

## Usage
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

3. Input text will be converted into an audio file (`hello.wav`), and the signal will be processed and visualized.

## How It Works
1. **Text-to-Speech Conversion:**
   - Converts input text to binary representation.
   - Generates a carrier sine wave modulated by the binary text signal (BAM).
   - Applies bandpass filtering to produce clean audio.

2. **Visualization:**
   - **Time-domain Plot:** Shows signal amplitude over time.
   - **Frequency-domain Analysis:** Performs Fourier transform to analyze spectral content.
   - **Spectrogram:** Displays the frequency content over time.
   - **Filter Response:** Visualizes the magnitude and phase response of the applied filter.

## Visualization Examples
- **Time-Domain Signal:**
  ![Time Domain](#)

- **Frequency Spectrum:**
  ![Frequency Spectrum](#)

- **Spectrogram:**
  ![Spectrogram](#)

- **Filter Response:**
  ![Filter Response](#)

## Future Enhancements
- Support for advanced text-to-speech synthesis techniques.
- Integration with real-world speech datasets for validation.
- Interactive web-based visualization tools.

---
This project demonstrates core concepts of signal processing and visualization, serving as a foundation for advanced speech processing applications.
