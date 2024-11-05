import seaborn
import seaborn.objects
import matplotlib.pyplot as plt
import matplotlib.figure as mpl
import scipy.stats
import numpy

if __name__ == "__main__":
    max_float = 0.99999999
    min_float = 0.00000001
    delta = 0.14
    laplace_dis = scipy.stats.laplace
    point = numpy.linspace(laplace_dis.ppf(min_float), laplace_dis.ppf(max_float), 1000)
    max_limit = point.max()
    shade_right = numpy.linspace(max_limit * delta, max_limit, 500)
    shade_left = numpy.linspace(-max_limit, max_limit * delta, 500)

    print("Seaborn object")
    plot = seaborn.objects.Plot(x=point, y=laplace_dis.pdf(point))
    plot = plot.add(seaborn.objects.Line())
    plot_figure = plt.figure()
    plot_plot = plot.on(plot_figure).plot()
    plot_ax = plot_figure.axes[0]
    plot_ax.fill_between(x=shade_left, y1=laplace_dis.pdf(shade_left), alpha=0.5)
    plot_ax.fill_between(x=shade_right, y1=laplace_dis.pdf(shade_right), alpha=0.5)
    plot_plot.show()
