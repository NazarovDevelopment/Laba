__author__ = 'Alexey'
import numpy as np
def forwardfourier(data):
    newfftdata = np.fft.fft(data)
    print(data)
    return newfftdata