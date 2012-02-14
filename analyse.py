
import csv
import pylab
import numpy as np


reader = csv.reader(open("PCA_cooking_oils_CSV.dat", "r"))
times = np.array(reader.next())

spectra = [np.array(line) for line in reader]

for s in spectra[::5]:
    pylab.plot(times, s)

pylab.show()
        
