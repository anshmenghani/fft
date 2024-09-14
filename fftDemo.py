#this is just a demo version

from PIL import Image
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

img = Image.open(r"C:\Users\anshm\Downloads\s5.jpg")
transform = fft(np.ravel(np.array(img)))
n = np.arange(len(transform))
plt.plot(n, np.abs(transform))
plt.xlabel('Frequency')
plt.ylabel('FFT Amplitude')
plt.show()
