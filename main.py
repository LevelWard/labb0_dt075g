import numpy as np
import sounddevice as sd #https://python-sounddevice.readthedocs.io/en/0.4.6/usage.html
import soundfile as sf #https://pypi.org/project/soundfile/
import librosa #https://librosa.org/doc/latest/index.html
import matplotlib.pyplot as plt #https://matplotlib.org/stable/tutorials/pyplot.html
import matplotlib

filename = 'Orkester.wav'
# Extract audio from file. data = sound and fs = Hz.
data, fs = sf.read(filename, dtype='float32')

#print(np.ndarray.tolist(data))

print("Sampling rate: " + str(fs))
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing

#Reshape the data as timevector
shapeData = np.shape(data)
dataSize = shapeData[0]
timeVec = np.linspace(0, 0.01, dataSize)
timeVec = np.arange(dataSize)*0.01

#Plot the data
plt.figure()
plt.plot(timeVec, data)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Period time [Sec]")
plt.title("F(t)")
plt.show()
