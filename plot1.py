import math
import numpy as np
from matplotlib import pyplot
from matplotlib.backends.backend_pdf import PdfPages

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig = pyplot.figure()
axis1 = fig.add_subplot(2, 1, 1)  # nrows, ncols, index
axis1.plot(x, y1)
axis2 = fig.add_subplot(2, 1, 2)  # nrows, ncols, index
axis2.plot(x, y2)

pdf = PdfPages('test2.pdf')

fignums = pyplot.get_fignums()
for fignum in fignums:
    pyplot.figure(fignum)
    pdf.savefig()

pdf.close()
