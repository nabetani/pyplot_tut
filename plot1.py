import math
import numpy as np
from matplotlib import pyplot
from matplotlib.backends.backend_pdf import PdfPages
import csv


def read_csv(fn):
    v = []
    with open(fn) as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        for row in reader:
            v.append(row[0:2] + [[float(x) for x in row[2:]]])
    return v


def write_pdf(fn):
    with PdfPages(fn) as pdf:
        fignums = pyplot.get_fignums()
        for fignum in fignums:
            pyplot.figure(fignum)
            pdf.savefig()


def plot_op(fig, hoge, fuga, op):
    params = ["foo", "bar", "baz"]
    for ix in range(len(params)):
      sparam = params[ix]
      graph = fig.add_subplot(3, 1, ix+1)  # nrows, ncols, index
      key = [sparam, op]
      for name, data in [["hoge", hoge], ["fuga", fuga]]:
        seq = [x for x in data if x[0:2]==key][0]
        y = seq[2]
        x=range(len(y))
        graph.plot(x,y)


def main():
    hoge=read_csv("hoge.csv")
    fuga=read_csv("fuga.csv")
    for op in ["aap", "noot", "mies", "zus", "jet"]:
        plot_op(pyplot.figure(), hoge, fuga, op)
    write_pdf("graph.pdf")


main()