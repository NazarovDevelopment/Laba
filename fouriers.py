__author__ = 'Alexey'

import LoadNiceFile as lfile
import FourierMy as fourier

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2


startdata = lfile.loadfile("si.lvm")


fftdata = fourier.forwardfourier(startdata[:, 1])
print(fftdata)

freqdata = 1/startdata[:, 0]
print(freqdata)


plt2.plot(startdata[:, 0], startdata[:,1])
plt2.show()
plt.plot(freqdata, fftdata)
plt
plt.show()