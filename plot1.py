import math
import numpy as np
from matplotlib import pyplot
from matplotlib.backends.backend_pdf import PdfPages

x  = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

pyplot.figure()

pyplot.plot(x, y1)

pyplot.figure()
pyplot.plot(x, y2)

pdf = PdfPages('test2.pdf')

fignums = pyplot.get_fignums()
for fignum in fignums:
  pyplot.figure(fignum)
  pdf.savefig()

pdf.close()