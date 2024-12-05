import matplotlib.pyplot as plt
import numpy as np


def plot_signal_and_spectrum(signal, spectrum):
    # Create time axis for plotting
    time_axis = np.arange(len(signal))

    # Plot the original signal
    plt.subplot(2, 1, 1)
    plt.plot(time_axis, signal)
    plt.title('Original Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    # Plot the magnitude spectrum
    plt.subplot(2, 1, 2)
    plt.plot(time_axis, spectrum)
    plt.title('Magnitude Spectrum')
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')

    plt.tight_layout()
    plt.show()


# Define the discrete-time signal
time = np.linspace(0, 1, 500)
frequency1 = 5  # Frequency of the first sinusoidal component
frequency2 = 20  # Frequency of the second sinusoidal component
amplitude1 = 1  # Amplitude of the first sinusoidal component
amplitude2 = 0.5  # Amplitude of the second sinusoidal component
signal = amplitude1 * np.sin(2 * np.pi * frequency1 * time) + \
    amplitude2 * np.sin(2 * np.pi * frequency2 * time)


# Compute the FFT of the signal
fft_result = np.fft.fft(signal)

# Compute the magnitude spectrum of the FFT result
magnitude_spectrum = np.abs(fft_result)

# Compute the IFFT of the FFT result
reconstructed_signal = np.fft.ifft(fft_result)

# Display the original signal, the magnitude spectrum, and the reconstructed
# signal
plot_signal_and_spectrum(signal, magnitude_spectrum)

# Save the magnitude spectrum plot (optional)
# spectrum_path = 'Magnitude Spectrum.png'
# plt.plot(magnitude_spectrum)
# plt.title('Magnitude Spectrum')
# plt.xlabel('Frequency')
# plt.ylabel('Magnitude')
# plt.savefig(spectrum_path)
# print(f"Magnitude spectrum plot saved at: {spectrum_path}")
# plt.show()
