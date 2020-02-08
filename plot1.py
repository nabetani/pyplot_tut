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
    fig.suptitle(op)
    params = ["foo", "bar", "baz"]
    for ix in range(len(params)):
        sparam = params[ix]
        graph = fig.add_subplot(3, 1, ix+1)  # nrows, ncols, index
        graph.set_title(sparam)
        key = [sparam, op]
        for name, data in [["hoge", hoge], ["fuga", fuga]]:
            seq = [x for x in data if x[0:2] == key][0]
            y = seq[2]
            x = range(len(y))
            graph.plot(x, y, label=name)
            graph.legend()
        graph.set_ylabel(sparam+' value')
    pyplot.tight_layout()
    fig.text(0.5, 0.02, 'x label', ha='center', va='center')
    fig.subplots_adjust(top=0.9)
    fig.align_labels()


A4_PORTRAIT = (8.27, 11.69)
A4_LANDSCAPE = (11.69, 8.27)


def main():
    hoge = read_csv("hoge.csv")
    fuga = read_csv("fuga.csv")
    for op in ["aap", "noot", "mies", "zus", "jet"]:
        plot_op(pyplot.figure(figsize=A4_PORTRAIT), hoge, fuga, op)
    write_pdf("graph.pdf")


main()
