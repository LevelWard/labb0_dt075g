import numpy as np
import sounddevice as sd #https://python-sounddevice.readthedocs.io/en/0.4.6/usage.html
import soundfile as sf #https://pypi.org/project/soundfile/
import matplotlib.pyplot as plt

def playFile(filename):
    # Extract audio from file. data = sound and fs = Hz.
    data, fs = sf.read(filename, dtype='float32')

    # print(np.ndarray.tolist(data))

    print("Sampling rate: " + str(fs))
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing


def plotFileData(filename):
    data, fs = sf.read(filename, dtype='float32')
    # Reshape the data as timevector
    shapeData = np.shape(data)
    dataSize = shapeData[0]
    timeVec = np.linspace(0, 0.01, dataSize)
    timeVec = np.arange(dataSize) * 0.01
    # Plot the data
    plt.figure()
    plt.plot(timeVec, data)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Period time [Sec]")
    plt.title("F(t)")
    plt.show()


audioFile = "Orkester.wav"
plotFileData(audioFile)
playFile(audioFile)
