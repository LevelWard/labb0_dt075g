import numpy as np
import sounddevice as sd #https://python-sounddevice.readthedocs.io/en/0.4.6/usage.html
import soundfile as sf #https://pypi.org/project/soundfile/
import librosa #https://librosa.org/doc/latest/index.html

filename = 'Orkester.wav'
# Extract audio from file. data = sound and fs = Hz.
data, fs = sf.read(filename, dtype='float32')
print("Sampling rate: " + str(fs))
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing


